import os
import urllib.request

from aip import AipOcr

from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')

class PageUpdatePassword(BasePage):
    # yaml文件读取
    data = get_yaml()
    input_login_username = data['inputs'].get('input_login_username')  # 登录用户名元素定位
    input_login_password = data['inputs'].get('input_login_password')  # 登录密码元素定位
    input_update_password_1 = data['inputs'].get('input_update_password_1')  # 账号安全输入框元素定位
    input_update_password_2 = data['inputs'].get('input_update_password_2')  # 账号安全输入框元素定位
    input_update_password_3 = data['inputs'].get('input_update_password_3')  # 账号安全输入框元素定位
    input_update_password_4 = data['inputs'].get('input_update_password_4')  # 账号安全输入框元素定位
    input_update_password_5 = data['inputs'].get('input_update_password_5')  # 账号安全输入框元素定位
    btn_login_code_image = data['buttons'].get('btn_login_code_image')
    input_login_code = data['inputs'].get('input_login_code')  # 验证码输入框
    btn_code_login = data['buttons'].get('btn_code_login')  # 验证码登录按钮

    btn_submit = data['buttons'].get('btn_submitPay')  # 账号安全确认提交元素定位
    btn_login = data['buttons'].get('btn_login')  # 登录按钮
    select_security = data['buttons'].get('select_security')
    select_security_item = data['buttons'].get('select_security_item')

    link_member_centre = data['links'].get('link_member_centre')  # 会员中心
    link_account_security = data['links'].get('link_account_security')  # 账号安全页面
    link_unread_message = data['links'].get('link_unread_message')

    toast_text = data['pop_box'].get('pop_toast_text')  # 弹出即消失的提示框
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网站公告元素定位
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')  # 关闭警告弹出框元素定位
    pop_login_war_close = data['pop_box'].get('pop_login_war_close')
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')  # 获取警告提示框元素定位

    tab_security_login_pwd = data['tabs'].get('tab_security_login_pwd')  # 修改登录密码页面元素定位
    tab_security_fund_pwd = data['tabs'].get('tab_security_fund_pwd')  # 修改资金密码页面元素定位
    tab_security_secret_pwd = data['tabs'].get('tab_security_secret_pwd')  # 修改密保密码页面元素定位

    assert_public_username = data['asserts'].get('assert_public_username')  # 已登录账号名元素定位

    def find_click_notice(self):
        """
        locate whether the website announcement pops up,and close the website announcement if it pops up.
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def submit_update_password(self, suc, old_password, new_password, confirm_password):
        """
        Modify the encapsulation method of login password
        :param suc: 0
        :param old_password: old password
        :param new_password: new password
        :param confirm_password: confirm password
        :return: _toast_text
        """
        try:
            self.type_security_password_1(old_password)
            self.type_security_password_2(new_password)
            self.type_security_password_3(confirm_password)
            self.click_submit()
            if suc == '0':
                _toast_text = self.get_text(self.toast_text)
                return _toast_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def submit_set_fund_password(self, suc, fund_password, confirm_password):
        """
        Encapsulation method of setting up fund password
        :param suc:
        :param fund_password:
        :param confirm_password:
        :return:
        """
        try:
            self.click_fund_password_tab()
            self.type_security_password_1(fund_password)
            self.type_security_password_2(confirm_password)
           # self.type_security_password_4(answer)
            self.click_submit()
            if suc == "0":
                _toast_text = self.get_text(self.toast_text)
                return _toast_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason: %s' % e)

    def submit_update_fund_password(self, suc, old_pwd, new_pwd, confirm_pwd, security):
        """
        Modify the encapsulation method of fund password
        :param suc:
        :param old_pwd:
        :param new_pwd:
        :param confirm_pwd:
        :param security:
        :return:
        """
        try:
            self.click_fund_password_tab()
            self.type_security_password_1(old_pwd)
            self.type_security_password_2(new_pwd)
            self.type_security_password_3(confirm_pwd)
            self.type_security_password_5(security)
            # self.forced_wait(2)
            self.click_submit()
            if suc == "0":
                _toast_text = self.get_text(self.toast_text)
                return _toast_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason: %s' % e)

    def type_security_password_1(self, password):
        """
        input old password
        :param password: self.password
        :return:
        """
        self.type(self.input_update_password_1, password)

    def type_security_password_2(self, password):
        """
        input new password
        :param password: self.password
        :return:
        """
        self.type(self.input_update_password_2, password)

    def type_security_password_3(self, password):
        """
        input confirm password
        :param password: self.password
        :return:
        """
        self.type(self.input_update_password_3, password)

    def type_security_password_4(self, password):
        """
        input fund security password
        :param password:
        :return:
        """
        self.type(self.input_update_password_4, password)

    def type_security_password_5(self, password):
        """
        input fund security password
        :param password:
        :return:
        """
        self.type(self.input_update_password_5, password)

    def click_submit(self):
        """
        submit confirm button
        :return:
        """
        self.click(self.btn_submit)

    def visit_link_unread_message(self):
        """
        Asscess the unread message page
        :return:
        """
        self.click(self.link_unread_message)

    def visit_member_centre_page(self):
        """
        Access the update password page
        :return:
        """
        self.click(self.link_member_centre)

    def click_update_password_tab(self):
        """
        click update password tab
        :return:
        """
        self.click(self.tab_security_login_pwd)

    def visit_account_security_page(self):
        """
        click account security
        :return:
        """
        self.click(self.link_account_security)

    def click_fund_password_tab(self):
        """
        click tab set fund password link
        :return:
        """
        self.click(self.tab_security_fund_pwd)

    def click_security_password_tab(self):
        """
        click  update security password link
        :return:
        """
        self.click(self.tab_security_secret_pwd)

    def click_select_security(self):
        """
        click select security
        :return:
        """
        self.click(self.select_security)

    def click_select_security_item(self):
        """
        select security item
        :return:
        """
        self.move_to_element(self.select_security_item)
        self.click(self.select_security_item)

    def click_select_security_problem(self):
        """
        click select security problem
        :return:
        """
        self.click_select_security()
        self.click_select_security_item()

    def get_toast_text(self):
        """
        Get text information of toast pop-up type
        :return: _toast_text
        """
        _toast_text = self.get_text(self.toast_text)
        return _toast_text

    def get_username_text(self):
        """
        Get login name
        :return:
        """
        _user_text = self.get_text(self.assert_public_username)
        return _user_text

    def type_username(self, name):
        """
        input login username
        :param name: name
        :return:
        """
        self.type(self.input_login_username, name)

    def type_password(self, pwd):
        """
        input login password
        :param pwd:
        :return:
        """
        self.type(self.input_login_password, pwd)

    def click_login_btn(self):
        """
        click login button
        :return:
        """
        self.click(self.btn_login)

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

    def type_login_code(self, code):
        """
        验证码输入框
        :param code:
        :return:
        """
        self.type(self.input_login_code, code)

    def click_code_login_btn(self):
        """
        存在验证码的登录按钮
        :return:
        """
        self.click(self.btn_code_login)

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
                for code_i in msg.get('words_result'):
                    print(code_i.get('words'))
                    self.code = code_i.get('words')
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
        except BaseException as e:
            self.click_login_btn()
            log1.error('定位验证码元素失败，原因：界面不存在验证码-%s' % e)
