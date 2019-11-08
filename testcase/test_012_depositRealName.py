import os
import unittest
from functools import wraps

import ddt
import yaml
from BeautifulReport import BeautifulReport

from Common import parallel
from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml
from Common.log import log1
from Common.update_yaml import update_deposit_channel_1
from PageObject.page_onlineDeposit import PageOnlineDeposit

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 6)



@ddt.ddt
class TestOnlineDepositBank(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath
    # 获取yaml文件内容
    data = get_yaml()
    assert_amount_err = data['asserts'].get('assert_deposit_amount_err')  # 存款金额断言-请输入正确存款金额
    assert_amount_min = data['asserts'].get('assert_deposit_amount_min')  # 存款金额断言-存款金额不能低于10元
    assert_deposit_zfb_min = data['asserts'].get('assert_deposit_zfb_min')  # 支付宝存款金额断言-金额低于通道最低金额%s
    assert_bank = data['asserts'].get('assert_deposit_bank')  # 请选择汇入银行
    suc = data['datas'].get('data_suc')  #
    username = data['datas'].get('data_last_username')  # 上一次成功注册的账号
    password = data['datas'].get('data_password')
    data_amount_err = data['datas'].get('data_amount_err')
    data_dep_channel_1 = data['datas'].get('data_dep_channel_1')
    data_zfbh5_min_amount = data['datas'].get('data_zfbh5_min_amount')  # 支付宝支付范围的最小值
    data_zfbh5_max_amount = data['datas'].get('data_zfbh5_max_amount')  # 支付宝支付范围的最大值
    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')

    def save_img(self, img_name):
        """
            传入一个img_name, 并存储到默认的文件路径下
        :param img_name:
        :return:
        """
        self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))

    @classmethod
    def setUpClass(cls):
        browser = BasePage(cls)
        cls.driver = browser.open_browser()

    def setUp(self):
        self.link = PageOnlineDeposit(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.link = PageOnlineDeposit(cls.driver)
        cls.link.dr_quit()

    @BeautifulReport.add_test_img('test_online_deposit_bank_001')
    def test_online_deposit_bank_001(self):
        """在网银转账充值页面，验证[汇入银行]字段是否不能为空"""
        self.case_name = "在网银转账充值页面，验证汇入银行字段是否不能为空"
        log1.info("Executing test cases：%s" %  self.case_name)
        log1.info('input data:username:%s,password:%s' % (self.username, self.password))
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
        # 浏览器置顶
        self.link.js_scroll_top()
        # 强制等待
        self.link.forced_wait(1)
        # 访问线上存款
        self.link.visit_online_deposit()
        # 访问网银转账
        self.link.find_tab_deposit_bank()
        # 点击提交按钮
        self.link.click_submit()
        # 获取提示信息
        self._text = self.link.get_toast_text()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._text, self.assert_bank,self.output_verify_fail % (self.assert_bank, self._text.replace(" ", "")))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_bank, self._text.replace(" ", "")))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 选择银行
            self.link.click_select_bank()
            self.link.click_select_bank_item()
            log1.info("Successful execution of test cases：%s" %  self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @ddt.data(*case_data)
    def test_online_deposit_bank_002(self, data):
        # """在网银转账充值页面，验证不符合规则的[存款金额]字段是否能被阻止提交"""
        # case_name = "在网银转账充值页面，验证[存款金额]字段是否不能为空"
        self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        self.dep_amount = data['amount']
        self.dep_name = data['name']
        self.dep_time = data['time']
        self.suc = data['suc']
        self.dep_assert = data['assert_vale']
        log1.info('input data:suc:%s,amount:%s,name:%s,time:%s,assert:%s' % (self.suc, self.dep_amount, self.dep_name, self.dep_time, self.dep_assert))
        self.re_data = self.link.verify_deposit_bank_amount_err(self.suc, self.dep_amount, self.dep_name,
                                                                        self.dep_time)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.dep_assert,self.output_verify_fail % (self.dep_assert, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.dep_assert, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)

            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise
