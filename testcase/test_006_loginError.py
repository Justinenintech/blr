import os
import unittest

import ddt
from BeautifulReport import BeautifulReport

from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.log import log1
from PageObject.page_login import LoginPage

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 0)


@ddt.ddt
class TestLoginError(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath

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
        self.link = LoginPage(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.link = LoginPage(cls.driver)
        cls.link.dr_quit()

    @BeautifulReport.add_test_img('test_login_error_001')
    def test_login_error_001(self):
        """登录测试用例"""
        self.link.find_click_notice()

    # @BeautifulReport.add_test_img('test_login')
    @ddt.data(*case_data)
    def test_login_error_002(self, data):
        """登录测试用例"""
        #self.link.find_click_notice()
        self.case_name = data['case_name']
        log1.info("Executing use test case:%s" % self.case_name)
        self.name = data['username']
        self.pwd = data['pwd']
        self.suc = data['suc']
        self.assert_value = data['assert']
        # self.link.save_window_snapshot(self.case_name)
        log1.info('input data:name:%s,pwd:%s,suc:%s,assert:%s' % (self.name, self.pwd, self.suc, self.assert_value))
        self.re_data = self.link.login(self.suc, self.name, self.pwd)
        try:
            self.assertIn(self.assert_value, self.re_data)
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise
