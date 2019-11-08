# -*- coding: UTF-8 -*-
import os
import unittest
import yaml

from Common.basePage import BasePage
from Common.getYaml import get_yaml

from Common.log import log1
from BeautifulReport import BeautifulReport

from PageObject.page_appDownload import AppDownloadPage


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
        self.link = AppDownloadPage(self.driver)

    @BeautifulReport.add_test_img('test_app_download_001')
    def test_app_download_001(self):
        """未登录情况下，访问右侧悬浮窗口的APP下载页面"""
        self.case_name = '未登录情况下，访问右侧悬浮窗口的APP下载页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_app_download_page()
        # 获取当前句柄的title
        self.app_title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.app_title, self.assert_public_app_title,
                             self.output_verify_fail % (
                                 self.assert_public_app_title, self.app_title))
            log1.info(self.output_verify_success % (
                self.assert_public_app_title, self.app_title))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_app_download_002')
    def test_app_download_002(self):
        """在APP下载页面，访问ios教程页面"""
        self.case_name = '在APP下载页面，访问ios教程页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 访问ios教程
        self.link.visit_ios_help_page()
        # 获取教程的title信息
        app_title = self.link.get_ios_help_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(app_title, self.assert_app_ios_help, self.output_verify_fail % (
                self.assert_app_ios_help, app_title))
            log1.info(self.output_verify_success % (
                self.assert_app_ios_help, app_title))
            # 保存截图
            self.link.save_window_snapshot(self.assert_app_ios_help)
            # 关闭ios教程页面
            self.link.click_ios_help_close()
            self.link.forced_wait(1)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_app_download_003')
    def test_app_download_003(self):
        """在APP下载页面，点击【进入PC网页版】，访问网站首页"""
        self.case_name = '从APP下载页面，点击进入PC网页版，访问网站首页'
        log1.info("Executing test cases：%s" % self.case_name)
        # 获取进入PC网页版的title信息
        self.link.visit_pc_home_page()
        # 获取当前句柄的title
        app_title = self.link.get_title()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(app_title, self.assert_public_home_title,
                             self.output_verify_fail % (self.assert_public_home_title, app_title))
            log1.info(self.output_verify_success % (self.assert_public_home_title, app_title))
            # 保存截图
            self.link.save_window_snapshot(self.assert_public_home_title)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @classmethod
    def tearDownClass(cls):
        cls.link = AppDownloadPage(cls.driver)
        cls.link.dr_quit()
