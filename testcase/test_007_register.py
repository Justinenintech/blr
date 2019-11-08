import os
import re
import unittest
import urllib
from urllib import request

import ddt
import yaml
from BeautifulReport import BeautifulReport
from aip import AipOcr

from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml
from Common.log import log1
from Common.update_yaml import update_last_username, update_newest_username
from PageObject.page_register import PageRegister

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 1)

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')
""" 测试报告的基础用例Sample """
# _path = abspath
# code_path = _path + '\\test_code.jpg'
# yaml文件读取
data = get_yaml()
pop_register_war_text = data['pop_box'].get('pop_register_war_text')  # 获取警告提示框信息

@ddt.ddt
class TestRegister(unittest.TestCase):

    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath
    # yaml文件读取
    data = get_yaml()
    data_newest_username = data['datas'].get('data_newest_username')
    data_password = data['datas'].get('data_password')
    data_phone = data['datas'].get('data_phone')
    data_suc = data['datas'].get('data_suc')
    assert_register_reset = data['datas'].get('assert_register_reset')
    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')
    pop_register_war_text = data['pop_box'].get('pop_register_war_text')  # 获取警告提示框信息

    def save_img(self, img_name):
        """
        传入一个img_name, 并存储到默认的文件路径下
        param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @classmethod
    def setUpClass(cls) -> None:
        browser = BasePage(cls)
        cls.driver = browser.open_browser()

    def setUp(self) -> None:
        self.link = PageRegister(self.driver)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.link = PageRegister(cls.driver)
        cls.link.dr_quit()

    def test_register_account_001(self):
        """注册测试用例-重置功能"""
        self.case_name = ""
        log1.info("Executing use test case:%s" % self.case_name)
        self.suc = '0'
        self.username = 'enintech0'
        self.password = '12345678'
        self.code = '1234'
        self.phone = '13898378887'
        self.re_data = self.link.click_reset(self.suc,self.username,self.password,self.password,self.phone,self.code)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_register_reset,
                             self.output_verify_fail % (self.assert_register_reset, self.re_data))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_register_reset, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.info('Failure of test case execution! Reason: %s' % e + '\n')

    @BeautifulReport.add_test_img('test_register_account_002')
    @ddt.data(*case_data)
    def test_register_account_002(self, data):
        """注册测试用例"""
        self.case_name = data['case_name']
        log1.info("Executing use test case:%s" % self.case_name)
        # 获取注册账号
        self.username = data['username']
        # 获取注册密码
        self.password = data['password']
        # 获取注册确认密码
        self.passwd = data['passwd']
        # 获取判断标识
        self.suc = data['suc']
        # 获取验证码
        self.code = data['code']
        # 获取手机号码
        self.phone = data['phone']
        # 获取预期值
        self.assert_value = data['assert_vale']
        # 输出获取的测试数据
        log1.info('input data:username:%s,password:%s,passwd:%s,phone:%s,code:%s,suc:%s,assert:%s' % (
            self.username, self.password, self.passwd, self.code, self.phone,self.suc, self.assert_value))
        # 执行注册通用方法
        self.re_data = self.link.register_warning(self.suc, self.username, self.password, self.passwd,
                                                  self.code,self.phone)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data.replace(" ",""), self.assert_value.replace(" ",""),
                             self.output_verify_fail % (self.assert_value.replace(" ",""), self.re_data.replace(" ","")))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_value.replace(" ",""), self.re_data.replace(" ","")))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    # @BeautifulReport.add_test_img('test_register_account_003')
    # def test_register_account_003(self):
    #     """检测是否能够成功注册账号"""
    #     # self.link.forced_wait(5)
    #     self.case_name = '检测是否能够成功注册账号'
    #     log1.info("Executing use test case:%s" % self.case_name)
    #     # # 判断是否存在网站公告，如果存在则关闭公告提示！
    #     # self.link.find_click_notice()
    #     # # 访问注册页面
    #     # self.link.visit_register_page()
    #     # 输入测试数据
    #     self.link.type_register_username(self.data_newest_username)
    #     self.link.type_register_password(self.data_password)
    #     self.link.type_register_passwd(self.data_password)
    #     self.link.type_register_phone(self.data_phone)
    #     img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #     code_str = img_str.get_attribute('src')
    #     urllib.request.urlretrieve(code_str, code_path)
    #     APP_ID = '17161646'
    #     API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #     SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #     client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #     i = open(code_path, 'rb')
    #     img = i.read()
    #     msg = client.basicGeneral(img)
    #     # msg是一个字典，其中words_result中包含了文字信息
    #     for code_i in msg.get('words_result'):
    #         print(code_i.get('words'))
    #         self.code = code_i.get('words')
    #     self.link.forced_wait(2)
    #     self.link.type_register_code(self.code)
    #     i.close()
    #     self.link.click_register_ok()
    #     self.link.forced_wait(2)
    #     while ('帐号已存在' in self.link.get_war_text()) or ('请输入4位验证码' in self.link.get_war_text()) or (
    #             '验证码错误' in self.link.get_war_text()):
    #         if '帐号已存在' in self.link.get_war_text():
    #             self.link.forced_wait(2)
    #             # # self.link.click_close_warning()
    #             # self.link.forced_wait(1)
    #             # self.link.forced_wait(2)
    #             global new_count
    #             # yaml文件读取
    #             data = get_yaml()
    #             data_newest_username = data['datas'].get('data_newest_username')
    #             update_last_username(data_newest_username)
    #             old_count = re.sub("\D", "", data_newest_username)
    #             sum_count = int(old_count) + 1
    #             new_count = data_newest_username.replace(old_count, str(sum_count))
    #             update_newest_username(new_count)
    #             self.link.forced_wait(2)
    #             self.link.type_register_username(new_count)
    #             self.link.forced_wait(2)
    #             self.link.click_check_code_img()
    #             self.link.forced_wait(2)
    #             img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #             # log1.info(img_str)
    #             code_str = img_str.get_attribute('src')
    #             # log1.info(code_str)
    #             urllib.request.urlretrieve(code_str, code_path)
    #             APP_ID = '17161646'
    #             API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #             SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #             client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #             k = open(code_path, 'rb')
    #             img = k.read()
    #             msg = client.basicGeneral(img)
    #             # msg是一个字典，其中words_result中包含了文字信息
    #             for code_k in msg.get('words_result'):
    #                 print(code_k.get('words'))
    #                 self.code = code_k.get('words')
    #             self.link.forced_wait(2)
    #             self.link.type_register_code(self.code)
    #             k.close()
    #             # self.link.forced_wait(5)
    #             self.link.click_register_ok()
    #             self.link.forced_wait(2)
    #             #continue
    #         if '请输入4位验证码' in self.link.get_war_text():
    #             self.link.forced_wait(2)
    #             # self.link.click_close_warning()
    #             # self.link.forced_wait(1)
    #             self.link.click_check_code_img()
    #             self.link.forced_wait(1)
    #             img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #             # log1.info(img_str)
    #             code_str = img_str.get_attribute('src')
    #             # log1.info(code_str)
    #             urllib.request.urlretrieve(code_str, code_path)
    #             APP_ID = '17161646'
    #             API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #             SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #             client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #             j = open(code_path, 'rb')
    #             img = j.read()
    #             msg = client.basicGeneral(img)
    #             # msg是一个字典，其中words_result中包含了文字信息
    #             for code_j in msg.get('words_result'):
    #                 print(code_j.get('words'))
    #                 self.code = code_j.get('words')
    #             self.link.forced_wait(2)
    #             self.link.type_register_code(self.code)
    #             j.close()
    #             self.link.click_register_ok()
    #             self.link.forced_wait(2)
    #             #continue
    #         if '验证码错误' in self.link.get_war_text():
    #             self.link.forced_wait(2)
    #             # self.link.click_close_warning()
    #             # self.link.forced_wait(1)
    #             self.link.click_check_code_img()
    #             self.link.forced_wait(1)
    #             img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #             # log1.info(img_str)
    #             code_str = img_str.get_attribute('src')
    #             # log1.info(code_str)
    #             urllib.request.urlretrieve(code_str, code_path)
    #             APP_ID = '17161646'
    #             API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #             SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #             client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #             h = open(code_path, 'rb')
    #             img = h.read()
    #             msg = client.basicGeneral(img)
    #             # msg是一个字典，其中words_result中包含了文字信息
    #             for code_h in msg.get('words_result'):
    #                 print(code_h.get('words'))
    #                 self.code = code_h.get('words')
    #             self.link.forced_wait(2)
    #             self.link.type_register_code(self.code)
    #             h.close()
    #             self.link.click_register_ok()
    #             self.link.forced_wait(2)
    #             #continue
    #     try:
    #         check_name = self.link.get_username_text()
    #         # 校验预期结果与实际结果是否一致
    #         self.assertIsNotNone(check_name.replace(" ", ""))
    #         # 将结果输出到日志文件
    #         log1.info(check_name.replace(" ", ""))
    #         # 保存截图
    #         self.link.save_window_snapshot('成功注册账号')
    #         # yaml文件读取
    #         data = get_yaml()
    #         data_newest_username = data['datas'].get('data_newest_username')
    #         update_last_username(data_newest_username)
    #         old_count = re.sub("\D", "", data_newest_username)
    #         sum_count = int(old_count) + 1
    #         self.new_count = data_newest_username.replace(old_count, str(sum_count))
    #         update_newest_username(self.new_count)
    #         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
    #     except BaseException as e:
    #         self.save_img(self.case_name)
    #         log1.error('Failure of test case execution! Reason: %s' % e + '\n')
    #         #self.skipTest('IP被封无法注册～！，跳过用例test_register_account_003')
    #         raise


    @unittest.skip('IP被封无法注册～！，跳过用例test_register_account_003')
    @BeautifulReport.add_test_img('test_register_account_003')
    def test_register_account_003(self):
        """检测是否能够成功注册账号"""
        # self.link.forced_wait(5)
        self.case_name = '检测是否能够成功注册账号'
        log1.info("Executing use test case:%s" % self.case_name)
        # # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # # 访问注册页面
        # self.link.visit_register_page()
        # 输入测试数据
        self.link.type_register_username(self.data_newest_username)
        self.link.type_register_password(self.data_password)
        self.link.type_register_passwd(self.data_password)
        self.link.type_register_phone(self.data_phone)
        img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
        code_str = img_str.get_attribute('src')
        urllib.request.urlretrieve(code_str, code_path)
        APP_ID = '17161646'
        API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
        SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
        i = open(code_path, 'rb')
        img = i.read()
        msg = client.basicGeneral(img)
        # msg是一个字典，其中words_result中包含了文字信息
        for code_i in msg.get('words_result'):
            print(code_i.get('words'))
            self.code = code_i.get('words')
        self.link.forced_wait(2)
        self.link.type_register_code(self.code)
        i.close()
        self.link.click_register_ok()
        self.link.forced_wait(2)

        if self.link.get_exist(self.pop_register_war_text):
            alr_exists = '帐号已存在' in self.link.get_war_text()
            ver_error = '验证码错误' in self.link.get_war_text()
            inp_code = '请输入4位验证码' in self.link.get_war_text()
            while (alr_exists or ver_error or inp_code):
                if alr_exists:
                    self.link.forced_wait(1)
                    # self.link.click_close_warning()
                    # self.link.forced_wait(1)
                    global new_count
                    # yaml文件读取
                    data = get_yaml()
                    data_newest_username = data['datas'].get('data_newest_username')
                    update_last_username(data_newest_username)
                    old_count = re.sub("\D", "", data_newest_username)
                    sum_count = int(old_count) + 1
                    new_count = data_newest_username.replace(old_count, str(sum_count))
                    update_newest_username(new_count)
                    self.link.forced_wait(2)
                    self.link.type_register_username(new_count)
                    self.link.forced_wait(2)
                    self.link.click_check_code_img()
                    self.link.forced_wait(2)
                    img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
                    # log1.info(img_str)
                    code_str = img_str.get_attribute('src')
                    # log1.info(code_str)
                    urllib.request.urlretrieve(code_str, code_path)
                    APP_ID = '17161646'
                    API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
                    SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
                    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
                    k = open(code_path, 'rb')
                    img = k.read()
                    msg = client.basicGeneral(img)
                    # msg是一个字典，其中words_result中包含了文字信息
                    for code_k in msg.get('words_result'):
                        print(code_k.get('words'))
                        self.code = code_k.get('words')
                    self.link.forced_wait(2)
                    self.link.type_register_code(self.code)
                    k.close()
                    # self.link.forced_wait(5)
                    self.link.click_register_ok()
                    self.link.forced_wait(2)
                if inp_code:
                    # self.link.forced_wait(2)
                    # self.link.click_close_warning()
                    self.link.forced_wait(1)
                    self.link.click_check_code_img()
                    self.link.forced_wait(1)
                    img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
                    # log1.info(img_str)
                    code_str = img_str.get_attribute('src')
                    # log1.info(code_str)
                    urllib.request.urlretrieve(code_str, code_path)
                    APP_ID = '17161646'
                    API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
                    SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
                    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
                    j = open(code_path, 'rb')
                    img = j.read()
                    msg = client.basicGeneral(img)
                    # msg是一个字典，其中words_result中包含了文字信息
                    for code_j in msg.get('words_result'):
                        print(code_j.get('words'))
                        self.code = code_j.get('words')
                    self.link.forced_wait(2)
                    self.link.type_register_code(self.code)
                    j.close()
                    self.link.click_register_ok()
                    self.link.forced_wait(2)
                if ver_error:
                    # self.link.forced_wait(2)
                    # self.link.click_close_warning()
                    self.link.forced_wait(1)
                    self.link.click_check_code_img()
                    self.link.forced_wait(1)
                    img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
                    # log1.info(img_str)
                    code_str = img_str.get_attribute('src')
                    # log1.info(code_str)
                    urllib.request.urlretrieve(code_str, code_path)
                    APP_ID = '17161646'
                    API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
                    SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
                    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
                    h = open(code_path, 'rb')
                    img = h.read()
                    msg = client.basicGeneral(img)
                    # msg是一个字典，其中words_result中包含了文字信息
                    for code_h in msg.get('words_result'):
                        print(code_h.get('words'))
                        self.code = code_h.get('words')
                    self.link.forced_wait(2)
                    self.link.type_register_code(self.code)
                    h.close()
                    self.link.click_register_ok()
                    self.link.forced_wait(2)
        # else:
        #     self.skipTest('IP被封无法注册～！，跳过用例test_register_account_003')
        try:
            check_name = self.link.get_username_text()
            # 校验预期结果与实际结果是否一致
            self.assertIsNotNone(check_name.replace(" ", ""))
            # 将结果输出到日志文件
            log1.info(check_name.replace(" ", ""))
            # 保存截图
            self.link.save_window_snapshot('成功注册账号')
            # yaml文件读取
            data = get_yaml()
            data_newest_username = data['datas'].get('data_newest_username')
            update_last_username(data_newest_username)
            old_count = re.sub("\D", "", data_newest_username)
            sum_count = int(old_count) + 1
            self.new_count = data_newest_username.replace(old_count, str(sum_count))
            update_newest_username(self.new_count)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            # update_last_username(self.data_newest_username)
            # old_count = re.sub("\D", "", self.data_newest_username)
            # sum_count = int(old_count) + 1
            # self.new_count = self.data_newest_username.replace(old_count, str(sum_count))
            # update_newest_username(self.new_count)
            self.save_img(self.case_name)
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise
