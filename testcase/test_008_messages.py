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
from PageObject.page_messages import PageMessages

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 8)


@ddt.ddt
class TestMessages(unittest.TestCase):
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
    assert_sys_message = data['asserts'].get('assert_sys_message')
    assert_sys_message_title = data['asserts'].get('assert_sys_message_title')
    assert_suggestion_title = data['asserts'].get('assert_suggestion_title')
    assert_suggestion_area = data['asserts'].get('assert_suggestion_area')
    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')

    # assert_sys_message: 系统信息
    # assert_sys_message_el:
    # - css
    # selector
    # -.preferential >.header

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
        self.link = PageMessages(self.driver)

    @BeautifulReport.add_test_img('test_messages_001')
    def test_messages_001(self):
        """新注册会员，验证系统消息是否正确"""
        self.case_name = '新注册会员，验证系统消息是否正确'
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
        # # 浏览器置顶
        self.link.js_scroll_top()
        # 强制等待
        self.link.forced_wait(1)
        # 点击未读讯息按钮
        self.link.click_link_unread_message()
        # # 获取中间布局的标题信息
        # _title = self.link.verity_get_sys_msg_title()
        # # 获取右侧布局的标题信息
        # _right_title = self.link.verity_get_sys_msg_right_title()
        # # 获取左侧布局的日期信息
        # _time = self.link.verity_get_sys_msg_time()
        # # 获取当前系统日期
        # now_time = datetime.datetime.now()
        # _time_now = now_time.strftime('%Y-%m-%d')  # %H%M%S
        _title = self.link.get_assert_sys_message_el()
        try:
            # 验证标题是否一致
            self.assertIn(self.assert_sys_message, _title.replace(" ", ""))
            # 验证标题是否一致
            # self.assertIn(self.assert_sys_message_title, _right_title.replace(" ", ""))
            # # 验证消息日期是否正确
            # self.assertIn(_time, _time_now)
            # 断言成功，截图
            self.link.save_window_snapshot(self.case_name)
            # 访问投诉建议页面
            self.link.click_tab_suggestions()
            log1.info("Successful execution of test cases:%s" % self.case_name)
        except AssertionError as e:
            # self.save_img(case_name)
            self.link.click_tab_suggestions()
            log1.error("Failure of test case execution:%s" % e)
            # self.skipTest(case_name)
            raise

    @BeautifulReport.add_test_img('test_messages_002')
    @ddt.data(*case_data)
    def test_messages_002(self,data):
        """新注册会员，验证是否能够成功发送投诉建议"""
        self.case_name = '新注册会员，验证是否能够成功发送投诉建议'
        # self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        self.suc = data['suc']
        self.title = data['title']
        self.area = data['area']
        self.assert_value = data['assert_vale']
        # 验证是否能够提交投诉建议
        self.re_data = self.link.verify_suggestion(self.suc,self.title,self.area)
        try:
            # 验证提示信息的预期结果与实际结果是否一致
            self.assertIn(self.assert_value, self.re_data.replace(" ", ""))
            # 断言成功，截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name)
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error("Failure of test case execution:%s" % e)
            # self.skipTest(case_name)
            raise

    @BeautifulReport.add_test_img('test_messages_003')
    def test_messages_003(self):
        """新注册会员，验证已发投注信息的内容是否正确"""
        self.case_name = '新注册会员，验证已发投注信息的内容是否正确'
        # self.case_name = data['case_name']
        log1.info("Executing test cases：%s" % self.case_name)
        try:
            # 访问已发送消息
            self.link.click_tab_sent_message()
            # 获取已发送消息标题
            _title = self.link.verity_sent_msg_title()
            # 验证标题是否一致
            self.assertEqual(_title.replace(" ",""), self.assert_suggestion_title)
            # 获取已发送消息内容
            _area = self.link.verity_sent_msg_area()
            # 验证内容是否一致
            self.assertEqual(_area.replace(" ", ""), self.assert_suggestion_area)
            # 获取已发送消息日期
            _time = self.link.verity_get_sys_msg_time()
            now_time = datetime.datetime.now()
            _time_now = now_time.strftime('%Y-%m-%d')  # %H%M%S
            # 验证日期是否正确
            self.assertIn(_time, _time_now)
            # 断言成功，截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name)
        except AssertionError as e:
            self.save_img(self.case_name)
            log1.error("Failure of test case execution:%s" % e)
            # self.skipTest(case_name)
            raise

    @classmethod
    def tearDownClass(cls) -> None:
        cls.link = PageMessages(cls.driver)
        cls.link.dr_quit()
