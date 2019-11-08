""" 
@author: lileilei
@file: ddd.py 
@time: 2018/1/19 11:43 
"""
import os
import unittest

import xlrd
from Common.log import log1


def get_test_data(filepath, index):
    try:
        file = xlrd.open_workbook(filepath)
        me = file.sheets()[index]
        nrows = me.nrows
        listdata = []
        for i in range(1, nrows):
            dict_canshu = {}
            dict_canshu['case_name'] = me.cell(i, 0).value
            dict_canshu.update(eval(me.cell(i, 2).value))
            dict_canshu.update(eval(me.cell(i, 3).value))
            listdata.append(dict_canshu)
        return listdata
    except Exception as e:
        log1.error('获取测试用例数据失败，原因：%s' % e)

# test_dir = './testcase/'

def find_pyfile_and_import(rootDir):
    if os.path.exists(rootDir):
        arr = rootDir.split("/")
        pathDir = ""
        for path in arr:
            pathDir = pathDir + path + "/"
            if not os.path.exists(pathDir + "/__init__.py"):
                f = open(pathDir + "/__init__.py", 'w')
                f.close()
    list_dirs = os.walk(rootDir)
    #print(list_dirs)
    for dirName, subdirList, fileList in list_dirs:
        print(dirName)
        #print(subdirList)
        print(fileList)
        for f in fileList:
            file_name = f
            print("filename:%s" % file_name)
            #print("123123123" + file_name[0:5])
            if file_name[0:5] == "text_" and file_name[-3:] == ".py":
                print( "123123123"+file_name[0:5])
                if dirName[-1:] != "/":
                    print(dirName[-1:])
                    impPath = dirName.replace("/", ".")[2:].replace("\\", ".")
                    print("impPath:::%s" %impPath)
                else:
                    impPath = dirName.replace("/", ".")[2:-1]
                    print("impPath:%s" % impPath)
                if impPath != "":
                    exe_str = "from" + impPath + "import" + file_name[0:-3]
                    print("exe_str:%s" % exe_str)
                else:
                    exe_str = "import" + file_name[0:-3]
                    print("exe_str:%s" % exe_str)
                exec(exe_str, globals())
                #print( exec(exe_str, globals()))


def get_xls_case_by_index(filepath, sheet_name):
    #global col_1, col_2, col_3
    file = xlrd.open_workbook(filepath)
    sheet = file.sheet_by_name(sheet_name)
    ncols = sheet.ncols
    for j in range(ncols):
        cell_value = sheet.cell_value(0, j)
        if cell_value == "fileName":
            col_1 = j
        if cell_value == "className":
            col_2 = j
        if cell_value == "caseName":
            col_3 = j
    nrows = sheet.nrows
    caseList = []
    for i in range(1, nrows):
        if sheet.row_values(i)[0].lower().strip() == 'ready':
            fileName = sheet.cell_value(i, col_1)
            className = sheet.cell_value(i, col_2)
            caseName = sheet.cell_value(i, col_3)
            case = '%s.%s("%s")' % (fileName.strip(), className.strip(), caseName.strip())
            caseList.append(case)
    return caseList

# test_dir = './testcase/'

def gen_test_suite(testDir):
    case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                             'excels', 'case_list.xlsx')
    testunit = unittest.TestSuite()
    find_pyfile_and_import(testDir)
    testCaseList = get_xls_case_by_index(case_path, 'login')
    print(testCaseList)
    for test_case in testCaseList:
        print(test_case)
        testunit.addTest(eval(test_case))
    return testunit