import datetime
import os
import re
import urllib.request

from aip import AipOcr
from selenium.webdriver.common.by import By

from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1

# path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
#                     'yamls', 'page_data_002.yaml')
# test_data_file = os.path.abspath(path)
# file = open(test_data_file, 'r', encoding='utf-8')
# data = yaml.load(file, Loader=yaml.FullLoader)
# assert_bank = data['onlineDeposit'].get('assert_bank')
from Common.update_yaml import update_deposit_channel_1, update_zfbh5_amount, update_deposit_channel_2

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')


class PageOnlineDeposit(BasePage):
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
    link_online_deposit = data['links'].get('link_online_deposit')  # 线上存款
    toast_text = data['pop_box'].get('pop_toast_text')  # 弹出即消失的提示框
    btn_submit = data['buttons'].get('btn_submitPay')  # 账号安全确认提交元素定位
    select_bank = data['buttons'].get('select_bank')  # 汇款银行下拉框
    select_bank_item = data['buttons'].get('select_bank_item')  # 汇款银行下拉框内容
    input_deposit_amount = data['inputs'].get('input_deposit_amount')  # 网银存款-存款金额
    input_deposit_name = data['inputs'].get('input_deposit_name')  # 网银存款-存款姓名
    input_deposit_time = data['inputs'].get('input_deposit_time')  # 网银存款-存款时间
    input_deposit_binding_name = data['inputs'].get('input_deposit_binding_name')  # 绑定姓名弹出框的输入框
    input_zfb_h5 = data['inputs'].get('input_zfb_h5')  # 支付宝输入框
    btn_clear_time = data['buttons'].get('btn_clear_time')  # 清除已输入的时间
    pop_deposit_binding_name = data['pop_box'].get('pop_deposit_binding_name')  # 绑定姓名弹出框的提示信息
    pop_deposit_binding_cancel = data['pop_box'].get('pop_deposit_binding_cancel')  # 绑定姓名的取消按钮
    tab_deposit_bank = data['tabs'].get('tab_deposit_bank')  # 网银转账存款方式
    tab_deposit_zfb = data['tabs'].get('tab_deposit_zfb')  # 支付宝存款方式
    tab_deposit_zfb_1 = data['tabs'].get('tab_deposit_zfb_1')  # 支付宝-通道1
    tab_deposit_zfb_2 = data['tabs'].get('tab_deposit_zfb_2')  # 支付宝-通道2
    input_login_code = data['inputs'].get('input_login_code')  # 判断验证码输入框是否可见

    select_zfb = data['buttons'].get('select_zfb')  # 支付宝下拉框
    select_zfb_item = data['buttons'].get('select_zfb_item')  # 支付宝下拉框的内容


    pop_deposit_zfbh5_text = data['pop_box'].get('pop_deposit_zfbh5_text')  # 支付宝H5符合条件的弹出提示框信息
    pop_deposit_zfbh5_close = data['pop_box'].get('pop_deposit_zfbh5_close')  # 支付宝H5符合条件的弹出提示框关闭按钮
    pop_deposit_zfbh5_pay = data['pop_box'].get('pop_deposit_zfbh5_pay')  # 支付宝H5符合条件的弹出提示框支付按钮

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    # def find_code(self):
    #     notice_element = self.find_element(self.input_login_code)
    #     if self.get_displayed(notice_element):
    #         self.click(self.pop_web_notice_close)
    #     else:
    #         pass

    def find_tab_deposit_bank(self):
        """
        判断是否存在网银转账充值方式
        :return:
        """
        if self.get_displayed(self.tab_deposit_bank):
            self.click(self.tab_deposit_bank)
        else:
            pass

    def find_tab_deposit_zfb(self):
        """
        判断是否存在支付宝充值方式
        :return:
        """
        if self.get_displayed(self.tab_deposit_zfb):
            self.click(self.tab_deposit_zfb)
        else:
            pass

    def find_zfb_input(self):
        """
        在支付宝充值页面，获取支付范围，并存储到yaml文件中
        :return:
        """
        try:
            notice_element = self.find_element(self.input_zfb_h5)
            if self.get_displayed(self.input_zfb_h5):
                # self.click(self.input_zfb_h5)
                value_text = notice_element.get_attribute('placeholder')
                cost = re.findall('\d+', value_text)
                if cost[0] < cost[1]:
                    min_amount = cost[0]
                    max__amount = cost[1]
                    #print("True，min:%s,max:%s" % (min_amount, max__amount))
                    update_zfbh5_amount(min_amount, max__amount)
                    return min_amount, max__amount
                else:
                    max__amount = cost[0]
                    min_amount = cost[1]
                    #print("False，min:%s,max:%s" % (min_amount, max__amount))
                    update_zfbh5_amount(min_amount, max__amount)
                    return min_amount, max__amount
            else:
                pass
        except BaseException as e:
            log1.error('定位支付宝输入框元素失败，原因：该域不存在输入框元素-%s' % e)

    def find_channel_1(self):
        """
        在充值页面，查找是否存在支付宝的充值通道-1
        :return:
        """
        try:
            self.find_tab_deposit_zfb()
            actives = self.driver.find_element_by_class_name('content')
            spans = actives.find_elements_by_tag_name("span")
            for span_text in spans:
                # log1.info("_text:%s" % _text)
                if span_text.text.replace(" ", "") == '充值通道1':
                    _text = span_text.text
                    update_deposit_channel_1(_text)
                    return _text
        except BaseException as e:
            log1.error("定位元素失败，原因：不存在充值通道1-%s" % e + '\n')

    def find_channel_2(self):
        """
        在充值页面，查找是否存在支付宝的充值通道-1
        :return:
        """
        try:
            self.find_tab_deposit_zfb()
            actives = self.driver.find_element_by_class_name('content')
            spans = actives.find_elements_by_tag_name("span")
            for span_text in spans:
                # log1.info("_text:%s" % _text)
                if span_text.text.replace(" ", "") == '充值通道2':
                    _text = span_text.text
                    update_deposit_channel_2(_text)
                    return _text
        except BaseException as e:
            log1.error("定位元素失败，原因：不存在充值通道2-%s" % e + '\n')

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

    def verify_deposit_bank_amount_err(self, suc, amount, dep_name, dep_time):
        """
        验证网银存款-存款金额字段的规则
        :param suc:
        :return:
        """
        try:
            self.type_deposit_amount(amount)
            self.type_deposit_name(dep_name)
            self.click_clear_time()
            self.type_deposit_time(dep_time)
            self.click_submit()

            if suc == "0":
                _toast_text = self.get_text(self.toast_text)
                return _toast_text
            if suc == "1":
                self.forced_wait(1)
                #rename_text = self.driver.find_element(By.XPATH, "//span[contains(.,'请务必填写真实姓名，一旦绑定将无法修改姓名')]").text
                rename_text = self.get_text(self.pop_deposit_binding_name)
                return rename_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason: %s' % e)

    def verify_deposit_zfbh5_amount(self, suc, amount):
        """
        支付宝，H5模式，带输入框的支付测试方法
        :param suc:
        :param amount:
        :return:
        """
        try:
            notice_element = self.find_element(self.input_zfb_h5)
            if self.get_displayed(notice_element):
                try:
                    #self.find_zfb_input()
                    self.type_deposit_zfbh5_amount(amount)
                    if self.driver.find_element_by_css_selector('.submitPay').is_enabled() == True:
                        self.click_submit()
                    if suc == "0":
                        _toast_text = self.get_text(self.toast_text)
                        return _toast_text
                    if suc == "1":
                        _pay_text = self.get_text(self.pop_deposit_zfbh5_text)
                        return _pay_text
                except BaseException as e:
                    log1.error('Failure of test case execution! Reason: %s' % e)
            # select_element = self.find_element(self.select_deposit_zfb)
            # if self.get_displayed(select_element):
            #     try:
            #         self.select_deposit_zfb()
            #         self.select_deposit_zfb_item()
            #         self.click_submit()
            #         if suc == "1":
            #             _pay_text = self.get_text(self.pop_deposit_zfbh5_text)
            #             return _pay_text
            #     except BaseException as e:
            #         log1.error('Failure of test case execution! Reason: %s' % e)
            # elif self.get_displayed(notice_element):
            #     try:
            #         #self.find_zfb_input()
            #         self.type_deposit_zfbh5_amount(amount)
            #         self.click_submit()
            #         if suc == "0":
            #             _toast_text = self.get_text(self.toast_text)
            #             return _toast_text
            #         if suc == "1":
            #             _pay_text = self.get_text(self.pop_deposit_zfbh5_text)
            #             return _pay_text
            #     except BaseException as e:
            #         log1.error('Failure of test case execution! Reason: %s' % e)
        except BaseException as e:
            log1.error('定位元素失败，原因：该域不存在输入框元素-%s' % e)

    def verify_deposit_zfbh5_select(self, suc, amount):
        """
        支付宝，H5模式，带输入框的支付测试方法
        :param suc:
        :param amount:
        :return:
        """
        try:
            if self.get_displayed(self.select_deposit_zfb):
                try:
                    self.select_deposit_zfb()
                    self.select_deposit_zfb_item()
                    self.click_submit()
                    if suc == "1":
                        _pay_text = self.get_text(self.pop_deposit_zfbh5_text)
                        return _pay_text
                except BaseException as e:
                    log1.error('Failure of test case execution! Reason: %s' % e)
        except BaseException as e:
            log1.error('定位元素失败，原因：该域不存在输入框元素-%s' % e)

    def select_deposit_zfb(self):
        self.click(self.select_zfb)

    def select_deposit_zfb_item(self):
        self.move_to_element(self.select_zfb_item)
        self.click(self.select_zfb_item)

    def visit_online_deposit(self):
        """
        线上存款
        :return:
        """
        self.click(self.link_online_deposit)

    def click_tab_deposit_zfb_1(self):
        """
        切换到支付宝通道-1
        :return:
        """
        self.click(self.tab_deposit_zfb_1)

    def click_tab_deposit_zfb_2(self):
        """
        切换到支付宝通道-2
        :return:
        """
        self.click(self.tab_deposit_zfb_2)

    def click_pop_deposit_zfbh5_close(self):
        """
        支付宝，是否继续支付弹出框的关闭方法
        :return:
        """
        self.click(self.pop_deposit_zfbh5_close)

    def click_pop_deposit_zfbh5_pay(self):
        """
        支付宝，是否继续支付弹出框的支付方法
        :return:
        """
        self.click(self.pop_deposit_zfbh5_pay)

    def type_deposit_zfbh5_amount(self, amount):
        """
        在支付宝存款金额字段输入内容
        :param amount: amount
        :return:
        """
        self.type(self.input_zfb_h5, amount)

    def type_deposit_amount(self, amount):
        """
        在汇款金额字段输入内容
        :param amount: amount
        :return:
        """
        self.type_send(self.input_deposit_amount, amount)

    def type_deposit_name(self, name):
        """
        在汇款姓名字段输入内容
        :param name: name
        :return:
        """
        self.type_send(self.input_deposit_name, name)

    def type_deposit_time(self, _time):
        """
        在汇款时间字段输入内容
        :param _time:
        :return: _time
        """
        self.type(self.input_deposit_time, _time)

    def type_login_code(self, code):
        """
        验证码输入框
        :param code:
        :return:
        """
        self.type(self.input_login_code, code)

    def click_clear_time(self):
        """
        清除时间输入框内容，再输入时间
        :return:
        """
        self.click(self.input_deposit_time)
        self.move_to_element(self.btn_clear_time)
        self.click(self.btn_clear_time)

    def click_binding_name_cancel(self):
        """
        绑定姓名取消按钮
        :return:
        """
        self.click(self.pop_deposit_binding_cancel)

    def click_select_bank(self):
        """
        点击下拉框
        :return:
        """
        self.click(self.select_bank)

    def click_select_bank_item(self):
        """
        选择下拉框的内容
        :return:
        """
        self.move_to_element(self.select_bank_item)
        self.click(self.select_bank_item)

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

    def click_submit(self):
        """
        提交功能
        :return:
        """
        self.click(self.btn_submit)

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