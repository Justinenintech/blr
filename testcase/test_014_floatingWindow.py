# -*- coding: UTF-8 -*-
import os
import unittest
import yaml

from Common.basePage import BasePage
from Common.getYaml import get_yaml

from Common.log import log1
from BeautifulReport import BeautifulReport

from PageObject.page_floatingWindow import FloatingWindow


class TestDownloadAPP(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath
    # 获取yaml文件内容
    data = get_yaml()
    assert_public_app_title = data['asserts'].get('assert_public_app_title')  # APP下载title
    assert_app_ios_help = data['asserts'].get('assert_app_ios_help')  # ios安装教程title
    assert_public_home_title = data['asserts'].get('assert_public_home_title')  # 首页
    assert_zhucezhanghao = data['asserts'].get('assert_zhucezhanghao')
    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')
    assert_public_customer_en = data['asserts'].get('assert_public_customer_en')
    assert_public_customer_cn = data['asserts'].get('assert_public_customer_cn')
    assert_public_email_title = data['asserts'].get('assert_public_email_title')  # 在线客服-投诉邮箱账号
    assert_public_carousel_announcement = data['asserts'].get('assert_public_carousel_announcement')
    assert_public_lottery_genero = data['asserts'].get('assert_public_lottery_genero')
    assert_public_interest_title = data['asserts'].get('assert_public_interest_title')
    assert_register_reset = data['asserts'].get('assert_register_reset')
    link_float_r_close = data['links'].get('link_float_r_close')
    link_float_l_close = data['links'].get('link_float_l_close')
    username = data['datas'].get('data_last_username')  # 上一次成功注册的账号
    password = data['datas'].get('data_password')
    suc = data['datas'].get('data_suc')

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
        self.link = FloatingWindow(self.driver)

    @BeautifulReport.add_test_img('test_app_download_001')
    def test_float_window_001(self):
        """未登录情况下，访问右侧悬浮窗口的加入会员页面"""
        self.case_name = '未登录情况下，访问右侧悬浮窗口的加入会员页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_float_huiyuan()
        # 获取当前句柄的title
        self.re_data = self.link.get_huiyuan_text(self.suc)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_register_reset,
                             self.output_verify_fail % (
                                 self.assert_register_reset, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_register_reset, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_float_window_002')
    def test_float_window_002(self):
        """未登录情况下，访问右侧悬浮窗口的在线客服页面"""
        self.case_name = '未登录情况下，访问右侧悬浮窗口的在线客服页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 通过导航栏访问在线客服
        self.link.visit_float_customer()
        # 获取当前窗口句柄的title信息
        self._title = self.link.get_title()
        try:
            if self._title == self.assert_public_customer_cn:
                self.email = self.link.get_float_customer_cn()
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
                self.link.switch_to_window_by_title(self.assert_public_home_title)
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
                self.link.switch_to_window_by_title(self.assert_public_home_title)
                log1.info("Successful execution of test case:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_home_title)
            # self.skipTest('error，test_interest_free_015')
            raise

    @BeautifulReport.add_test_img('test_app_download_003')
    def test_float_window_003(self):
        """未登录情况下，访问右侧悬浮窗口的支付秒到帐页面"""
        self.case_name = '未登录情况下，访问右侧悬浮窗口的支付秒到帐页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问支付秒到帐页面
        self.re_data = self.link.visit_float_transfer(self.suc)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_public_carousel_announcement,
                             self.output_verify_fail % (
                                 self.assert_public_carousel_announcement, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_public_carousel_announcement, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_float_window_004')
    def test_float_window_004(self):
        """未登录情况下，访问左侧悬浮窗口的金管家页面"""
        self.case_name = '未登录情况下，访问左侧悬浮窗口的金管家页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        #self.link.find_click_notice()
        # 访问金管家页面，并且获取新打开窗口的句柄
        self.link.visit_float_guanjia()
        # 获取当前句柄的title
        self.re_data = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_public_lottery_genero,
                             self.output_verify_fail % (
                                 self.assert_public_lottery_genero, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_public_lottery_genero, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_home_title)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_float_window_005')
    def test_float_window_005(self):
        """未登录情况下，访问左侧悬浮窗口的免息借呗页面"""
        self.case_name = '未登录情况下，访问左侧悬浮窗口的免息借呗页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问免息借呗页面，并且获取新打开窗口的句柄
        self.link.visit_float_jiebei()
        # 获取当前句柄的title
        self.re_data = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_public_interest_title,
                             self.output_verify_fail % (
                                 self.assert_public_interest_title, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_public_interest_title, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            # 关闭当前浏览器窗口
            self.link.close_browser()
            # 返回浏览器窗口{test_interest_free_013}
            self.link.switch_to_window_by_title(self.assert_public_home_title)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_float_window_006')
    def test_float_window_006(self):
        """未登录情况下，关闭右侧悬浮窗，再执行刷新，验证悬浮窗是否成功加载"""
        self.case_name = '未登录情况下，关闭左侧和右侧悬浮窗，再执行刷新，验证悬浮窗是否成功加载'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 关闭右侧悬浮窗
        self.link.visit_float_r_close()
        self.link.forced_wait(1)
        # 获取当前句柄的title
        self.link.refresh()
        self.link.forced_wait(1)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertTrue(self.link.get_displayed(self.link_float_r_close))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_float_window_007')
    def test_float_window_007(self):
        """未登录情况下，关闭左侧悬浮窗，再执行刷新，验证悬浮窗是否成功加载"""
        self.case_name = '未登录情况下，关闭左侧和右侧悬浮窗，再执行刷新，验证悬浮窗是否成功加载'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        #self.link.find_click_notice()
        # 关闭左侧悬浮窗
        self.link.visit_float_l_close()
        self.link.forced_wait(1)
        # 获取当前句柄的title
        self.link.refresh()
        self.link.forced_wait(1)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertTrue(self.link.get_displayed(self.link_float_l_close))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_app_download_008')
    def test_float_window_008(self):
        """未登录情况下，访问轮播公告"""
        self.case_name = '未登录情况下，访问轮播公告'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问轮播公告
        self.re_data = self.link.visit_carousel_announcement(self.suc)
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_public_carousel_announcement,
                             self.output_verify_fail % (
                                 self.assert_public_carousel_announcement, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_public_carousel_announcement, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    # @BeautifulReport.add_test_img('test_float_window_009')
    # def test_float_window_009(self):
    #     """已登录情况下，访问轮播公告"""
    #     self.case_name = '未登录情况下，访问轮播公告'
    #     log1.info("Executing test cases：%s" % self.case_name)
    #     # 判断是否存在网站公告，如果存在则关闭公告提示！
    #     self.link.find_click_notice()
    #     # 输入登录用户名
    #     self.link.type_login_username(self.username)
    #     #         # 输入登录密码
    #     self.link.type_login_password(self.password)
    #     #         # 如果存在验证码，则输入获取的验证码信息
    #     self.link.find_type_login_code()
    #     # 访问轮播公告
    #     self.link.visit_login_carousel_announcement(self)
    #     self.re_data = self.link.get_car_announcement()
    #     try:
    #         # 校验预期结果与实际结果是否一致
    #         self.assertEqual(self.re_data, "系统信息",
    #                          self.output_verify_fail % (
    #                              "系统信息", self.re_data))
    #         log1.info(self.output_verify_success % (
    #             "系统信息", self.re_data))
    #         # 保存截图
    #         self.link.save_window_snapshot(self.case_name)
    #         log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
    #     except AssertionError as e:
    #         log1.error("Failure of test case execution：%s" % e + '\n')
    #         raise
    #
    # @BeautifulReport.add_test_img('test_float_window_010')
    # def test_float_window_010(self):
    #     """未登录情况下，访问支付秒到帐"""
    #     self.case_name = '未登录情况下，访问支付秒到帐'
    #     log1.info("Executing test cases：%s" % self.case_name)
    #     # 判断是否存在网站公告，如果存在则关闭公告提示！
    #     self.link.find_click_notice()
    #     # 输入登录用户名
    #     self.link.type_login_username(self.username)
    #     #         # 输入登录密码
    #     self.link.type_login_password(self.password)
    #     #         # 如果存在验证码，则输入获取的验证码信息
    #     self.link.find_type_login_code()
    #     # 访问轮播公告
    #     self.re_data = self.link.visit_login_float_transfer(self.suc)
    #     try:
    #         # 校验预期结果与实际结果是否一致
    #         self.assertEqual(self.re_data, "网银转帐",
    #                          self.output_verify_fail % (
    #                              "网银转帐", self.re_data))
    #         log1.info(self.output_verify_success % (
    #             "网银转帐", self.re_data))
    #         # 保存截图
    #         self.link.save_window_snapshot(self.case_name)
    #         log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
    #     except AssertionError as e:
    #         log1.error("Failure of test case execution：%s" % e + '\n')
    #         raise


    @classmethod
    def tearDownClass(cls):
        cls.link = FloatingWindow(cls.driver)
        cls.link.dr_quit()
