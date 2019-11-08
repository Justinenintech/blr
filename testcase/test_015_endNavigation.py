# -*- coding: UTF-8 -*-
import os
import unittest

from Common.basePage import BasePage
from Common.getYaml import get_yaml

from Common.log import log1
from BeautifulReport import BeautifulReport
from PageObject.page_endNavigation import EndNavigation

data = get_yaml()


class TestEndNavigation(unittest.TestCase):
    d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                     'error_img')
    abspath = os.path.abspath(d)
    """ 测试报告的基础用例Sample """
    driver = None
    img_path = abspath
    # 获取yaml文件内容
    data = get_yaml()

    output_verify_fail = data['outputs'].get('output_verify_fail')
    output_verify_success = data['outputs'].get('output_verify_success')
    assert_about_us =  data['asserts'].get('assert_about_us')
    assert_contact_us = data['asserts'].get('assert_contact_us')
    assert_withdrawal_help = data['asserts'].get('assert_withdrawal_help')
    assert_deposit_help = data['asserts'].get('assert_deposit_help')
    assert_common_problem_1 = data['asserts'].get('assert_common_problem_1')
    assert_common_problem_2 = data['asserts'].get('assert_common_problem_2')
    assert_common_problem_3 = data['asserts'].get('assert_common_problem_3')
    assert_responsible_betting1 = data['asserts'].get('assert_responsible_betting1')
    assert_responsible_betting2 = data['asserts'].get('assert_responsible_betting2')

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
        self.link = EndNavigation(self.driver)

    @BeautifulReport.add_test_img('test_end_navigation_001')
    def test_end_navigation_001(self):
        """访问关于我们页面"""
        self.case_name = '访问关于我们页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        self.link.find_click_notice()
        self.link.forced_wait(1)
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_link_about_us()
        # 获取当前句柄的title
        self.re_data = self.link.get_about_us()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_about_us,
                             self.output_verify_fail % (
                                 self.assert_about_us, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_about_us, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_002')
    def test_end_navigation_002(self):
        """访问联系我们页面"""
        self.case_name = '访问联系我们页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_link_contact_us()
        # 获取当前句柄的title
        self.re_data = self.link.get_contact_us()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertIn(self.assert_contact_us,self.re_data,
                             self.output_verify_fail % (
                              self.assert_contact_us, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_contact_us, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_003')
    def test_end_navigation_003(self):
        """访问存款帮助页面"""
        self.case_name = '访问存款帮助页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_link_deposit_help()
        # 获取当前句柄的title
        self.re_data = self.link.get_deposit_help()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data,self.assert_deposit_help,
                             self.output_verify_fail % (
                                 self.assert_deposit_help, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_deposit_help, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_004')
    def test_end_navigation_004(self):
        """访问取款帮助页面"""
        self.case_name = '访问取款帮助页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        #self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_link_withdrawal_help()
        # 获取当前句柄的title
        self.re_data = self.link.get_withdrawal_help()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data,self.assert_withdrawal_help,
                             self.output_verify_fail % (
                                 self.assert_withdrawal_help, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_withdrawal_help, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_005')
    def test_end_navigation_005(self):
        """访问常见问题-一般常见问题页面"""
        self.case_name = '访问常见问题-一般常见问题页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        #self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_link_common_problem()
        # 获取当前句柄的title
        self.re_data = self.link.get_questions1()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data,self.assert_common_problem_1,
                             self.output_verify_fail % (
                                 self.assert_common_problem_1, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_common_problem_1, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_006')
    def test_end_navigation_006(self):
        """访问常见问题-游戏及投注问题页面"""
        self.case_name = '访问常见问题-游戏及投注问题页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        #self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_tab_questions_2()
        # 获取当前句柄的title
        self.re_data = self.link.get_questions2()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data,self.assert_common_problem_2,
                             self.output_verify_fail % (
                                 self.assert_common_problem_2, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_common_problem_2, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_007')
    def test_end_navigation_007(self):
        """访问常见问题-游戏及投注问题页面"""
        self.case_name = '访问常见问题-游戏及投注问题页面'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_tab_questions_3()
        # 获取当前句柄的title
        self.re_data = self.link.get_questions3()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_common_problem_3,
                             self.output_verify_fail % (
                                 self.assert_common_problem_3, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_common_problem_3, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_008')
    def test_end_navigation_008(self):
        """访问责任与博彩"""
        self.case_name = '访问责任与博彩'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_link_responsible_betting()
        # 获取当前句柄的title
        self.re_data = self.link.get_responsible_betting_el1()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_responsible_betting1,
                             self.output_verify_fail % (
                                 self.assert_responsible_betting1, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_responsible_betting1, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_009')
    def test_end_navigation_009(self):
        """访问责任与博彩-条款与规则"""
        self.case_name = '访问责任与博彩-条款与规则'
        log1.info("Executing test cases：%s" % self.case_name)
        # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问APP下载页面，并且获取新打开窗口的句柄
        self.link.visit_responsible_betting_el2()
        # 获取当前句柄的title
        self.re_data = self.link.get_responsible_betting_el2()
        try:
            # 校验预期结果与实际结果是否一致
            self.assertEqual(self.re_data, self.assert_responsible_betting2,
                             self.output_verify_fail % (
                                 self.assert_responsible_betting2, self.re_data))
            log1.info(self.output_verify_success % (
                self.assert_responsible_betting2, self.re_data))
            # 保存截图
            self.link.save_window_snapshot(self.case_name)
            log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error("Failure of test case execution：%s" % e + '\n')
            raise

    @BeautifulReport.add_test_img('test_end_navigation_010')
    def test_end_navigation_010(self):
        """访问代理加盟页面,默认为金字塔代理模式"""
        self.case_name = '访问代理加盟页面,默认为金字塔代理模式'
        log1.info("Executing use test case:%s" % self.case_name)
        #     # 判断是否存在网站公告，如果存在则关闭公告提示！
        # self.link.find_click_notice()
        # 访问代理加盟页面
        self.link.visit_link_partner()
        # 获取校验文字信息
        self.re_data = self.link.get_link_agent_course_1()
        try:
            self.assertEqual(self.re_data, "金字塔代理模式", self.output_verify_fail % ("金字塔代理模式", self.re_data))
            log1.info(self.output_verify_success % ("金字塔代理模式", self.re_data))
            self.link.save_window_snapshot('金字塔代理模式')
            log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
        except AssertionError as e:
            log1.error('Failure of test case execution! Reason: %s' % e + '\n')

    @BeautifulReport.add_test_img('test_end_navigation_011')
    def test_end_navigation_011(self):
        """访问金字塔代理教程相关页面"""
        self.case_name = '访问金字塔代理教程相关页面'
        log1.info("Executing use test case:%s" % self.case_name)
        # 访问金字塔代理教程页面
        self.link.visit_link_agent_course_2()
        for i in range(1, 11):
            agent_courses = data['links'].get('link_agent_course_3'.replace('1', str(i)))
            try:
                if i == 1:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何邀请注册帐号')
                    log1.info("如何邀请注册帐号")
                elif i == 2:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何进入代理中心')
                    log1.info("如何进入代理中心")
                elif i == 3:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何生成邀链接')
                    log1.info("如何生成邀链接")
                elif i == 4:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何管理邀链接')
                    log1.info("如何管理邀链接")
                elif i == 5:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何查看下级人数')
                    log1.info("如何查看下级人数")
                elif i == 6:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何查看下级列表')
                    log1.info("如何查看下级列表")
                elif i == 7:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何查看下级财务')
                    log1.info("如何查看下级财务")
                elif i == 8:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何查看代理受益')
                    log1.info("如何查看代理受益")
                elif i == 9:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何查看下级报表')
                    log1.info("如何查看下级报表")
                elif i == 10:
                    self.link.click(agent_courses)
                    self.link.save_window_snapshot('如何查看报表总汇')
                    log1.info("如何查看报表总汇")
                log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
            except AssertionError as e:
                log1.error('Failure of test case execution! Reason: %s' % e + '\n')

    @classmethod
    def tearDownClass(cls):
        cls.link = EndNavigation(cls.driver)
        cls.link.dr_quit()
