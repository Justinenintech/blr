import datetime
import os
from shutil import copyfile

from Common.config import Config

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report')
abspath = os.path.join(os.path.abspath(d)+'/')
print(abspath)
config = Config()

def new_file(testdir):
    # d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report')
    # abspath = os.path.join(os.path.abspath(d) + '/')
    # 列出目录下所有的文件
    list = os.listdir(testdir)
    # 对文件修改时间进行升序排列
    list.sort(key=lambda fn:os.path.getmtime(testdir+fn))
    list.sort(key=lambda fn: testdir)
    # 获取最新修改时间的文件
    filetime = datetime.datetime.fromtimestamp(os.path.getmtime(testdir + list[-1]))
    print('获取最新修改时间的文件:%s'%filetime)
    # 获取文件所在目录
    filepath = os.path.join(testdir, list[-1])
    print("最新修改的文件："+list[-1])
    print("时间："+filetime.strftime('%Y-%m-%d %H-%M-%S'))
    pro_copy = config.config_read('copy', 'pro_copy')
    copyfile(filepath, pro_copy + list[-1])
    return list[-1]


# 返回最新文件或文件夹名：
# # print(new_file(u"D:\\xampp\\htdocs\\tycijt\\"))
# print(new_file(abspath))
