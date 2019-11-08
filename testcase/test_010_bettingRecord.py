import datetime
import os
import unittest

import ddt
from BeautifulReport import BeautifulReport

from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml
from Common.log import log1
from PageObject.page_bettingRecord import PageBettingRecord

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 8)


@ddt.ddt
class TestBettingRecord(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath
    # yaml文件读取
    data = get_yaml()


    username = data['datas'].get('data_last_username')  # 上一次成功注册的账号
    password = data['datas'].get('data_password')

    assert_betting_record = data['asserts'].get('assert_betting_record')  # 投注记录
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
        self.link = PageBettingRecord(self.driver)

    @BeautifulReport.add_test_img('test_betting_record_001')
    def test_betting_record_001(self):
        """新注册会员，登录情况下，访问投注记录"""
        self.case_name = '新注册会员，登录情况下，访问投注记录'
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
        # 浏览器置顶
        self.link.js_scroll_top()
        # 强制等待
        self.link.forced_wait(1)
        # 点击投注记录
        self.link.click_link_betting_record()
        # 获取投注记录标题
        self.re_data = self.link.verity_get_betting_record()
        try:
            # 验证标题是否一致
            self.assertEqual(self.re_data.replace(" ", ""), self.assert_betting_record,
                             self.output_verify_fail % (
                             self.assert_betting_record, self.re_data.replace(" ", "")))
            # 将结果输出到日志文件
            log1.info(self.output_verify_success % (
            self.assert_betting_record, self.re_data.replace(" ", "")))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name)
        except AssertionError as e:
            log1.error("Failure of test case execution:%s" % e)
            # self.skipTest(case_name)
            raise

    @classmethod
    def tearDownClass(cls) -> None:
        cls.link = PageBettingRecord(cls.driver)
        cls.link.dr_quit()
