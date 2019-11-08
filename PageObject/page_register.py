import os
import re
import urllib.request

from aip import AipOcr

from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1
from Common.update_yaml import update_last_username, update_newest_username

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')


class PageRegister(BasePage):
    data = get_yaml()
    link_register = data['links'].get('link_register')  # 元素定位，注册按钮
    re_user = data['inputs'].get('input_register_username')  # 元素定位，注册页面，会员账号
    pwd_one = data['inputs'].get('input_register_password_one')  # 元素定位，注册页面，密码
    pwd_two = data['inputs'].get('input_register_password_two')  # 元素定位，注册页面，确认密码
    re_code = data['inputs'].get('input_register_code')  # 元素定位，注册页面，验证码
    re_phone = data['inputs'].get('input_register_phone')  # 元素定位，注册页面，手机号码
    btn_register_confirm = data['buttons'].get('btn_register_confirm')  # 元素定位，注册页面，确认按钮
    btn_register_reset = data['buttons'].get('btn_register_reset')  # 元素定位，重置按钮
    btn_register_code_image = data['buttons'].get('btn_register_code_image')
    tab_register_null = data['pop_box'].get('tab_register_null')

    assert_public_username = data['asserts'].get('assert_public_username')  # 获取登录账号信息
    pop_register_war_close = data['pop_box'].get('pop_register_war_close')  # 注册警告提示框，关闭按钮
    pop_register_war_text = data['pop_box'].get('pop_register_war_text')  # 获取警告提示框信息
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网页公告
    data_newest_username = data['datas'].get('data_newest_username')

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def visit_register_page(self):
        """
        访问注册页面
        :return:
        """
        self.click(self.link_register)

    def register_warning(self, suc, username, password, passwd, code, phone):
        """
        检测注册功能的字段校验是否符合规则
        :param suc: 0
        :param username: 账号
        :param password: 密码
        :param passwd: 确认密码
        :param code: 验证码
        :param phone: 手机号码
        :return: .ivu-icon-ios-close-empty
        """
        try:
            # self.find_click_notice()
            # self.visit_register_page()
            self.type_register_username(username)  # 输入账号
            #self.forced_wait(1)
            self.type_register_password(password)  # 输入密码
            #self.forced_wait(1)
            self.type_register_passwd(passwd)  # 输入确认密码
            #self.forced_wait(1)
            self.type_register_code(code)  # 输入验证码
            #self.forced_wait(1)
            self.type_register_phone(phone)  # 输入手机号
            self.click_register_ok()
            # self.forced_wait(1)
            # if self.get_displayed(self.pop_register_war_close):
            #     self.click_close_warning()
            # else:
            #     self.click_register_ok()
            #     self.forced_wait(1)
            #     self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_register_war_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def click_reset(self, suc, username, password, passwd, phone, code):
        """
        检测重置功能是否成功
        :return:
        """
        try:
            self.find_click_notice()
            self.visit_register_page()
            self.type_register_username(username)  # 输入账号
            self.type_register_password(password)  # 输入密码
            self.type_register_passwd(passwd)  # 输入确认密码
            self.type_register_code(code)  # 输入验证码
            self.type_register_phone(phone)  # 输入手机号码
            # 点击重置按钮
            self.click(self.btn_register_reset)
            # 点击确认按钮
            self.click(self.btn_register_confirm)
            # self.forced_wait(1)
            # self.click(self.pop_register_war_close)
            if suc == '0':
                _war_text = self.get_text(self.pop_register_war_text)
                return _war_text
        except Exception as e:
            log1.error('用例执行失败，原因：%s' % e)

    def type_register_username(self, username):
        self.type_send(self.re_user, username)

    def type_register_password(self, password):
        self.type_send(self.pwd_one, password)

    def type_register_passwd(self, passwd):
        self.type_send(self.pwd_two, passwd)

    def type_register_code(self, code):
        self.type_send(self.re_code, code)

    def type_register_phone(self, phone):
        self.type_send(self.re_phone, phone)

    def click_register_ok(self):
        self.click(self.btn_register_confirm)

    def click_check_code_img(self):
        self.click(self.btn_register_code_image)

    def click_close_warning(self):
        """
        Close the warning box
        :return:
        """
        self.click(self.pop_register_war_close)

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_register_war_text)
        return war_text

    def get_username_text(self):
        """
        get login username value
        :return:
        """
        _user_text = self.get_text(self.assert_public_username)
        return _user_text
    #
    # def find_type_login_code(self):
    #     """
    #     登录系统
    #     :param suc: 0
    #     :param username: yusheng
    #     :param password: 12345678
    #     :return:
    #     """
    #     try:
    #         img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #         # log1.info(img_str)
    #         code_str = img_str.get_attribute('src')
    #         # log1.info(code_str)
    #         urllib.request.urlretrieve(code_str, code_path)
    #         APP_ID = '17161646'
    #         API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #         SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #         client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #         i = open(code_path, 'rb')
    #         img = i.read()
    #         msg = client.basicGeneral(img)
    #         # msg是一个字典，其中words_result中包含了文字信息
    #         for code_i in msg.get('words_result'):
    #             print(code_i.get('words'))
    #             self.code = code_i.get('words')
    #         self.forced_wait(2)
    #         self.type_register_code(self.code)
    #         i.close()
    #         self.click_register_ok()
    #         self.forced_wait(2)
    #         while ('帐号已存在' in self.get_war_text()) or ('请输入4位验证码' in self.get_war_text()) or ('验证码错误' in self.get_war_text()):
    #             if '帐号已存在' in self.get_war_text():
    #                 log1.info("123131313132132131231313123123")
    #                 self.forced_wait(2)
    #                 self.click_close_warning()
    #                 self.forced_wait(1)
    #                 # self.link.forced_wait(2)
    #                 update_last_username(self.data_newest_username)
    #                 old_count = re.sub("\D", "", self.data_newest_username)
    #                 sum_count = int(old_count) + 1
    #                 global new_count
    #                 new_count = self.data_newest_username.replace(old_count, str(sum_count))
    #                 update_newest_username(new_count)
    #                 self.forced_wait(2)
    #                 self.type_register_username(new_count)
    #                 self.forced_wait(2)
    #                 self.click_check_code_img()
    #                 self.forced_wait(2)
    #                 img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #                 # log1.info(img_str)
    #                 code_str = img_str.get_attribute('src')
    #                 # log1.info(code_str)
    #                 urllib.request.urlretrieve(code_str, code_path)
    #                 APP_ID = '17161646'
    #                 API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #                 SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #                 client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #                 k = open(code_path, 'rb')
    #                 img = k.read()
    #                 msg = client.basicGeneral(img)
    #                 # msg是一个字典，其中words_result中包含了文字信息
    #                 for code_k in msg.get('words_result'):
    #                     print(code_k.get('words'))
    #                     self.code = code_k.get('words')
    #                 self.forced_wait(2)
    #                 self.type_register_code(self.code)
    #                 k.close()
    #                 # self.link.forced_wait(5)
    #                 self.click_register_ok()
    #                 self.forced_wait(2)
    #             if '请输入4位验证码' in self.get_war_text():
    #                 self.forced_wait(2)
    #                 self.click_close_warning()
    #                 self.forced_wait(1)
    #                 self.click_check_code_img()
    #                 self.forced_wait(1)
    #                 img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #                 # log1.info(img_str)
    #                 code_str = img_str.get_attribute('src')
    #                 # log1.info(code_str)
    #                 urllib.request.urlretrieve(code_str, code_path)
    #                 APP_ID = '17161646'
    #                 API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #                 SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #                 client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #                 j = open(code_path, 'rb')
    #                 img = j.read()
    #                 msg = client.basicGeneral(img)
    #                 # msg是一个字典，其中words_result中包含了文字信息
    #                 for code_j in msg.get('words_result'):
    #                     print(code_j.get('words'))
    #                     self.code = code_j.get('words')
    #                 self.forced_wait(2)
    #                 self.type_register_code(self.code)
    #                 j.close()
    #                 self.click_register_ok()
    #                 self.forced_wait(2)
    #             if '验证码错误' in self.get_war_text():
    #                 self.forced_wait(2)
    #                 self.click_close_warning()
    #                 self.forced_wait(1)
    #                 self.click_check_code_img()
    #                 self.forced_wait(1)
    #                 img_str = self.driver.find_element_by_css_selector('.checkLoginCodeImage')
    #                 # log1.info(img_str)
    #                 code_str = img_str.get_attribute('src')
    #                 # log1.info(code_str)
    #                 urllib.request.urlretrieve(code_str, code_path)
    #                 APP_ID = '17161646'
    #                 API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
    #                 SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
    #                 client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    #                 h = open(code_path, 'rb')
    #                 img = h.read()
    #                 msg = client.basicGeneral(img)
    #                 # msg是一个字典，其中words_result中包含了文字信息
    #                 for code_h in msg.get('words_result'):
    #                     print(code_h.get('words'))
    #                     self.code = code_h.get('words')
    #                 self.forced_wait(2)
    #                 self.type_register_code(self.code)
    #                 h.close()
    #                 self.click_register_ok()
    #                 self.forced_wait(2)
    #     except BaseException as e:
    #         log1.error('定位验证码元素失败，原因：界面不存在验证码-%s' % e)