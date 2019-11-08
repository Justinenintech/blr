import os
import urllib.request

from aip import AipOcr

from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')


class PageMessages(BasePage):
    # yaml文件读取
    data = get_yaml()
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')  # 获取警告提示框信息
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')  # 关闭警告提示框信息
    pop_login_war_close = data['pop_box'].get('pop_login_war_close')
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网页公告
    input_login_username = data['inputs'].get('input_login_username')  # 登录用户名元素定位
    input_login_password = data['inputs'].get('input_login_password')  # 登录密码元素定位
    btn_login = data['buttons'].get('btn_login')  # 登录按钮
    btn_code_login = data['buttons'].get('btn_code_login')  # 验证码登录按钮
    btn_login_code_image = data['buttons'].get('btn_login_code_image')  # 登录验证码
    toast_text = data['pop_box'].get('pop_toast_text')  # 弹出即消失的提示框
    btn_submit = data['buttons'].get('btn_submit')  # 账号安全确认提交元素定位
    input_login_code = data['inputs'].get('input_login_code')  # 验证码输入框

    get_sys_msg_right_title = data['buttons'].get('get_sys_msg_right_title')  # 系统信息，右侧标题
    get_sys_msg_title = data['buttons'].get('get_sys_msg_title')  # 系统信息，中间标题
    get_sys_msg_time = data['buttons'].get('get_sys_msg_time')  # 系统信息，左侧日期
    get_sent_msg_title = data['buttons'].get('get_sent_msg_title')  # 获取已发送消息的标题
    get_sent_msg_area = data['buttons'].get('get_sent_msg_area')  # 获取已发送消息的内容
    tab_system_message = data['tabs'].get('tab_system_message')  # 系统信息
    tab_suggestions = data['tabs'].get('tab_suggestions')  # 投诉建议
    tab_sent_message = data['tabs'].get('tab_sent_message')  # 已发信息
    link_unread_message = data['links'].get('link_unread_message')  # 未读讯息
    input_suggestions_title = data['inputs'].get('input_suggestions_title')  # 投诉建议-标题
    input_suggestions_area = data['inputs'].get('input_suggestions_area')  # 投诉建议-标题
    assert_sys_message_el = data['asserts'].get('assert_sys_message_el')

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

    def type_input_suggestions_title(self, titles):
        """
        投诉建议-输入标题
        :param name:
        :return:
        """
        self.type(self.input_suggestions_title, titles)

    def type_input_suggestions_area(self, area):
        """
        投诉建议-输入内容
        :param name:
        :return:
        """
        self.type(self.input_suggestions_area, area)

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

    def click_login_close_warning(self):
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

    def verify_suggestion(self, suc, title, area):
        """
        验证是否能够提交投诉建议
        :param suc:
        :param name:
        :param card:
        :param pwd:
        :return:
        """
        try:
            self.type_input_suggestions_title(title)
            #self.type(self.input_suggestions_title, title)
            self.type_input_suggestions_area(area)
            self.click_submit()
            if suc == "0":
                _toast_text = self.get_text(self.toast_text)
                return _toast_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason: %s' % e)

    def click_link_unread_message(self):
        """
        访问未读讯息
        :return:
        """
        self.click(self.link_unread_message)

    def click_tab_suggestions(self):
        """
        切换投诉建议页面
        :return:
        """
        self.click(self.tab_suggestions)

    def click_tab_system_message(self):
        """
        切换到系统信息页面
        :return:
        """
        self.click(self.tab_system_message)

    def click_tab_sent_message(self):
        """
        切换到已发信息页面
        :return:
        """
        self.click(self.tab_sent_message)

    def verity_get_sys_msg_right_title(self):
        """
        新注册会员，获取系统消息右侧标题
        :return:
        """
        _text = self.get_text(self.get_sys_msg_right_title)
        return _text

    def verity_get_sys_msg_title(self):
        """
        新注册会员，获取系统消息中间标题
        :return:
        """
        _text = self.get_text(self.get_sys_msg_title)
        return _text

    def verity_get_sys_msg_time(self):
        """
        新注册会员，获取系统消息左侧日期
        :return:
        """
        _text = self.get_text(self.get_sys_msg_time)
        return _text

    def verity_sent_msg_title(self):
        """
        验证已发送消息的标题是否正确
        :return:
        """
        _text = self.get_text(self.get_sent_msg_title)
        return _text

    def verity_sent_msg_area(self):
        """
        验证已发送消息的标题是否正确
        :return:
        """
        _text = self.get_text(self.get_sent_msg_area)
        return _text

    def click_submit(self):
        """
        提交功能
        :return:
        """
        self.click(self.btn_submit)

    def get_assert_sys_message_el(self):
        """
        获取系统信息的标题
        :return:
        """
        _text = self.get_text(self.assert_sys_message_el)
        return _text