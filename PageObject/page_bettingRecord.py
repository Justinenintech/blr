import os
import urllib.request

from aip import AipOcr

from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')


class PageBettingRecord(BasePage):
    # yaml文件读取
    data = get_yaml()
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')  # 获取警告提示框信息
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')  # 关闭警告提示框信息
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网页公告
    input_login_username = data['inputs'].get('input_login_username')  # 登录用户名元素定位
    input_login_password = data['inputs'].get('input_login_password')  # 登录密码元素定位
    btn_login = data['buttons'].get('btn_login')  # 登录按钮
    btn_code_login = data['buttons'].get('btn_code_login')  # 验证码登录按钮
    btn_login_code_image = data['buttons'].get('btn_login_code_image')  # 登录验证码
    toast_text = data['pop_box'].get('pop_toast_text')  # 弹出即消失的提示框
    btn_submit = data['buttons'].get('btn_submit')  # 账号安全确认提交元素定位
    input_login_code = data['inputs'].get('input_login_code')  # 验证码输入框

    link_betting_record = data['links'].get('link_betting_record')  # 投注记录
    get_betting_record = data['buttons'].get('get_betting_record')  # 实时返水

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

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

    def type_login_code(self, code):
        """
        验证码输入框
        :param code:
        :return:
        """
        self.type(self.input_login_code, code)

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

    def get_toast_text(self):
        """
        弹出提示信息
        :return:
        """
        _toast_text = self.get_text(self.toast_text)
        return _toast_text

    def click_close_warning(self):
        """
        Close the warning box
        :return:
        """
        self.click(self.pop_public_waring_close)

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_public_waring_text)
        return war_text

    def click_check_code_img(self):
        """
        点击验证码图标，刷新验证码
        :return:
        """
        self.click(self.btn_login_code_image)

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
                self.click_code_login_btn()
                while (('请输入4位验证码' in self.get_war_text()) or ('验证码错误' in self.get_war_text())):
                    if '请输入4位验证码' in self.get_war_text():
                        self.forced_wait(1)
                        self.click_close_warning()
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
                        i = open(code_path, 'rb')
                        img = i.read()
                        msg = client.basicGeneral(img)
                        # msg是一个字典，其中words_result中包含了文字信息
                        for i in msg.get('words_result'):
                            print(i.get('words'))
                            self.code = i.get('words')
                        self.forced_wait(1)
                        self.type_login_code(self.code)
                        self.forced_wait(1)
                        self.click_code_login_btn()
                    if '验证码错误' in self.get_war_text():
                        self.forced_wait(1)
                        self.click_close_warning()
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
                        i = open(code_path, 'rb')
                        img = i.read()
                        msg = client.basicGeneral(img)
                        # msg是一个字典，其中words_result中包含了文字信息
                        for i in msg.get('words_result'):
                            print(i.get('words'))
                            self.code = i.get('words')
                        self.forced_wait(1)
                        self.type_login_code(self.code)
                        self.forced_wait(1)
                        self.click_code_login_btn()
        except Exception as e:
            self.click_login_btn()
            log1.error('定位验证码元素失败，原因：界面不存在验证码-%s' % e)

    def click_link_betting_record(self):
        """
        访问投注记录
        :return:
        """
        self.click(self.link_betting_record)

    def verity_get_betting_record(self):
        _text = self.get_text(self.get_betting_record)
        return _text
