import os

from Common.basePage import BasePage
from Common.getYaml import get_yaml
import urllib.request
from Common.log import log1
from aip import AipOcr
d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')


class FloatingWindow(BasePage):
    data = get_yaml()
    link_app_download = data['links'].get('link_app_download')  # APP下载页面
    link_float_huiyuan = data['links'].get('link_float_huiyuan')
    link_float_kefu = data['links'].get('link_float_kefu')
    link_float_transfer = data['links'].get('link_float_transfer') # 支付秒到帐
    link_float_guanjia = data['links'].get('link_float_guanjia') # 金管家
    link_float_r_close  = data['links'].get('link_float_r_close')# 右侧悬浮窗关闭按钮
    link_float_l_close = data['links'].get('link_float_l_close')# 左侧悬浮窗关闭按钮
    link_float_jiebei = data['links'].get('link_float_jiebei') # 金管家
    link_carousel_announcement = data['links'].get('link_carousel_announcement') # 轮播公告

    assert_public_zhucezhanghao = data['links'].get('assert_public_zhucezhanghao')
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网站公告
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')  # 获取警告提示框信息
    pop_register_war_text = data['pop_box'].get('pop_register_war_text')
    assert_public_email_element = data['asserts'].get('assert_public_email_element')
    assert_public_en_element = data['asserts'].get('assert_public_en_element')
    btn_register_confirm = data['buttons'].get('btn_register_confirm')
    btn_login = data['buttons'].get('btn_login')  # 登录按钮
    btn_code_login = data['buttons'].get('btn_code_login')  # 验证码登录按钮
    btn_login_code_image = data['buttons'].get('btn_login_code_image')  # 登录验证码
    input_login_code = data['inputs'].get('input_login_code')  # 验证码输入框
    input_login_username = data['inputs'].get('input_login_username')  # 登录用户名元素定位
    input_login_password = data['inputs'].get('input_login_password')  # 登录密码元素定位

    tab_system_message = data['tabs'].get('tab_system_message')  #
    tab_deposit_bank = data['tabs'].get('tab_deposit_bank')  #

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def visit_float_huiyuan(self):
        """
        Visit the 加入会员 page
        :return:
        """
        self.click(self.link_float_huiyuan)

    def visit_float_transfer(self,suc):
        """
        访问右侧悬浮窗支付秒到帐
        :return:
        """
        self.click(self.link_float_transfer)
        self.click_close_warning()
        if suc == "0":
            war_text = self.get_text(self.pop_public_waring_text)
            return war_text

    def visit_login_float_transfer(self, suc):
        """
        访问右侧悬浮窗支付秒到帐
        :return:
        """
        self.click(self.link_float_transfer)
        if suc == "0":
            war_text = self.get_text(self.tab_deposit_bank)
            return war_text

    def visit_float_guanjia(self):
        """
        访问左侧悬浮窗金管家页面
        :return:
        """
        self.open_new_window(self.link_float_guanjia)

    def visit_float_jiebei(self):
        """
        访问左侧悬浮窗免息借呗
        :return:
        """
        self.open_new_window(self.link_float_jiebei)

    def visit_float_r_close(self):
        """
        关闭右侧悬浮窗
        :return:
        """
        self.click(self.link_float_r_close)

    def visit_float_l_close(self):
        """
        关闭左侧悬浮窗
        :return:
        """
        self.click(self.link_float_r_close)

    def visit_carousel_announcement(self,suc):
        """
        访问轮播公告
        :return:
        """
        self.click(self.link_carousel_announcement)
        self.click_close_warning()
        if suc == "0":
            war_text = self.get_text(self.pop_public_waring_text)
            return war_text

    def visit_login_carousel_announcement(self):
        """
        访问轮播公告
        :return:
        """
        self.click(self.link_carousel_announcement)

    def get_car_announcement(self):
        """
        获取系统信息标题
        :return:
        """
        war_text = self.get_text(self.tab_system_message)
        return war_text

    def click_close_warning(self):
        """
        Close the warning box
        :return:
        """
        self.click(self.pop_public_waring_close)

    def get_huiyuan_text(self,suc):
        """
        获取加入会员的校验信息
        :return:
        """
        self.click(self.btn_register_confirm)
        if suc == "0":
            _toast_text = self.get_text(self.pop_register_war_text)
            return _toast_text

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_public_waring_text)
        return war_text

    def visit_float_customer(self):
        """在线客服"""
        self.open_new_window(self.link_float_kefu)

    def get_float_customer_cn(self):
        """
        Get description information of online customer service(Chinese Version)
        :return:
        """
        customer_text_cn = self.get_text(self.assert_public_email_element)
        return customer_text_cn


    def type_login_username(self, username):
        """
        登录方法，输入账号信息
        :param username:
        :return:
        """
        self.type(self.input_login_username, username)

    def type_login_password(self, password):
        """
        登录方法，输入密码
        :param password:
        :return:
        """
        self.type(self.input_login_password, password)

    def click_check_code_img(self):
        """
        点击验证码图标，刷新验证码
        :return:
        """
        self.click(self.btn_login_code_image)

    def click_login_btn(self):
        """
        没有验证码的登录按钮
        :return:
        """
        self.click(self.btn_login)

    def click_code_login_btn(self):
        """
        存在验证码的登录按钮
        :return:
        """
        self.click(self.btn_code_login)

    def type_login_code(self, code):
        """
        验证码输入框
        :param code:
        :return:
        """
        self.type(self.input_login_code, code)

    def click_login_close_warning(self):
        """
        Close the warning box
        :return:
        """
        self.click(self.pop_public_waring_close)

    def find_type_login_code(self):
        """
        登录系统
        :param suc: 0
        :param username: yusheng
        :param password: 12345678
        :return:
        """
        try:
            flg = self.get_displayed(self.input_login_code)
            if flg:
                img_str = self.driver.find_element_by_id('vPic')
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
                for i in msg.get('words_result'):
                    print(i.get('words'))
                    self.code = i.get('words')
                self.type_login_code(self.code)
                i.close()
                self.click_code_login_btn()
                ver_error = '验证码错误' in self.get_war_text()
                inp_code = '请输入4位验证码' in self.get_war_text()
                while (inp_code or ver_error):
                    if inp_code:
                        self.forced_wait(1)
                        self.click_login_close_warning()
                        self.forced_wait(1)
                        self.click_check_code_img()
                        self.forced_wait(1)
                        img_str = self.driver.find_element_by_id('vPic')
                        code_str = img_str.get_attribute('src')
                        urllib.request.urlretrieve(code_str, code_path)
                        APP_ID = '17161646'
                        API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
                        SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
                        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
                        j = open(code_path, 'rb')
                        img = j.read()
                        msg = client.basicGeneral(img)
                        # msg是一个字典，其中words_result中包含了文字信息
                        for code_k in msg.get('words_result'):
                            print(code_k.get('words'))
                            self.code = code_k.get('words')
                        self.forced_wait(1)
                        self.type_login_code(self.code)
                        j.close()
                        self.forced_wait(1)
                        self.click_code_login_btn()
                    if ver_error:
                        self.forced_wait(1)
                        self.click_login_close_warning()
                        self.forced_wait(1)
                        self.click_check_code_img()
                        self.forced_wait(1)
                        img_str = self.driver.find_element_by_id('vPic')
                        code_str = img_str.get_attribute('src')
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
                        self.forced_wait(1)
                        self.type_login_code(self.code)
                        k.close()
                        self.forced_wait(1)
                        self.click_code_login_btn()
        except Exception as e:
            self.click_login_btn()
            log1.error('定位验证码元素失败，原因：界面不存在验证码-%s' % e)
