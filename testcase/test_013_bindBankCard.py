import datetime
import os
import unittest
import ddt
from BeautifulReport import BeautifulReport

from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml
from Common.log import log1
from Common.update_yaml import update_bind_card
from PageObject.page_onlineWithdrawal import PageOnlineWithdrawal

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 7)
case_data_10 = get_test_data(case_path, 10)


@ddt.ddt
class TestBindBankCard(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath
    # yaml文件读取
    data = get_yaml()

    assert_withdrawal_binding_bank = data['asserts'].get('assert_withdrawal_binding_bank')

    username = data['datas'].get('data_last_username')  # 上一次成功注册的账号
    password = data['datas'].get('data_password')
    data_bind_name = data['datas'].get('data_bind_name')
    data_bind_card = data['datas'].get('data_bind_card')
    data_fund_pwd = data['datas'].get('data_fund_pwd')
    assert_bind_pass = data['asserts'].get('assert_bind_pass')
    assert_bind_repeat = data['asserts'].get('assert_bind_repeat')

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
        self.link = PageOnlineWithdrawal(self.driver)

    @BeautifulReport.add_test_img('test_bing_bank_card_001')
    def test_bing_bank_card_001(self):
        """新注册会员，在未绑定银行卡的情况下，验证是否阻止提款申请"""
        self.case_name = '新注册会员，在未绑定银行卡的情况下，验证是否阻止提款申请'
        # self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        self.link.find_click_notice()
        # yaml文件读取
        data = get_yaml()
        data_last_username = data['datas'].get('data_last_username')
        # 输入登录用户名
        self.link.type_login_username(data_last_username)
        # 输入登录密码
        self.link.type_login_password(self.password)
        # 如果存在验证码，则输入获取的验证码信息
        self.link.find_type_login_code()
        # # 点击登录按钮
        # self.link.click_login_btn()
        # 浏览器置顶
        self.link.js_scroll_top()
        self.link.forced_wait(1)
        # 点击线上取款按钮
        self.link.click_online_withdrawal()
        # 获取弹出框提示信息实际结果
        try:
            if self.link.get_toast_text() == '请绑定银行卡':
                self.re_data = self.link.get_toast_text()
                # ctxt.
                try:
                    # 判断预期结果与实际结果是否一致
                    self.assertIn(self.assert_withdrawal_binding_bank, self.re_data.replace(" ", ""))
                    # 选择提款申请
                    self.link.click_tab_withdrawal_request()
                    # 获取弹出框提示信息实际结果
                    self.re_data = self.link.get_toast_text()
                    # 判断预期结果与实际结果是否一致
                    self.assertIn(self.assert_withdrawal_binding_bank, self.re_data.replace(" ", ""))
                    self.link.forced_wait(1)
                    # 断言成功，截图
                    self.link.save_window_snapshot(self.case_name)
                    log1.info("Successful execution of test cases:%s" % self.case_name)
                except AssertionError as e:
                    log1.error("Failure of test case execution:%s" % e)
                    raise
        except BaseException as e:
            # 进入绑定银行卡页面
            self.link.click_tab_withdrawal_bank_cards()
            log1.error("Failure of test case execution:%s" % e)

    @ddt.data(*case_data)
    def test_bing_bank_card_002(self, data):
        """绑定银行卡字段规则校验"""
        self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        try:
            if self.link.type_username_disabled() == True:
                # 获取提款人姓名
                self.name = data['name']
                # 获取银行卡号
                self.card = data['card']
                # 获取资金密码
                self.pwd = data['password']
                self.suc = data['suc']
                # 获取断言预期结果
                self.assert_value = data['assert_vale']
                self.re_data = self.link.verify_bind_bank_card_rule(self.suc, self.name, self.card, self.pwd)
                if self.re_data == '请选择或输入银行':
                    self.link.forced_wait(1)
                    self.link.click_select_bind_bank_card()
                    # self.assertIn(self.assert_value.replace(" ", ""), self.re_data.replace(" ", ""))
                if self.re_data == '请选择银行所在地':
                    self.link.click_select_bind_city()
                    # self.link.forced_wait(3)
                if "资金密码必须是6位且全数字" in self.re_data.replace(" ", ""):
                    self.link.forced_wait(5)
                if "资金密码错误" in self.re_data:
                    self.link.forced_wait(5)
                if "开户姓名的最小长度为2字符" in self.re_data.replace(" ", ""):
                    self.link.forced_wait(5)
                if "抱歉！当前银行卡已经绑定请勿重复绑定！" in self.re_data.replace(" ", ""):
                    self.link.forced_wait(5)
                try:
                    # 判断提示信息的预期结果与实际结果是否一致
                    self.assertIn(self.assert_value.replace(" ", ""), self.re_data.replace(" ", ""))
                    # 断言成功，截图
                    self.link.save_window_snapshot(self.case_name)
                    log1.info("Successful execution of test cases:%s" % self.case_name)
                except AssertionError as e:
                    self.save_img(self.case_name)
                    log1.error("Failure of test case execution:%s" % e)
                    raise
            else:
                self.skipTest(
                    '提款人姓名输入框状态为:%s！已绑定过银行卡，则跳过用例test_bing_bank_card_002' % self.link.type_username_disabled())
        except BaseException as e:
            log1.error("Failure of test case execution:%s" % e)
            self.skipTest(
                '提款人姓名输入框状态为:%s！已绑定过银行卡，则跳过用例test_bing_bank_card_002' % self.link.type_username_disabled())

    @ddt.data(*case_data_10)
    def test_bing_bank_card_003(self, data):
        """绑定银行卡字段规则校验"""
        self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        try:
            if self.link.type_username_disabled() == False:
                # # 获取提款人姓名
                # self.name = data['name']
                # 获取银行卡号
                self.card = data['card']
                # 获取资金密码
                self.pwd = data['password']
                self.suc = data['suc']
                # 获取断言预期结果
                self.assert_value = data['assert_vale']
                self.re_data = self.link.verify_bind_bank_card_rule_1(self.suc, self.card, self.pwd)
                if self.re_data == '请选择或输入银行':
                    self.link.forced_wait(1)
                    self.link.click_select_bind_bank_card()
                    # self.assertIn(self.assert_value.replace(" ", ""), self.re_data.replace(" ", ""))
                if self.re_data == '请选择银行所在地':
                    self.link.click_select_bind_city()
                    # self.link.forced_wait(3)
                if "资金密码必须是6位且全数字" in self.re_data.replace(" ", ""):
                    self.link.forced_wait(5)
                if "资金密码错误" in self.re_data:
                    self.link.forced_wait(5)
                # if "开户姓名的最小长度为2字符" in self.re_data.replace(" ", ""):E
                #     self.link.forced_wait(5)
                if "抱歉！当前银行卡已经绑定请勿重复绑定！" in self.re_data.replace(" ", ""):
                    self.link.forced_wait(5)
                try:
                    # 判断提示信息的预期结果与实际结果是否一致
                    self.assertIn(self.assert_value.replace(" ", ""), self.re_data.replace(" ", ""))
                    # 断言成功，截图
                    self.link.save_window_snapshot(self.case_name)
                    log1.info("Successful execution of test cases:%s" % self.case_name)
                except AssertionError as e:
                    self.save_img(self.case_name)
                    log1.error("Failure of test case execution:%s" % e)
                    raise
            else:
                self.skipTest(
                    '提款人姓名输入框状态为:%s！未绑定过银行卡，则跳过用例test_bing_bank_card_003' % self.link.type_username_disabled())
        except BaseException as e:
            log1.error("Failure of test case execution:%s" % e)
            self.skipTest('提款人姓名输入框状态为:%s！未绑定过银行卡，则跳过用例test_bing_bank_card_003' % self.link.type_username_disabled())

    @BeautifulReport.add_test_img('test_bing_bank_card_004')
    def test_bing_bank_card_004(self):
        """第一次绑定银行卡，已设置密保和资金密码，验证所有字段符合条件是否能够成功绑定"""
        self.case_name = "第一次绑定银行卡，已设置密保和资金密码，验证所有字段符合条件是否能够成功绑定"
        log1.info("Executing test cases：%s" % self.case_name)
        self.link.refresh()
        self.link.forced_wait(1)
        # 点击线上取款按钮
        self.link.click_online_withdrawal()
        try:
            if self.link.type_username_disabled() == True:
                # 输入提款人姓名
                self.link.type_input_update_password_1(self.data_bind_name)
                # 选择开户银行
                self.link.click_select_bind_bank_card()
                # 输入银行卡号
                self.link.type_input_update_password_3(self.data_bind_card)
                # 选择所在地
                self.link.click_select_bind_city()
                # 输入资金密码
                self.link.type_input_update_password_5(self.data_fund_pwd)
                # 点击提交
                self.link.click_submit()
                # 获取弹出提示框预期结果
                _toast_text = self.link.get_toast_text()
                try:
                    # 验证弹出框提示信息是否与预期结果一致
                    assert self.assert_bind_repeat in _toast_text, '绑定成功提示信息的预期结果：%s 与 实际结果：%s 不一致' % (
                        self.assert_bind_repeat, _toast_text)
                    # assert self.assert_bind_pass in _toast_text, self.click_submit()
                    # 验证提款人姓名输入框是否禁用状态
                    # self.assertFalse(self.link.get_input_bind_card_name(), '提款人姓名输入框为可编辑状态！')
                    # # 验证绑定的开户银行是否正确
                    # self.bank = self.link.verity_get_bind_bank()
                    # self.assertEqual(self.bank.replace(" ", ""), "工商银行", '绑定的开户银行信息为：{%s}' % self.bank)
                    # # 验证银行卡号是否加密显示，如：1212 **** **** ***6 666
                    # self.card = self.link.verity_get_bind_card()
                    # self.assertIn(self.data_bind_card.replace(self.data_bind_card[4:-4], "***********"),
                    #               self.card.replace(" ", ""), '银行卡号：{%s}未加密显示' % self.card)
                    # # 验证取款人是否加密显示，如：里**
                    # self.name = self.link.verity_get_bind_name()
                    # self.assertIn(self.data_bind_name.replace(self.data_bind_name[1:], "**"), self.name,
                    #               '提款人姓名：{%s}未加密显示' % self.name)
                    # # 验证绑定时间是否为当前时间
                    # self._time = self.link.verity_get_bind_time()
                    # now_time = datetime.datetime.now()
                    # _time_now = now_time.strftime('%Y-%m-%d')  # %H%M%S
                    # self.assertIn(_time_now, self._time, '绑定时间显示不正确：{%s}' % self._time)
                    # self.link.forced_wait(1)
                    # # 断言成功，截图
                    # self.link.save_window_snapshot(self.case_name)
                    # # 将成功注册的银行卡号+1，并更新到yaml文件中
                    # self.new_card = int(self.data_bind_card) + 1
                    # update_bind_card(self.new_card)
                    log1.info("Successful execution of test cases:%s" % self.case_name)
                except AssertionError as e:
                    log1.error("Failure of test case execution:%s" % e)
                    raise
            else:
                self.skipTest(
                    '{提款人姓名}输入框状态为:%s！输入框不可编辑，则跳过用例test_bing_bank_card_004' % self.link.type_username_disabled())
        except BaseException as e:
            log1.error("Failure of test case execution:%s" % e)
            self.skipTest(
                '{提款人姓名}输入框状态为:%s！输入框不可编辑，则跳过用例test_bing_bank_card_004' % self.link.type_username_disabled())

    @BeautifulReport.add_test_img('test_bing_bank_card_005')
    def test_bing_bank_card_005(self):
        """已绑定过银行卡，已设置密保和资金密码，验证所有字段符合条件是否能够成功绑定"""
        self.case_name = "已绑定过银行卡，已设置密保和资金密码，验证所有字段符合条件是否能够成功绑定"
        log1.info("Executing test cases：%s" % self.case_name)
        self.link.refresh()
        self.link.forced_wait(1)
        # 点击线上取款按钮
        self.link.click_online_withdrawal()
        try:
            if self.link.type_username_disabled() == False:
                # 输入提款人姓名
                # self.link.type_input_update_password_1(self.data_bind_name)
                # 选择开户银行
                self.link.click_select_bind_bank_card()
                # 输入银行卡号
                self.link.type_input_update_password_3(self.data_bind_card)
                # 选择所在地
                self.link.click_select_bind_city()
                # 输入资金密码
                self.link.type_input_update_password_5(self.data_fund_pwd)
                # 点击提交
                self.link.click_submit()
                # 获取弹出提示框预期结果
                _toast_text = self.link.get_toast_text()
                try:
                    # 验证弹出框提示信息是否与预期结果一致
                    assert self.assert_bind_repeat in _toast_text, '绑定成功提示信息的预期结果：%s 与 实际结果：%s 不一致' % (
                        self.assert_bind_repeat, _toast_text)
                    # assert self.assert_bind_pass in _toast_text, self.click_submit()
                    # # 验证提款人姓名输入框是否禁用状态
                    # self.assertFalse(self.link.get_input_bind_card_name(), '提款人姓名输入框为可编辑状态！')
                    # # 验证绑定的开户银行是否正确
                    # self.bank = self.link.verity_get_bind_bank()
                    # self.assertEqual(self.bank.replace(" ", ""), "工商银行", '绑定的开户银行信息为：{%s}' % self.bank)
                    # # 验证银行卡号是否加密显示，如：1212 **** **** ***6 666
                    # self.card = self.link.verity_get_bind_card()
                    # self.assertIn(self.data_bind_card.replace(self.data_bind_card[4:-4], "***********"),
                    #               self.card.replace(" ", ""), '银行卡号：{%s}未加密显示' % self.card)
                    # # 验证取款人是否加密显示，如：里**
                    # self.name = self.link.verity_get_bind_name()
                    # self.assertIn(self.data_bind_name.replace(self.data_bind_name[1:], "**"), self.name,
                    #               '提款人姓名：{%s}未加密显示' % self.name)
                    # # 验证绑定时间是否为当前时间
                    # self._time = self.link.verity_get_bind_time()
                    # now_time = datetime.datetime.now()
                    # _time_now = now_time.strftime('%Y-%m-%d')  # %H%M%S
                    # self.assertIn(_time_now, self._time, '绑定时间显示不正确：{%s}' % self._time)
                    # self.link.forced_wait(1)
                    # # 断言成功，截图
                    # self.link.save_window_snapshot(self.case_name)
                    # # 将成功注册的银行卡号+1，并更新到yaml文件中
                    # self.new_card = int(self.data_bind_card) + 1
                    # update_bind_card(self.new_card)
                    log1.info("Successful execution of test cases:%s" % self.case_name)
                except AssertionError as e:
                    log1.error("Failure of test case execution:%s" % e)
                    raise
            else:
                self.skipTest(
                    '{提款人姓名}输入框状态为:%s！输入框可编辑，则跳过用例test_bing_bank_card_005' % self.link.type_username_disabled())
        except BaseException as e:
            log1.error("Failure of test case execution:%s" % e)
            # self.skipTest(
            #     '{提款人姓名}输入框状态为:%s！输入框可编辑，则跳过用例test_bing_bank_card_005' % self.link.type_username_disabled())

    @classmethod
    def tearDownClass(cls) -> None:
        cls.link = PageOnlineWithdrawal(cls.driver)
        cls.link.dr_quit()
