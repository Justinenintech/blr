import os
import unittest

from BeautifulReport import BeautifulReport

from Common.basePage import BasePage
from Common.getTestData import get_test_data
from Common.getYaml import get_yaml
from Common.log import log1
from PageObject.page_gameLink import GameLinkPage

case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
                         'excels', 'case_data.xlsx')
case_data = get_test_data(case_path, 0)


class TestGameLink(unittest.TestCase):
    # 获取yaml文件内容
    data = get_yaml()
    suc = data['datas'].get('data_suc')
    _casino_game_name = data['datas'].get('data_casino_game_name')
    assert_public_login_first = data['asserts'].get('assert_public_login_first')
    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')
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
        self.link = GameLinkPage(self.driver)

    @classmethod
    def tearDownClass(cls):
        cls.link = GameLinkPage(cls.driver)
        cls.link.dr_quit()

    @BeautifulReport.add_test_img('test_start_game_001')
    def test_start_game_001(self):
        """未登录情况下，访问体育赛事中的皇冠体育"""
        self.case_name = "未登录情况下，访问体育赛事中的皇冠体育"
        log1.info("Executing use test cases: %s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 验证是否存在网站公告，如果存在则关闭
        self.link.find_click_notice()
        # 获取弹出提示信息
        self.re_data = self.link.visit_sport_hg_page(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_002')
    def test_start_game_002(self):
        """未登录情况下，访问体育赛事中的沙巴体育"""
        self.case_name = "未登录情况下，访问体育赛事中的沙巴体育"
        log1.info("Executing use test cases: %s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 获取弹出提示信息
        self.re_data = self.link.visit_sport_sb_page(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_003')
    def test_start_game_003(self):
        """未登录情况下，访问体育赛事中的BBin体育"""
        self.case_name = "未登录情况下，访问体育赛事中的BBin体育"
        log1.info("Executing use test cases: %s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 获取弹出提示信息
        self.re_data = self.link.visit_sport_bbin_page(self.suc)
        try:
            # 验证弹出提示信息是否一致 啊
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_004')
    def test_start_game_004(self):
        """未登录情况下，访问体育赛事中的AG体育"""
        self.case_name = "未登录情况下，访问体育赛事中的AG体育"
        log1.info("Executing use test case:%s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 获取弹出提示信息
        self.re_data = self.link.visit_sport_ag_page(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_005')
    def test_start_game_005(self):
        """未登录情况下，在视讯直播中启动AG场馆"""
        self.case_name = "未登录情况下，在视讯直播中启动AG场馆"
        log1.info("Executing use test case:%s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 获取弹出提示信息
        self.re_data = self.link.visit_game_live_ag_page(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_006')
    def test_start_game_006(self):
        """未登录情况下，在电子游艺中启动[游戏xxx]"""
        self.case_name = "未登录情况下，在电子游艺中启动[游戏xxx]"
        log1.info("Executing use test case:%s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 获取弹出提示信息
        self.re_data = self.link.visit_game_casino_page(self.suc, self._casino_game_name)
        try:
            self.assertEqual(self.re_data, self.assert_public_login_first)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_007')
    def test_start_game_007(self):
        """未登录情况下，访问棋牌游戏中的乐游棋牌"""
        self.case_name = "未登录情况下，访问棋牌游戏中的乐游棋牌"
        log1.info("Executing use test cases:%s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 置顶
        self.link.js_scroll_top()
        # 强制等待
        self.link.forced_wait(1)
        # 获取弹出提示信息
        self.re_data = self.link.visit_game_chess_ly(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_008')
    def test_start_game_008(self):
        """未登录情况下，访问棋牌游戏中的开元棋牌"""
        self.case_name = "未登录情况下，访问棋牌游戏中的开元棋牌"
        log1.info("Executing use test cases:%s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 置顶
        self.link.js_scroll_top()
        # 强制等待
        self.link.forced_wait(1)
        # 获取弹出提示信息
        self.re_data = self.link.visit_game_chess_ky(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_start_game_009')
    def test_start_game_009(self):
        """未登录情况下，访问棋牌游戏中的VG棋牌"""
        self.case_name = "未登录情况下，访问棋牌游戏中的VG棋牌"
        log1.info("Executing use test cases:%s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 置顶
        self.link.js_scroll_top()
        # 强制等待
        self.link.forced_wait(1)
        # 获取弹出提示信息
        self.re_data = self.link.visit_game_chess_vg(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise

    # @BeautifulReport.add_test_img('test_start_game_010')
    # def test_start_game_010(self):
    #     """未登录情况下，访问棋牌游戏中的FG棋牌"""
    #     self.case_name = "未登录情况下，访问棋牌游戏中的FG棋牌"
    #     log1.info("Executing use test case:%s" % self.case_name)
    #     log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
    #     # 置顶
    #     self.link.js_scroll_top()
    #     # 强制等待
    #     self.link.forced_wait(1)
    #     # 获取弹出提示信息
    #     self.re_data = self.link.visit_game_chess_fg(self.suc)
    #     try:
    #         # 验证弹出提示信息是否一致
    #         self.assertEqual(self.re_data, self.assert_public_login_first,
    #                          self.output_verify_fail % (self.assert_public_login_first, self.re_data))
    #         # 将结果输入到日志文件
    #         log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
    #         # 保存截图
    #         self.link.save_window_snapshot(self.case_name)
    #         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
    #     except AssertionError as e:
    #         log1.error('Failure of test case execution! Reason: %s' % e + '\n')
    #         raise

    @BeautifulReport.add_test_img('test_start_game_011')
    def test_start_game_011(self):
        """未登录情况下，访问棋牌游戏中的天豪棋牌"""
        self.case_name = "未登录情况下，访问棋牌游戏中的天豪棋牌"
        log1.info("Executing use test case:%s" % self.case_name)
        log1.info('input data:suc:%s,assert:%s' % (self.suc, self.assert_public_login_first))
        # 置顶
        self.link.js_scroll_top()
        # 强制等待
        self.link.forced_wait(1)
        # 获取弹出提示信息
        self.re_data = self.link.visit_game_chess_th(self.suc)
        try:
            # 验证弹出提示信息是否一致
            self.assertEqual(self.re_data, self.assert_public_login_first,
                             self.output_verify_fail % (self.assert_public_login_first, self.re_data))
            # 将结果输入到日志文件
            log1.info(self.output_verify_success % (self.assert_public_login_first, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')
            raise
