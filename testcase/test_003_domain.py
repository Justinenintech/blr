# # -*- coding: UTF-8 -*-
# import os
# import unittest
#
# import ddt
# import yaml
#
# from Common.basePage import BasePage
# from Common.getTestData import get_test_data
# from Common.getYaml import get_yaml
#
# from Common.log import log1
# from BeautifulReport import BeautifulReport
#
# from PageObject.page_domain import DomainPage
#
# case_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'data',
#                          'excels', 'case_data.xlsx')
# case_data = get_test_data(case_path, 4)
#
#
#
# @ddt.ddt
# class TestDomain(unittest.TestCase):
#     d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
#                      'error_img')
#     abspath = os.path.abspath(d)
#     """ 测试报告的基础用例Sample """
#     driver = None
#     img_path = abspath
#
#     data = get_yaml()
#     assert_public_home_title = data['asserts'].get('assert_public_home_title')
#     assert_public_customer_en = data['asserts'].get('assert_public_customer_en')
#     assert_public_customer_cn = data['asserts'].get('assert_public_customer_cn')
#     assert_public_en_title = data['asserts'].get('assert_public_en_title')
#     assert_public_email_title = data['asserts'].get('assert_public_email_title')  # 在线客服-投诉邮箱账号
#     assert_public_domain_title = data['asserts'].get('assert_public_domain_title')  # 澳门新葡京集团 - 导航站
#     output_verify_fail = data['outputs'].get('output_verify_fail')
#     output_verify_success = data['outputs'].get('output_verify_success')
#     link_domain_url = data['links'].get('link_domain_url')
#     link_domain_urls = data['links'].get('link_domain_urls')
#
#     def save_img(self, img_name):
#         """
#         传入一个img_name, 并存储到默认的文件路径下
#         :param img_name:
#         :return:
#         """
#         self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.abspath(self.img_path), img_name))
#
#     @classmethod
#     def setUpClass(cls):
#         browser = BasePage(cls)
#         cls.driver = browser.open_browser()
#
#     def setUp(self):
#         self.link = DomainPage(self.driver)
#
#     # @classmethod
#     # def tearDown(cls):
#     #     cls.link = TopLinkPage(cls.driver)
#     #     cls.link.dr_quit()
#
#     @classmethod
#     def tearDownClass(cls):
#         cls.link = DomainPage(cls.driver)
#         cls.link.dr_quit()
#
#     @BeautifulReport.add_test_img('test_line_sense_001')
#     def test_line_sense_001(self):
#         """未登录情况下，访问线路检测"""
#         self.case_name = '未登录情况下，访问线路检测'
#         log1.info("Executing use test case：%s" % self.case_name)
#         # 判断是否存在网站公告，如果存在则关闭公告提示！
#         self.link.find_click_notice()
#         # 访问线路检测页面，并且获取新打开窗口的句柄
#         self.link.visit_domain_detection_page()
#         #self.link.get_new_handle()
#         # 获取当前句柄的title
#         self._title = self.link.get_title()
#         try:
#             # 校验预期结果与实际结果是否一致
#             self.assertEqual(self._title, self.assert_public_domain_title, self.output_verify_fail % (
#                 self.assert_public_domain_title, self._title))
#             # 将结果输出到日志
#             log1.info(self.output_verify_success % (
#                 self.assert_public_domain_title, self._title))
#             # 保存截图
#             self.link.save_window_snapshot(self.case_name)
#             log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
#         except AssertionError as e:
#             log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#             raise
#
#     @BeautifulReport.add_test_img('test_line_sense_002')
#     def test_line_sense_002(self):
#         """未登录情况下，在线路检测页面，分别访问5个官方网站"""
#         self.case_name = '未登录情况下，在线路检测页面，分别访问5个官方网站'
#         log1.info("Executing use test case：%s" % self.case_name)
#         try:
#             # 访问5个官方网站
#             namelist = ['blr33888.com', 'blr33888.com', 'blr33888.com', 'blr33888.com', 'blr33888.com', 'blr33888.com','blr33888.com','blr33888.com','blr33888.com']
#             for name in namelist:
#                 self.link.visit_domain_lists(name)
#                 #self.link.get_new_handle()
#                 self.link.forced_wait(5)
#                 self.link.close_browser()
#                 self.link.forced_wait(5)
#                 self.link.switch_to_window_by_title('澳门威尼斯人娱乐城—老品牌值得信赖')
#                 self.link.forced_wait(5)
#                 #self.link.get_new_handle()
#                 self.link.visit_domain_detection_page()
#             log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
#         except AssertionError as e:
#             log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#             raise
#     #
#     # @BeautifulReport.add_test_img('test_line_sense_003')
#     # def test_line_sense_003(self):
#     #     """未登录情况下，在线路检测页面，访问立即注册页面"""
#     #     self.case_name = '未登录情况下，在线路检测页面，访问{立即注册}页面'
#     #     log1.info("Executing use test case：%s" % self.case_name)
#     #     self.link.visit_domain_register()
#     #     # 获取新打开窗口的句柄
#     #     self.link.get_new_handle()
#     #     # 获取当前句柄的title
#     #     self._title = self.link.get_title()
#     #     try:
#     #         # 校验预期结果与实际结果是否一致
#     #         self.assertEqual(self._title, self.assert_public_home_title, self.output_verify_fail % (
#     #             self.assert_public_home_title, self._title))
#     #         # 将结果输出到日志
#     #         log1.info(self.output_verify_success % (
#     #             self.assert_public_home_title, self._title))
#     #         # 保存截图
#     #         self.link.save_window_snapshot(self.case_name)
#     #         # 关闭当前浏览器窗口
#     #         self.link.close_browser()
#     #         # 获取首页句柄
#     #         self.link.switch_to_window_by_title('澳门威尼斯人-网投领导者-官方线路备用网!')
#     #         log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
#     #     except AssertionError as e:
#     #         log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#     #         raise
#     #
#     # @BeautifulReport.add_test_img('test_line_sense_004')
#     # def test_line_sense_004(self):
#     #     """未登录情况下，在线路检测页面，访问{在线客服}页面"""
#     #     self.case_name = '未登录情况下，在线路检测页面，访问{在线客服}页面'
#     #     log1.info("Executing use test case：%s" % self.case_name)
#     #     self.link.forced_wait(1)
#     #     # 访问在线客服页面
#     #     self.link.visit_domain_customer()
#     #     # 获取新打开窗口的句柄
#     #     self.link.get_new_handle()
#     #     # 获取当前句柄的title
#     #     self._title = self.link.get_title()
#     #     try:
#     #         if self._title == self.assert_public_customer_cn:
#     #             self.email = self.link.get_domain_customer_cn()
#     #             # 校验预期结果与实际结果是否一致
#     #             self.assertEqual(self.email, self.assert_public_email_title, self.output_verify_fail % (
#     #                 self.assert_public_email_title, self.email))
#     #             # 将结果输出到日志
#     #             log1.info(self.output_verify_success % (
#     #                 self.assert_public_email_title, self.email))
#     #             # 保存截图
#     #             self.link.save_window_snapshot(self.case_name)
#     #             # 关闭当前浏览器窗口
#     #             self.link.close_browser()
#     #             # 获取首页句柄
#     #             self.link.switch_to_window_by_title('澳门威尼斯人-网投领导者-官方线路备用网!')
#     #             log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
#     #         if self._title == self.assert_public_customer_en:
#     #             # 校验预期结果与实际结果是否一致
#     #             self.assertEqual(self._title, self.assert_public_customer_en, self.output_verify_fail % (
#     #                 self.assert_public_customer_en, self._title))
#     #             # 将结果输出到日志
#     #             log1.info(self.output_verify_success % (
#     #                 self.assert_public_customer_en, self._title))
#     #             # 保存截图
#     #             self.link.save_window_snapshot(self.case_name)
#     #             # 关闭当前浏览器窗口
#     #             self.link.close_browser()
#     #             # 获取首页句柄
#     #             self.link.switch_to_window_by_title('澳门威尼斯人-网投领导者-官方线路备用网!')
#     #             log1.info("Successful execution of test cases：%s" % self.case_name + '\n')
#     #     except AssertionError as e:
#     #         log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#     #         raise
#     #
#     # @BeautifulReport.add_test_img('test_line_sense_002')
#     # def test_line_sense_002(self):
#     #     """未登录情况下，访问线路检测"""
#     #     self.case_name = '未登录情况下，在线路检测页面，访问6个域名'
#     #     log1.info("Executing use test case:%s" % self.case_name)
#     #    # lines = self.driver.find_element_by_id('ttcesu')
#     #     #self.link.visit_domain_list()
#     #     counts = self.link.count_elements(self.link_domain_url,'//a')
#     #     # log1.info(counts)
#     #     lines = self.link.find_element(self.link_domain_url)
#     #     urls = lines.find_elements_by_xpath('//a')
#     #     # log1.info(len(urls))
#     #     # #self.driver.find_elements_by_tag_name()
#     #     # #urls = lines.find_elements_by_xpath('//a')
#     #     # # text_name = self.driver.find_element_by_xpath('/html/body/div[3]/ul/div[1]/li[3]/a/h2')
#     #     # # log1.info(text_name.text)
#     #     spans = lines.find_elements_by_xpath('//h2')
#     #     # log1.info(len(spans))
#     #     #self.link.find_element('id','ttcesu')
#     #     #lines.c
#     #     try:
#     #         #self.link.visit_domain_list()
#     #         for i in range(counts):
#     #             if spans[i].text == '香港线路':
#     #                 _url = eles[i].get_attribute("href")
#     #                 log1.info("_url：%s" % _url)
#     #                 eles[i].click()
#     #                 # self.forced_wait(5)
#     #                 # self.get_new_handle()
#     #                 # self.forced_wait(5)
#     #                 open_url = self.driver.current_url
#     #                 log1.info("open_url：%s" % open_url)
#     #                 assert _url.split("/")[2] == open_url.split("/")[2], "进入官网站失败，网页中地址{%s}，打开的网站{%s}" % (
#     #                 _url, open_url)
#     #                 log1.info("成功进入官网，打开的网站{%s}" % open_url)
#     #                 self.save_window_snapshot("线路检测：%s" % open_url)
#     #                 self.forced_wait(5)
#     #                 break
#     #         # for span in spans:
#     #         #     for url in urls:
#     #         #         line_url = url.get_attribute("href")
#     #         #         log1.info("%s：%s" % (span.text,line_url))
#     #             # for span in spans:
#     #             #     class_value = span.get_attribute("span")
#     #             #     log1.info(class_value)
#     #             #     line_url = url.get_attribute("href")
#     #             #     log1.info(line_url)
#     #             # class_value = url.get_attribute("span")
#     #             # log1.info(class_value)
#     #             # # print(class_value)
#     #             # if class_value == '1':
#     #             #     line_url = url.get_attribute("href")
#     #             #     log1.info(line_url)
#     #             #     self.link.visit_domain_on1()
#     #             #     open_line_url = self.driver.current_url
#     #             #     log1.info(open_line_url)
#     #             #     self.link.forced_wait(2)
#     #             #     if line_url.split("/")[2] == open_line_url.split("/")[2]:
#     #             #         self.link.save_window_snapshot(open_line_url.split("/")[2])
#     #             #         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#     #             #     else:
#     #             #         log1.info("Failure of test case execution:%s" % self.case_name + '\n')
#     #             #     self.close_browser()
#     #             #     self.switch_to_window_by_title('澳门威尼斯人娱乐城—老品牌值得信赖')
#     #             # elif class_value == '2':
#     #             #     line_url = url.get_attribute("href")
#     #             #     log1.info(line_url)
#     #             #     self.link.visit_domain_on2()
#     #             #     open_line_url = self.driver.current_url
#     #             #     log1.info(open_line_url)
#     #             #     self.link.forced_wait(2)
#     #             #     if line_url.split("/")[2] == open_line_url.split("/")[2]:
#     #             #         self.link.save_window_snapshot(open_line_url.split("/")[2])
#     #             #         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#     #             #     else:
#     #             #         log1.info("Failure of test case execution:%s" % self.case_name + '\n')
#     #             #     self.close_browser()
#     #             #     self.switch_to_window_by_title('澳门威尼斯人娱乐城—老品牌值得信赖')
#     #             # elif class_value == '3':
#     #             #     line_url = url.get_attribute("href")
#     #             #     log1.info(line_url)
#     #             #     self.link.visit_domain_on3()
#     #             #     open_line_url = self.driver.current_url
#     #             #     log1.info(open_line_url)
#     #             #     self.link.forced_wait(2)
#     #             #     if line_url.split("/")[2] == open_line_url.split("/")[2]:
#     #             #         self.link.save_window_snapshot(open_line_url.split("/")[2])
#     #             #         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#     #             #     else:
#     #             #         log1.info("Failure of test case execution:%s" % self.case_name + '\n')
#     #             #     self.close_browser()
#     #             #     self.switch_to_window_by_title('澳门威尼斯人娱乐城—老品牌值得信赖')
#     #             # elif class_value == '4':
#     #             #     line_url = url.get_attribute("href")
#     #             #     log1.info(line_url)
#     #             #     self.link.visit_domain_on4()
#     #             #     open_line_url = self.driver.current_url
#     #             #     log1.info(open_line_url)
#     #             #     self.link.forced_wait(2)
#     #             #     if line_url.split("/")[2] == open_line_url.split("/")[2]:
#     #             #         self.link.save_window_snapshot(open_line_url.split("/")[2])
#     #             #         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#     #             #     else:
#     #             #         log1.info("Failure of test case execution:%s" % self.case_name + '\n')
#     #             #     self.close_browser()
#     #             #     self.switch_to_window_by_title('澳门威尼斯人娱乐城—老品牌值得信赖')
#     #             # elif class_value == '5':
#     #             #     line_url = url.get_attribute("href")
#     #             #     log1.info(line_url)
#     #             #     self.link.visit_domain_on5()
#     #             #     open_line_url = self.driver.current_url
#     #             #     log1.info(open_line_url)
#     #             #     self.link.forced_wait(2)
#     #             #     if line_url.split("/")[2] == open_line_url.split("/")[2]:
#     #             #         self.link.save_window_snapshot(open_line_url.split("/")[2])
#     #             #         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#     #             #     else:
#     #             #         log1.info("Failure of test case execution:%s" % self.case_name + '\n')
#     #             #     self.close_browser()
#     #             #     self.switch_to_window_by_title('澳门威尼斯人娱乐城—老品牌值得信赖')
#     #             # elif class_value == '6':
#     #             #     line_url = url.get_attribute("href")
#     #             #     log1.info(line_url)
#     #             #     self.link.visit_domain_on6()
#     #             #     self.switch_to_window_by_title('澳门威尼斯人娱乐城—老品牌值得信赖')
#     #     except AssertionError as e:
#     #         log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#     #         raise
#
#     @BeautifulReport.add_test_img('test_line_sense_003')
#     def test_line_sense_003(self):
#         """未登录情况下，在线路检测页面访问太阳城贵宾会页面"""
#         self.case_name = '未登录情况下，在线路检测页面访问太阳城贵宾会'
#         log1.info("Executing use test case:%s" % self.case_name)
#         # try:
#         lines = self.driver.find_element_by_class_name('lay_4')
#         class_li = lines.find_elements_by_xpath('//li')
#         for lis in class_li:
#             class_value = lis.get_attribute("class")
#             # log1.info(class_value)
#             if class_value == 'cc1':
#                 url = lis.find_element_by_tag_name('a')
#                 href_value = url.get_attribute("href")
#                 self.link.visit_domain_vip_club()
#                 win = self.link.get_handle()
#                 self.link.chage_handle(win)
#                 open_url = self.driver.current_url
#                 log1.info(open_url)
#                 log1.info(href_value)
#                 try:
#                     self.assertEqual(open_url.split("/")[2], href_value.split("/")[2])
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#                 except AssertionError as e:
#                     log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#                 break
#
#     @BeautifulReport.add_test_img('test_line_sense_004')
#     def test_line_sense_004(self):
#         """未登录情况下，在线路检测页面访问手机下载页面"""
#         self.case_name = '未登录情况下，在线路检测页面访问手机下载页面'
#         log1.info("Executing use test case:%s" % self.case_name)
#         # try:
#         lines = self.driver.find_element_by_class_name('lay_4')
#         class_li = lines.find_elements_by_xpath('//li')
#         for lis in class_li:
#             class_value = lis.get_attribute("class")
#             # log1.info(class_value)
#             if class_value == 'cc2':
#                 url = lis.find_element_by_tag_name('a')
#                 href_value = url.get_attribute("href")
#                 self.link.visit_domain_phone_login()
#                 win = self.link.get_handle()
#                 self.link.chage_handle(win)
#                 open_url = self.driver.current_url
#                 log1.info(open_url)
#                 log1.info(href_value)
#                 try:
#                     self.assertEqual(open_url.split("/")[2], href_value.split("/")[2])
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#                 except AssertionError as e:
#                     log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     self.skipTest('test_line_sense_004 -Error: The use case has not been completed!!')
#                 break
#
#     @BeautifulReport.add_test_img('test_line_sense_005')
#     def test_line_sense_005(self):
#         """未登录情况下，在线路检测页面访问资讯端下载页面"""
#         self.case_name = '未登录情况下，在线路检测页面访问资讯端下载页面'
#         log1.info("Executing use test case:%s" % self.case_name)
#         # try:
#         lines = self.driver.find_element_by_class_name('lay_4')
#         class_li = lines.find_elements_by_xpath('//li')
#         for lis in class_li:
#             class_value = lis.get_attribute("class")
#             # log1.info(class_value)
#             if class_value == 'cc3':
#                 url = lis.find_element_by_tag_name('a')
#                 href_value = url.get_attribute("href")
#                 self.link.visit_domain_browser_down()
#                 win = self.link.get_handle()
#                 self.link.chage_handle(win)
#                 open_url = self.driver.current_url
#                 log1.info(open_url)
#                 log1.info(href_value)
#                 try:
#                     self.assertEqual(open_url.split("/")[2], href_value.split("/")[2])
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#                 except AssertionError as e:
#                     log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     self.skipTest('test_line_sense_005 -Error: The use case has not been completed!!')
#                 break
#
#     @BeautifulReport.add_test_img('test_line_sense_006')
#     def test_line_sense_006(self):
#         """未登录情况下，在线路检测页面访问代理模式页面"""
#         self.case_name = '未登录情况下，在线路检测页面访问代理模式页面'
#         log1.info("Executing use test case:%s" % self.case_name)
#         # try:
#         lines = self.driver.find_element_by_class_name('lay_4')
#         class_li = lines.find_elements_by_xpath('//li')
#         for lis in class_li:
#             class_value = lis.get_attribute("class")
#             # log1.info(class_value)
#             if class_value == 'cc4':
#                 url = lis.find_element_by_tag_name('a')
#                 href_value = url.get_attribute("href")
#                 self.link.visit_domain_agent_login()
#                 win = self.link.get_handle()
#                 self.link.chage_handle(win)
#                 open_url = self.driver.current_url
#                 log1.info(open_url)
#                 log1.info(href_value)
#                 try:
#                     self.assertEqual(open_url, href_value)
#                     self.link.get_img('金字塔代理模式')
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#                 except AssertionError as e:
#                     log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     self.skipTest('test_line_sense_006 -Error: The use case has not been completed!!')
#                 break
#
#     @BeautifulReport.add_test_img('test_line_sense_007')
#     def test_line_sense_007(self):
#         """未登录情况下，在线路检测页面访问金字塔代理教程相关页面"""
#         self.case_name = '未登录情况下，在线路检测页面访问金字塔代理教程相关页面'
#         log1.info("Executing use test case:%s" % self.case_name)
#         self.link.visit_domain_agent_login()
#         win = self.link.get_handle()
#         self.link.chage_handle(win)
#         self.link.visit_domain_agent_courses()
#         self.driver.close()
#         self.driver.switch_to.window(win)
#         # self.link.get_img(textss)
#         log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#
#     @BeautifulReport.add_test_img('test_line_sense_008')
#     def test_line_sense_008(self):
#         """未登录情况下，在线路检测页面访问在线客服页面"""
#         self.case_name = '未登录情况下，在线路检测页面访问在线客服页面'
#         log1.info("执行测试用例：%s" % self.case_name)
#         self.link.visit_domain_customer()
#         win = self.link.get_handle()
#         self.link.chage_handle(win)
#         _title = self.link.get_title()
#         try:
#             if _title == self.assert_public_customer_cn:
#                 # log1.info(self.assert_public_customer_cn)
#                 email = self.link.get_domain_customer_cn()
#                 self.assertEqual(email, self.assert_public_email_title)
#                 self.driver.close()
#                 self.driver.switch_to.window(win)
#                 log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#             elif _title == self.assert_public_customer_en:
#                 self.assertEqual(_title, self.assert_public_customer_en)
#                 self.driver.close()
#                 self.driver.switch_to.window(win)
#                 log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#         except AssertionError as e:
#             log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#             self.driver.close()
#             self.driver.switch_to.window(win)
#             self.skipTest('test_line_sense_008 -Error: The use case has not been completed!!')
#
#     @BeautifulReport.add_test_img('test_line_sense_009')
#     def test_line_sense_009(self):
#         """未登录情况下，在线路检测页面访问优惠办理页面"""
#         self.case_name = '未登录情况下，在线路检测页面访问优惠办理页面'
#         log1.info("Executing use test case:%s" % self.case_name)
#         # try:
#         lines = self.driver.find_element_by_class_name('lay_4')
#         class_li = lines.find_elements_by_xpath('//li')
#         for lis in class_li:
#             class_value = lis.get_attribute("class")
#             # log1.info(class_value)
#             if class_value == 'cc6':
#                 url = lis.find_element_by_tag_name('a')
#                 href_value = url.get_attribute("href")
#                 self.link.visit_domain_pretreatment()
#                 win = self.link.get_handle()
#                 self.link.chage_handle(win)
#                 open_url = self.driver.current_url
#                 log1.info(open_url)
#                 log1.info(href_value)
#                 try:
#                     self.assertEqual(open_url, href_value)
#                     self.link.get_img('优惠办理页面')
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     log1.info("Successful execution of test cases:%s" % self.case_name + '\n')
#                 except AssertionError as e:
#                     log1.error('Failure of test case execution! Reason: %s' % e + '\n')
#                     self.driver.close()
#                     self.driver.switch_to.window(win)
#                     self.skipTest('test_line_sense_009 -Error: The use case has not been completed!!')
#                 break
