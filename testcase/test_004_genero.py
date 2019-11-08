# -*- coding: UTF-8 -*-
import os
import unittest

import ddt

from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml

from Common.log import log1
from BeautifulReport import BeautifulReport

from PageObject.page_genero import GeneroPage

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 9)



@ddt.ddt
class TestGenero(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath

    data = get_yaml()
    assert_login_first = data['asserts'].get('assert_login_first')
    assert_public_interest_title = data['asserts'].get('assert_public_interest_title')  # 免息借呗页面title
    assert_public_video_genero = data['asserts'].get('assert_public_video_genero')  # 金管家页面title
    assert_public_lottery_genero = data['asserts'].get('assert_public_lottery_genero')
    assert_public_app_title = data['asserts'].get('assert_public_app_title')  # app下载页面title
    assert_public_home_title = data['asserts'].get('assert_public_home_title')  # 首页title
    assert_public_account_title = data['asserts'].get('assert_public_account_title')  # 账号交易
    assert_public_customer_en = data['asserts'].get('assert_public_customer_en')
    assert_public_customer_cn = data['asserts'].get('assert_public_customer_cn')
    assert_public_en_title = data['asserts'].get('assert_public_en_title')
    assert_public_email_title = data['asserts'].get('assert_public_email_title')  # 在线客服-投诉邮箱账号
    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')
    data_suc = data['datas'].get('data_suc')
    data_last_username = data['datas'].get('data_last_username')

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
        self.link = GeneroPage(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.link = GeneroPage(cls.driver)
        cls.link.dr_quit()

    @BeautifulReport.add_test_img('test_genero_001')
    def test_genero_001(self):
        """未登录情况下，访问金管家页面"""
        self.case_name = '未登录情况下，访问金管家页面'
        log1.info("Executing use test case：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        self.link.find_click_notice()
        # 访问金管家页面，并且获取新打开窗口的句柄
        self.link.visit_genero_page()
        # 获取当前句柄的title
        _title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(_title, self.assert_public_lottery_genero,
                             self.output_verify_fail % (self.assert_public_lottery_genero, _title))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_lottery_genero, _title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_genero_002')
    def test_genero_002(self):
        """未登录情况下，在金管家页面访问免息借呗页面"""
        self.case_name = '未登录情况下，在金管家页面访问免息借呗页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在金管家页面访问免息借呗页面，并且获取新打开窗口的句柄
        self.link.visit_genero_interest_page()
        # 获取当前句柄的title
        _title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(_title, self.assert_public_interest_title,
                             self.output_verify_fail % (self.assert_public_interest_title, _title))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_interest_title, _title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭浏览器窗口
            self.link.close_browser()
            # 切换窗口
            self.link.switch_to_window_by_title(self.assert_public_video_genero)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭浏览器窗口
            self.link.close_browser()
            # 切换窗口
            self.link.switch_to_window_by_title(self.assert_public_video_genero)
            raise

    @BeautifulReport.add_test_img('test_genero_003')
    def test_genero_003(self):
        """未登录情况下，在金管家页面访问APP下载页面"""
        self.case_name = '未登录情况下，在金管家页面访问APP下载页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在金管家页面访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_genero_app_page()
        # 获取当前句柄的title
        _title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(_title, self.assert_public_app_title,
                             self.output_verify_fail % (self.assert_public_app_title, _title))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_app_title, _title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭浏览器窗口
            self.link.close_browser()
            # 切换窗口
            self.link.switch_to_window_by_title(self.assert_public_video_genero)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭浏览器窗口
            self.link.close_browser()
            # 切换窗口
            self.link.switch_to_window_by_title(self.assert_public_video_genero)
            raise

    @BeautifulReport.add_test_img('test_genero_004')
    def test_genero_004(self):
        """未登录情况下，在金管家页面访问在线客服页面"""
        self.case_name = '未登录情况下，在金管家页面访问在线客服页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在金管家页面访问在线客服页面，并且获取新打开窗口的句柄
        self.link.visit_genero_customer_page()
        # 获取当前句柄的title
        _title = self.link.get_title()
        try:
            if _title == self.assert_public_customer_cn:
                email = self.link.get_genero_customer_cn()
                # 校验预期结果与实际结果是否一致
                self.assertEqual(email, self.assert_public_email_title,
                                 self.output_verify_fail % (self.assert_public_email_title, email))
                # 将结果输入到日志文件
                log1.info(self.output_verify_success % (self.assert_public_email_title, _title))
                # 保存截图
                self.link.save_window_snapshot(self.case_name)
                # 关闭浏览器窗口
                self.link.close_browser()
                # 切换窗口
                self.link.switch_to_window_by_title(self.assert_public_video_genero)
                log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
            elif _title == self.assert_public_customer_en:
                self.assertEqual(_title, self.assert_public_customer_en,
                                 self.output_verify_fail % (self.assert_public_customer_en, _title))
                # 将结果输入到日志文件
                log1.info(self.output_verify_success % (self.assert_public_customer_en, _title))
                # 保存截图
                self.link.save_window_snapshot(self.case_name)
                # 关闭浏览器窗口
                self.link.close_browser()
                # 切换窗口
                self.link.switch_to_window_by_title(self.assert_public_video_genero)
                log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            # 关闭浏览器窗口
            self.link.close_browser()
            # 切换窗口
            self.link.switch_to_window_by_title(self.assert_public_video_genero)
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_genero_005')
    def test_genero_005(self):
        """未登录情况下，在金管家页面访问官方首页"""
        self.case_name = '未登录情况下，在金管家页面访问官方首页'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在金管家页面访问官方首页，并且获取新打开窗口的句柄
        self.link.visit_genero_home_page()
        # 获取当前句柄的title
        _title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(_title, self.assert_public_home_title,
                             self.output_verify_fail % (self.assert_public_home_title, _title))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_home_title, _title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭浏览器窗口
            self.link.close_browser()
            # 切换窗口
            self.link.switch_to_window_by_title(self.assert_public_video_genero)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭浏览器窗口
            self.link.close_browser()
            # 切换窗口
            self.link.switch_to_window_by_title(self.assert_public_video_genero)
            raise

    @BeautifulReport.add_test_img('test_genero_006')
    def test_genero_006(self):
        """未登录情况下，在金管家页面访问账号交易"""
        self.case_name = '未登录情况下，在金管家页面访问账号交易'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在金管家页面访问账号交易
        self.link.visit_genero_account_page()
        # 获取弹窗
        _alert = self.driver.switch_to_alert()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(_alert.text, self.assert_public_account_title,
                             self.output_verify_fail % (self.assert_public_account_title, _alert.text))
            # 关闭弹窗
            _alert.accept()
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_genero_007')
    @ddt.data(*case_data)
    def test_genero_007(self, data):
        """未登录情况下，在金管家页面执行等级查询"""
        self.case_name = data['case_name']
        log1.info("Executing use test case：%s" % self.case_name)
        self.suc = self.data_suc
        self.name = data['username']
        self.assert_value = self.assert_login_first
        log1.info('input data:name:%s,suc:%s,assert:%s' % (self.name, self.suc, self.assert_value))
        # 执行查询方法
        self.re_data = self.link.input_search_text(self.suc, self.name)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_value,self.output_verify_fail % (self.assert_value, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_value,  self.re_data))
            # 强制等待
            self.link.forced_wait(1)
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise
