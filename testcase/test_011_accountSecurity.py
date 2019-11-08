import os
import unittest

import ddt
from BeautifulReport import BeautifulReport

from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml
from Common.log import log1
from PageObject.page_updatePassword import PageUpdatePassword

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 2)
case_data_3 = get_test_data(case_path, 3)
case_data_5 = get_test_data(case_path, 5)

#yaml文件内容读取
data = get_yaml()
assert_set_fund_password = data['asserts'].get('assert_set_fund_password')


@ddt.ddt
class TestAccountSecurity(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath
    # yaml文件读取
    data = get_yaml()
    username = data['datas'].get('data_last_username')  # 上一次成功注册的账号
    password = data['datas'].get('data_password')  # 登录密码
    data_answer = data['datas'].get('data_answer')  # 密保答案
    data_error_answer = data['datas'].get('data_error_answer')  # 错误密保答案
    data_len_answer = data['datas'].get('data_len_answer')  # 密保答案长度小于2
    data_new_answer = data['datas'].get('data_new_answer')  # 新密保答案

    assert_security_problem = data['asserts'].get('assert_security_problem')  # 请选择密保问题断言
    assert_security_answer = data['asserts'].get('assert_security_answer')  # 请输入密保答案断言
    assert_security_new_answer = data['asserts'].get('assert_security_new_answer')  # 请输入新密保答案断言
    assert_security_set = data['asserts'].get('assert_security_set')  # 设置资金密码成功
    assert_security_agreement = data['asserts'].get('assert_security_agreement')  # 新密保不能与原密保一致
    assert_security_error = data['asserts'].get('assert_security_error')  # 原密保问题或答案错误
    assert_security_update = data['asserts'].get('assert_security_update')  # 修改密保成功
    assert_security_len = data['asserts'].get('assert_security_len')  # 密保答案 的最小长度为 2 字符

    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')

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
        self.link = PageUpdatePassword(self.driver)

    @BeautifulReport.add_test_img('test_account_security_001')
    def test_account_security_001(self):
        """验证是否能够成功访问账号安全页面"""
        self.case_name = '验证是否能够成功访问账号安全页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        self.link.find_click_notice()
        # yaml文件读取
        data = get_yaml()
        data_last_username = data['datas'].get('data_last_username')
        # 输入登录用户名
        self.link.type_username(data_last_username)
        # 输入登录密码
        self.link.type_password(self.password)
        # 如果存在验证码，则输入获取的验证码信息
        self.link.find_type_login_code()
        # 浏览器置顶
        self.link.js_scroll_top()
        # 获取登录账号信息
        self.re_data = self.link.get_username_text()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertIn(data_last_username,self.re_data.replace(" ", ""),
                             self.output_verify_fail % (data_last_username, self.re_data.replace(" ", "")))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (data_last_username, self.re_data.replace(" ", "")))
            # 强制等待
            self.link.forced_wait(1)
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # # 访问会员中心
            # self.link.visit_member_centre_page()
            # # 访问账号安全
            self.link.visit_account_security_page()
            #self.link.click_fund_password_tab()
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution:%s" % e + '\n')
            raise

    @ddt.data(*case_data)
    def test_account_security_002(self, data):
        """
        修改登录密码测试用力
        :param data: old_pwd,new_pwd,confirm_pwd
        :return:
        """
        self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        self.suc = data['suc']
        self.old_pwd = data['old_pwd']
        self.new_pwd = data['new_pwd']
        self.confirm_pwd = data['confirm_pwd']
        self.assert_value = data['assert_vale']
        log1.info('input suc:%s,old_pwd:%s,new_pwd:%s,confirm_pwd:%s,assert_value:%s' % (
            self.suc, self.old_pwd, self.new_pwd, self.confirm_pwd, self.assert_value))
        self.re_data = self.link.submit_update_password(self.suc, self.old_pwd, self.new_pwd, self.confirm_pwd)
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_value.replace(" ", ""), self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_value.replace(" ", ""), self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_value.replace(" ", ""), self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @unittest.skipIf(assert_set_fund_password != '设置资金密码','已设置过资金密码，跳过用例test_account_security_003')
    @ddt.data(*case_data_3)
    def test_account_security_003(self, data):
        """
        setting up fund password test cases
        :param data: old_pwd,new_pwd,confirm_pwd
        :return:
        """
        self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        self.suc = data['suc']
        self.fund_pwd = data['fund_pwd']
        self.confirm_pwd = data['confirm_pwd']
        self.assert_value = data['assert_vale']
        log1.info('input suc:%s,fund_pwd:%s,confirm_pwd:%s,assert_value:%s' % (
            self.suc, self.fund_pwd, self.confirm_pwd,self.assert_value))
        self.re_data = self.link.submit_set_fund_password(self.suc, self.fund_pwd, self.confirm_pwd)
        try:
            self.assertIn(self.assert_value.replace(" ", ""),self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                                 self.assert_value.replace(" ", ""), self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
                self.assert_value.replace(" ", ""), self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_004')
    @unittest.skipIf(assert_set_fund_password != '设置资金密码','已设置过资金密码，跳过用例test_account_security_004')
    def test_account_security_004(self):
        """验证密保答案是否不能为空"""
        self.case_name = "验证密保答案是否不能为空"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.click_select_security()
        self.link.forced_wait(3)
        self.link.click_select_security_item()
        self.link.forced_wait(3)
       # self.link.click_select_security_problem()
        self.link.click_submit()
        # self.link.forced_wait(3)
        self.re_data = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_answer,self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_answer, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_answer, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_005')
    @unittest.skipIf(assert_set_fund_password != '设置资金密码','已设置过资金密码，跳过用例test_account_security_005')
    def test_account_security_005(self):
        """验证是否能够成功设置资金密码"""
        self.case_name = "验证是否能够成功设置资金密码"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.type_security_password_4(self.data_answer)
        self.link.click_submit()
        self.re_data = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_set,self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_set, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_set, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @ddt.data(*case_data_5)
    def test_account_security_006(self, data):
        """
        Modify up fund password test cases
        :param data:
        :return:
        """
        self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        self.suc = data['suc']
        self.old_pwd = data['old_pwd']
        self.new_pwd = data['new_pwd']
        self.confirm_pwd = data['confirm_pwd']
        self.security = data['security']
        self.assert_value = data['assert_vale']
        log1.info('input suc:%s,old_pwd:%s,new_pwd:%s,confirm_pwd:%s,security:%s,assert_value:%s' % (
            self.suc, self.old_pwd, self.new_pwd, self.confirm_pwd, self.security, self.assert_value))
        self.re_data = self.link.submit_update_fund_password(self.suc, self.old_pwd, self.new_pwd, self.confirm_pwd,
                                                             self.security)
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn( self.assert_value,self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_value, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(
                self.output_verify_success % (self.assert_value, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_007')
    def test_account_security_007(self):
        """修改密保页面，验证密保答案是否不能为空"""
        self.case_name = "修改密保页面，验证密保答案是否不能为空"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.click_security_password_tab()
        self.link.click_submit()
        self.toast_text = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_answer,self.toast_text.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_answer, self.toast_text.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_answer, self.toast_text.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_008')
    def test_account_security_008(self):
        """修改密保页面，验证新密保问题是否不能为空"""
        self.case_name = "修改密保页面，验证新密保问题是否不能为空"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.type_security_password_2(self.data_answer)
        self.link.click_submit()
        self.toast_text = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_problem,self.toast_text.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_problem, self.toast_text.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_problem, self.toast_text.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_009')
    def test_account_security_009(self):
        """修改密保页面，验证新密保答案是否不能为空"""
        self.case_name = "修改密保页面，验证新密保答案是否不能为空"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.click_select_security()
        self.link.forced_wait(3)
        self.link.click_select_security_item()
        self.link.forced_wait(3)
        self.link.click_submit()
        self.link.forced_wait(3)
        self.toast_text = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_new_answer,self.toast_text.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_new_answer, self.toast_text.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_new_answer, self.toast_text.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_010')
    def test_account_security_010(self):
        """修改密保页面，验证新密保是否不能与原密保一致"""
        self.case_name = "修改密保页面，验证新密保是否不能与原密保一致"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.type_security_password_4(self.data_answer)
        self.link.click_submit()
        self.re_data = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_agreement,self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_agreement, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_agreement, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_011')
    def test_account_security_011(self):
        """修改密保页面，验证原密保问题或答案错误是否能阻止修改密保"""
        self.case_name = "修改密保页面，验证原密保问题或答案错误是否能阻止修改密保"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.type_security_password_2(self.data_error_answer)
        self.link.type_security_password_4(self.data_new_answer)
        self.link.click_submit()
        self.re_data = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_error,self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_error, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_error, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_012')
    def test_account_security_012(self):
        """修改密保页面，验证密保答案是否不能少于2个字符"""
        self.case_name = "修改密保页面，验证密保答案是否不能少于2个字符"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.type_security_password_2(self.data_len_answer)
        self.link.type_security_password_4(self.data_new_answer)
        self.link.click_submit()
        self.re_data = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_len.replace(" ", ""),self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_len.replace(" ", ""), self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_len.replace(" ", ""), self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_013')
    def test_account_security_013(self):
        """修改密保页面，验证是否能够成功修改密保-01"""
        self.case_name = "修改密保页面，验证是否能够成功修改密保-01"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.type_security_password_2(self.data_answer)
        self.link.type_security_password_4(self.data_new_answer)
        self.link.click_submit()
        self.re_data = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_update,self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_update, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_update, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_account_security_014')
    def test_account_security_014(self):
        """修改密保页面，验证是否能够成功修改密保-02"""
        self.case_name = "修改密保页面，验证是否能够成功修改密保-02"
        log1.info("Executing test case: %s" % self.case_name)
        self.link.type_security_password_2(self.data_new_answer)
        # 选择密保问题
        self.link.click_select_security()
        self.link.forced_wait(2)
        self.link.click_select_security_item()
        self.link.forced_wait(2)
        # 输入密保答案
        self.link.type_security_password_4(self.data_answer)
        # 点击提交按钮
        self.link.click_submit()
        # 获取弹出提示框信息
        self.re_data = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否正确
            self.assertIn(self.assert_security_update,self.re_data.replace(" ", "").split("\n确认")[0],
                             self.output_verify_fail % (
                             self.assert_security_update, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (
            self.assert_security_update, self.re_data.replace(" ", "").split("\n确认")[0]))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            self.link.forced_wait(2)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test cases execution：%s" % e + '\n')
            raise

    @classmethod
    def tearDownClass(cls) -> None:
        cls.link = PageUpdatePassword(cls.driver)
        cls.link.dr_quit()
