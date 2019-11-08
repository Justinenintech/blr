import os
import urllib.request

from aip import AipOcr

from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')


class PageOnlineWithdrawal(BasePage):
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
    link_online_withdrawal = data['links'].get('link_online_withdrawal')  # 线上取款
    input_deposit_binding_name = data['inputs'].get('input_deposit_binding_name')  # 绑定姓名弹出框的输入框
    input_zfb_h5 = data['inputs'].get('input_zfb_h5')  # 支付宝输入框
    btn_clear_time = data['buttons'].get('btn_clear_time')  # 清除已输入的时间
    pop_deposit_binding_name = data['pop_box'].get('pop_deposit_binding_name')  # 绑定姓名弹出框的提示信息
    pop_deposit_binding_cancel = data['pop_box'].get('pop_deposit_binding_cancel')  # 绑定姓名的取消按钮

    tab_withdrawal_request = data['tabs'].get('tab_withdrawal_request')  # 提款申请页面
    tab_withdrawal_bank_cards = data['tabs'].get('tab_withdrawal_bank_cards')  # 绑定银行卡页面

    input_login_code = data['inputs'].get('input_login_code')  # 判断验证码输入框是否可见
    input_update_password_1 = data['inputs'].get('input_update_password_1')  # 提款人姓名
    input_update_password_3 = data['inputs'].get('input_update_password_3')  # 银行卡号
    input_update_password_5 = data['inputs'].get('input_update_password_5')  # 资金密码

    select_bind_bank_card = data['buttons'].get('select_bind_bank_card')  # 开户银行下拉框
    select_bind_bank_card_item = data['buttons'].get('select_bind_bank_card_item')  # 开户银行下拉框内容-工商银行
    select_bind_city = data['buttons'].get('select_bind_city')  # 所在地下拉框
    select_bind_city_item = data['buttons'].get('select_bind_city_item')  # 所在地下拉框内容-北京市

    input_bind_card_name = data['inputs'].get('input_bind_card_name')  # 禁用状态的提款人姓名输入框

    get_bind_bank = data['buttons'].get('get_bind_bank')  # 绑定的银行
    get_bind_card = data['buttons'].get('get_bind_card')  # 绑定银行卡
    get_bind_name = data['buttons'].get('get_bind_name')  # 提款人姓名
    get_bind_time = data['buttons'].get('get_bind_time')  # 绑定时间

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def type_username_disabled(self):
        """判断输入框是否为disabled状态"""
        # type_repay = self.find_element(self.input_interestFreeIn_hk_amount).is_enabled()
        type_disabled= self.get_enabled(self.input_update_password_1)
        return type_disabled

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

    def type_input_update_password_1(self, name):
        """
        在提款人姓名输入框中输入内容
        :param name:
        :return:
        """
        self.type(self.input_update_password_1, name)

    def type_input_update_password_3(self, name):
        """
        在银行卡号输入框中输入内容
        :param name:
        :return:
        """
        self.type(self.input_update_password_3, name)

    def type_input_update_password_5(self, name):
        """
        在资金密码输入框中输入内容
        :param name:
        :return:
        """
        self.type(self.input_update_password_5, name)

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
        self.click(self.pop_login_war_close)

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_public_waring_text)
        return war_text

    def get_input_bind_card_name(self):
        """
        获取已绑定银行卡的，提款人姓名输入框状态
        :return:
        """
        flg = self.get_enabled(self.input_bind_card_name)
        return flg

    def get_click_submit(self):
        """
        获取确认提交按钮的状态
        :return:
        """
        flg = self.get_enabled(self.btn_submit)
        return flg

    def verity_get_bind_bank(self):
        """
        获取刚绑定的，开户银行
        :return:
        """
        _text = self.get_text(self.get_bind_bank)
        return _text

    def verity_get_bind_card(self):
        """
        获取刚绑定的，加密银行卡信息
        :return:
        """
        _text = self.get_text(self.get_bind_card)
        return _text

    def verity_get_bind_name(self):
        """
        获取刚绑定的，加密提款人信息
        :return:
        """
        _text = self.get_text(self.get_bind_name)
        return _text

    def verity_get_bind_time(self):
        """
        获取刚绑定的，绑定时间
        :return:
        """
        _text = self.get_text(self.get_bind_time)
        return _text

    def click_check_code_img(self):
        """
        点击验证码图标，刷新验证码
        :return:
        """
        self.click(self.btn_login_code_image)

    def verify_bind_bank_card_rule(self, suc, name, card, pwd):
        """
        绑定银行卡，已设置密保和资金密码，验证绑定银行卡相关字段的规则
        :param suc:
        :param name:
        :param card:
        :param pwd:
        :return:
        """
        try:
            self.type_input_update_password_1(name)
            self.type_input_update_password_3(card)
            self.type_input_update_password_5(pwd)
            if self.get_click_submit == False:
                self.forced_wait(2)
            else:
                self.click_submit()
            if suc == "0":
                _toast_text = self.get_text(self.toast_text)
                return _toast_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason: %s' % e)

    def verify_bind_bank_card_rule_1(self, suc, card, pwd):
        """
        绑定银行卡，已设置密保和资金密码，验证绑定银行卡相关字段的规则
        :param suc:
        :param name:
        :param card:
        :param pwd:
        :return:
        """
        try:
            #self.type_input_update_password_1(name)
            self.type_input_update_password_3(card)
            self.type_input_update_password_5(pwd)
            if self.get_click_submit == False:
                self.forced_wait(2)
            else:
                self.click_submit()
            if suc == "0":
                _toast_text = self.get_text(self.toast_text)
                return _toast_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason: %s' % e)

    def click_select_bind_bank_card(self):
        self.click(self.select_bind_bank_card)
        self.forced_wait(1)
        self.move_to_element(self.select_bind_bank_card_item)
        self.forced_wait(1)
        self.click(self.select_bind_bank_card_item)

    def click_select_bind_city(self):
        self.click(self.select_bind_city)
        self.forced_wait(1)
        self.move_to_element(self.select_bind_city_item)
        self.forced_wait(1)
        self.click(self.select_bind_city_item)

    def click_online_withdrawal(self):
        """
        线上取款
        :return:
        """
        self.click(self.link_online_withdrawal)

    def click_tab_withdrawal_bank_cards(self):
        """
        切换到绑定银行卡页面
        :return:
        """
        self.click(self.tab_withdrawal_bank_cards)

    def click_tab_withdrawal_request(self):
        """
        切换提款申请页面
        :return:
        """
        self.click(self.tab_withdrawal_request)

    def click_submit(self):
        """
        提交功能
        :return:
        """
        self.click(self.btn_submit)

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