# -*- coding: UTF-8 -*-
import os
import unittest

import ddt
from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml

from Common.log import log1
from BeautifulReport import BeautifulReport

from PageObject.page_interestFree import InterestFreePage

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 4)


@ddt.ddt
class TestInterestFree(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath

    data = get_yaml()
    assert_public_interest_title = data['asserts'].get('assert_public_interest_title')  # 免息借呗首页
    assert_public_action = data['asserts'].get('assert_public_action')  # 请登录操作
    assert_public_video_title = data['asserts'].get('assert_public_video_title')  # 视讯额度
    assert_public_chess_title = data['asserts'].get('assert_public_chess_title')  # 棋牌额度
    assert_public_lottery_title = data['asserts'].get('assert_public_lottery_title')  # 彩票额度
    assert_public_casino_title = data['asserts'].get('assert_public_casino_title')  # 电子额度
    assert_public_records_title = data['asserts'].get('assert_public_records_title')  # 借还款记录
    assert_interest_account_title = data['asserts'].get('assert_interest_account_title')  # 账号买卖提示信息
    assert_public_email_title = data['asserts'].get('assert_public_email_title')  # 在线客服-投诉邮箱账号
    assert_public_video_genero = data['asserts'].get('assert_public_video_genero')  # 视讯金管家等级查询
    assert_public_chess_genero = data['asserts'].get('assert_public_chess_genero')  # 棋牌金管家等级查询
    assert_public_lottery_genero = data['asserts'].get('assert_public_lottery_genero')  # 彩票金管家等级查询
    assert_public_casino_genero = data['asserts'].get('assert_public_casino_genero')  # 电子金管家等级查询
    assert_public_customer_en = data['asserts'].get('assert_public_customer_en')
    assert_public_customer_cn = data['asserts'].get('assert_public_customer_cn')
    assert_public_en_title = data['asserts'].get('assert_public_en_title')
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
        self.link = InterestFreePage(self.driver)

    # @classmethod
    # def tearDown(cls):
    #     cls.link = TopLinkPage(cls.driver)
    #     cls.link.dr_quit()

    @classmethod
    def tearDownClass(cls):
        cls.link = InterestFreePage(cls.driver)
        cls.link.dr_quit()

    @BeautifulReport.add_test_img('test_interest_free_001')
    def test_interest_free_001(self):
        """未登录情况下，访问免息借呗页面"""
        self.case_name = '未登录情况下，访问免息借呗页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        self.link.find_click_notice()
        # 访问免息借呗页面，并且获取新打开窗口的句柄
        self.link.visit_interest_free_loan()
        # 获取当前句柄的title
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_interest_title,
                             self.output_verify_fail % (self.assert_public_interest_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_interest_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_002')
    def test_interest_free_002(self):
        """未登录情况下，在免息借呗页面点击[我要借款]"""
        self.case_name = '未登录情况下，在免息借呗页面点击[我要借款]'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在免息借呗页面点击[我要借款]
        self.link.visit_interest_borrow_money()
        # 强制等待
        self.link.forced_wait(1)
        # 获取弹出提示框信息
        self.war_text = self.link.get_interest_war_text()
        # 关闭弹出提示框
        self.link.click_interest_close_warning()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.war_text, self.assert_public_action,
                             self.output_verify_fail % (self.assert_public_action, self.war_text))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_action, self.war_text))
            # 判断输入框的状态
            if self.link.type_user_disabled() == False and self.link.type_borrow_disabled() == True:
                # 保存截图
                self.link.save_window_snapshot('我要借款')
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_003')
    def test_interest_free_003(self):
        """未登录情况下，在免息借呗页面点击[我要还款]"""
        self.case_name = '未登录情况下，在免息借呗页面点击[我要还款]'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在免息借呗页面点击[我要还款]
        self.link.visit_interest_repay_money()
        # 强制等待
        self.link.forced_wait(1)
        # 获取弹出提示框信息
        self.war_text = self.link.get_interest_war_text()
        # 关闭弹出提示框
        self.link.click_interest_close_warning()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.war_text, self.assert_public_action,
                             self.output_verify_fail % (self.assert_public_action, self.war_text))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_action, self.war_text))
            # 判断输入框的状态
            if self.link.type_user_disabled() == False and self.link.type_repay_disabled() == True:
                # 保存截图
                self.link.save_window_snapshot('我要还款')
                # 访问首页
                self.link.visit_interest_home_page()
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            self.link.visit_interest_home_page()
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @ddt.data(*case_data)
    def test_interest_free_004(self, data):
        """未登录情况下，点击额度查询"""
        self.case_name = data['case_name']
        log1.info("Executing use test case:%s" % self.case_name)
        self.suc = data['suc']
        self.name = data['username']
        self.assert_value = data['assert_vale']
        log1.info('input data:name:%s,suc:%s,assert:%s' % (self.name, self.suc, self.assert_value))
        # 执行额度查询方法
        self.re_data = self.link.input_interestFree_search_text(self.suc, self.name)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_value,
                             self.output_verify_fail % (self.assert_value, self.re_data))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_value, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            self.save_img('test_interest_free_004')
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_005')
    def test_interest_free_005(self):
        """未登录情况下，在免息借呗首页，通过立即查看访问视讯额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过立即查看访问视讯额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过立即查看访问视讯额度页面
        self.link.visit_interest_video_page()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_video_title,
                             self.output_verify_fail % (self.assert_public_video_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_video_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 返回上一次
            self.link.back()
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_006')
    def test_interest_free_006(self):
        """未登录情况下，在免息借呗首页，通过立即查看访问棋牌额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过立即查看访问棋牌额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过立即查看访问棋牌额度页面
        self.link.visit_interest_chess_page()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_chess_title,
                             self.output_verify_fail % (self.assert_public_chess_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_chess_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 返回上一次
            self.link.back()
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_007')
    def test_interest_free_007(self):
        """未登录情况下，在免息借呗首页，通过立即查看访问彩票额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过立即查看访问彩票额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过立即查看访问彩票额度页面
        self.link.visit_interest_lottery_page()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_lottery_title,
                             self.output_verify_fail % (self.assert_public_lottery_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_lottery_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 返回上一次
            self.link.back()
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_008')
    def test_interest_free_008(self):
        """未登录情况下，在免息借呗首页，通过立即查看访问电子额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过立即查看访问电子额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过立即查看访问电子额度页面
        self.link.visit_interest_casino_page()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_casino_title,
                             self.output_verify_fail % (self.assert_public_casino_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_casino_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 返回上一次
            self.link.back()
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_009')
    def test_interest_free_009(self):
        """未登录情况下，在免息借呗首页，通过导航栏访问视讯额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过导航栏访问视讯额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问视讯额度页面
        self.link.visit_interest_video_quota()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_video_title,
                             self.output_verify_fail % (self.assert_public_video_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_video_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_010')
    def test_interest_free_010(self):
        """未登录情况下，在免息借呗首页，通过导航栏访问棋牌额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过导航栏访问棋牌额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问棋牌额度页面
        self.link.visit_interest_chess_quota()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_chess_title,
                             self.output_verify_fail % (self.assert_public_chess_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_chess_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_011')
    def test_interest_free_011(self):
        """未登录情况下，在免息借呗首页，通过导航栏访问彩票额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过导航栏访问彩票额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问彩票额度页面
        self.link.visit_interest_lottery_quota()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_lottery_title,
                             self.output_verify_fail % (self.assert_public_lottery_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_lottery_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_012')
    def test_interest_free_012(self):
        """未登录情况下，在免息借呗首页，通过导航栏访问电子额度页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过导航栏访问电子额度页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问电子额度页面
        self.link.visit_interest_casino_quota()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_casino_title,
                             self.output_verify_fail % (self.assert_public_casino_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_casino_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_013')
    def test_interest_free_013(self):
        """未登录情况下，在免息借呗首页，通过导航栏访问借还款记录页面"""
        self.case_name = '未登录情况下，在免息借呗首页，通过导航栏访问借还款记录页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问借还款记录页面
        self.link.visit_interest_records()
        # 获取当前句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_records_title,
                             self.output_verify_fail % (self.assert_public_records_title, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_records_title, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_014')
    def test_interest_free_014(self):
        """未登录情况下，在免息借呗首页，通过导航栏访问账号买卖"""
        self.case_name = '未登录情况下，在免息借呗首页，通过导航栏访问账号买卖'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问账号买卖
        self.link.visit_interest_account_sale()
        # 获取弹出提示框的提示信息
        self.war_text = self.link.get_interest_war_text()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.war_text, self.assert_interest_account_title,
                             self.output_verify_fail % (self.assert_interest_account_title, self.war_text))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_interest_account_title, self.war_text))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭弹出提示框
            self.link.click_interest_close_warning()
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            self.link.refresh()
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_015')
    def test_interest_free_015(self):
        """未登录情况下，在免息借呗首页，通过导航栏访问在线客服"""
        self.case_name = '未登录情况下，在免息借呗首页，通过导航栏访问在线客服'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问在线客服
        self.link.visit_interest_customer()
        # 获取当前窗口句柄的title信息
        self._title = self.link.get_title()
        try:
            if self._title == self.assert_public_customer_cn:
                self.email = self.link.get_genero_customer_cn()
                # 校验预期结果与实际结果是否一致
                self.assertEqual(self.email, self.assert_public_email_title,
                                 self.output_verify_fail % (self.assert_public_email_title, self.email))
                # 将结果输出到日志文件
                log1.info(self.output_verify_success % (
                    self.assert_public_email_title, self.email))
                # 保存截图
                self.link.save_window_snapshot(self.case_name)
                # 关闭当前浏览器窗口
                self.link.close_browser()
                # 返回浏览器窗口{test_interest_free_013}
                self.link.switch_to_window_by_title(self.assert_public_records_title)
                log1.info("Successful execution of test case:%s" % self.case_name + '\n')
            elif self._title == self.assert_public_customer_en:
                # 校验预期结果与实际结果是否一致
                self.assertEqual(self._title, self.assert_public_customer_en,
                                 self.output_verify_fail % (self.assert_public_customer_en, self._title))
                # 将结果输出到日志文件
                log1.info(self.output_verify_success % (
                    self.assert_public_customer_en, self._title))
                # 保存截图
                self.link.save_window_snapshot(self.case_name)
                # 关闭当前浏览器窗口
                self.link.close_browser()
                # 返回浏览器窗口{test_interest_free_013}
                self.link.switch_to_window_by_title(self.assert_public_records_title)
                log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            # self.skipTest('error，test_interest_free_015')
            raise

    @BeautifulReport.add_test_img('test_interest_free_016')
    def test_interest_free_016(self):
        """未登录情况下，在免息借呗首页访问视讯金管家页面"""
        self.case_name = '未登录情况下，在免息借呗首页访问视讯金管家页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在免息借呗首页访问视讯金管家页面
        self.link.visit_interest_video_genero()
        # 获取当前窗口句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_video_genero,
                             self.output_verify_fail % (self.assert_public_video_genero, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_video_genero, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_interest_free_017')
    def test_interest_free_017(self):
        """未登录情况下，在免息借呗首页访问棋牌金管家页面"""
        self.case_name = '未登录情况下，在免息借呗首页访问棋牌金管家页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在免息借呗首页访问棋牌金管家页面
        self.link.visit_interest_chess_genero()
        # 获取当前窗口句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_chess_genero,
                             self.output_verify_fail % (self.assert_public_chess_genero, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_chess_genero, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            self.skipTest('error，test_interest_free_017')
            raise

    @BeautifulReport.add_test_img('test_interest_free_018')
    def test_interest_free_018(self):
        """未登录情况下，在免息借呗首页访问彩票金管家页面"""
        self.case_name = '未登录情况下，在免息借呗首页访问彩票金管家页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在免息借呗首页访问彩票金管家页面
        self.link.visit_interest_lottery_genero()
        # 获取当前窗口句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_lottery_genero,
                             self.output_verify_fail % (self.assert_public_lottery_genero, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_lottery_genero, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            self.skipTest('error，test_interest_free_018')
            raise

    @BeautifulReport.add_test_img('test_interest_free_019')
    def test_interest_free_019(self):
        """未登录情况下，在免息借呗首页访问电子金管家页面"""
        self.case_name = '未登录情况下，在免息借呗首页访问电子金管家页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 在免息借呗首页访问彩票金管家页面
        self.link.visit_interest_casino_genero()
        # 获取当前窗口句柄的title信息
        self._title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self._title, self.assert_public_casino_genero,
                             self.output_verify_fail % (self.assert_public_casino_genero, self._title))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
                self.assert_public_casino_genero, self._title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_records_title)
            self.skipTest('error，test_interest_free_019')
            raise
