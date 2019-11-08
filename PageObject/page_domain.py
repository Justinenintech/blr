from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1

data = get_yaml()


class DomainPage(BasePage):

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网页公告
        # notice_element = self.find_element(pop_web_notice_close)
        if self.get_displayed(pop_web_notice_close):
            self.click(pop_web_notice_close)
        else:
            pass

    def visit_domain_detection_page(self):
        """
        线路检测
        :return:
        """

        click_line = data['links'].get('link_domain_detection_page')  # 线路检测
        self.open_new_window(click_line)

    # def visit_domain_list(self):
    #     link_domain_urls = data['links'].get('link_domain_urls')  # 线路检测
    #     link_domain_url = data['links'].get('link_domain_url')  # 线路检测
    #     #self.click_eles(link_domain_url, '//span')
    #     namelist = ['香港线路', '澳门线路', '大陆线路', '台湾线路', '美国线路','贵宾线路']
    #     for name in namelist:
    #         log1.info(name)
    #         self.click_eles(link_domain_url, '//a','//h2',name)

    # def visit_domain_lists(self):
    #     self.click_eles_i()

    def visit_domain_agent_courses(self):
        link_domain_agent_course = data['links'].get('link_domain_agent_course')  # 代理登录
        self.click(link_domain_agent_course)
        for i in range(1, 11):
            agent_courses = data['links'].get('link_domain_agent_course1'.replace('1', str(i)))
            try:
                if i == 1:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何邀请注册帐号')
                elif i == 2:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何进入代理中心')
                elif i == 3:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何生成邀链接')
                elif i == 4:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何管理邀链接')
                elif i == 5:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何查看下级人数')
                elif i == 6:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何查看下级列表')
                elif i == 7:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何查看下级财务')
                elif i == 8:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何查看代理受益')
                elif i == 9:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何查看下级报表')
                elif i == 10:
                    self.click(agent_courses)
                    self.save_window_snapshot('如何查看报表总汇')
            except BaseException as e:
                log1.error('Failure of test case execution! Reason：%s' % e)


    def visit_domain_lists(self,span_text):
        link_domain_url = data['links'].get('link_domain_url')
        counts = self.count_elements(link_domain_url, '//a')
        # log1.info(counts)
        lines = self.find_element(link_domain_url)
        eles = lines.find_elements_by_xpath('//a')
        spans = lines.find_elements_by_xpath('//h2')
        for i in range(counts):
            if spans[i].text == span_text:
                _url = eles[i].get_attribute("href")
                log1.info("_url：%s" % _url)
                eles[i].click()
                # self.forced_wait(5)
                # self.get_new_handle()
                self.forced_wait(5)
                open_url = self.driver.current_url
                log1.info("open_url：%s" % open_url)
                assert _url.split("/")[2] == open_url.split("/")[2], "进入官网站失败，网页中地址{%s}，打开的网站{%s}" % (
                    _url, open_url)
                log1.info("成功进入官网，打开的网站{%s}" % open_url)
                self.save_window_snapshot("线路检测：%s" % open_url)
                self.forced_wait(5)
                return _url,open_url

    def visit_domain_register(self):
        link_domain_register = data['links'].get('link_domain_register')
        self.click(link_domain_register)

    def visit_domain_customer(self):
        link_domain_customer = data['links'].get('link_domain_customer')
        self.click(link_domain_customer)

    def get_domain_customer_cn(self):
        """
        Get description information of online customer service(Chinese Version)
        :return:
        """
        assert_public_email_element = data['asserts'].get('assert_public_email_element')
        customer_text_cn = self.get_text(assert_public_email_element)
        return customer_text_cn

    def get_domain_customer_en(self):
        """
        Get description information of online customer service(English Version)
        :return:
        """
        assert_public_en_element = data['asserts'].get('assert_public_en_element')
        customer_text_en = self.get_text(assert_public_en_element)
        return customer_text_en

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')  # 获取警告提示框信息
        war_text = self.get_text(pop_public_waring_text)
        return war_text

    def visit_domain_on1(self):
        """
        线路1
        :return:
        """
        line_on1 = data['links'].get('link_domain_on1')  # 线路检测-1
        #self.click(line_on1)
        self.open_new_window(line_on1)

    def visit_domain_on2(self):
        """
        线路2
        :return:
        """
        line_on2 = data['links'].get('link_domain_on2')  # 线路检测-2
        self.open_new_window(line_on2)

    def visit_domain_on3(self):
        """
        线路3
        :return:
        """
        line_on3 = data['links'].get('link_domain_on3')  # 线路检测-3
        self.open_new_window(line_on3)

    def visit_domain_on4(self):
        """
        线路4
        :return:
        """
        line_on4 = data['links'].get('link_domain_on4')  # 线路检测-4

        self.open_new_window(line_on4)

    def visit_domain_on5(self):
        """
        线路5
        :return:
        """
        line_on5 = data['links'].get('link_domain_on5')  # 线路检测-5
        self.open_new_window(line_on5)

    def visit_domain_on6(self):
        """
        线路6
        :return:
        """
        line_on6 = data['links'].get('link_domain_on6')  # 线路检测-6
        self.open_new_window(line_on6)
        # def get_line_url(self):

    #     """获取当前所有线路检测的url地址"""
    #     line_urlss = self.find_element(self.line_urls)
    #     line_urlss

    # def input_search_text(self,suc,username):
    #     """
    #     在额度查询输入框输入要查询的会员账号
    #     :param suc: 弹出提示框的描述信息
    #     :param username: 输入的会员账号信息
    #     :return: war_text，war_error
    #     """
    #     try:
    #         self.type(self.ipu_username,username)
    #         self.click(self.click_search)
    #         self.my_sleep(1)
    #         if suc == '1':
    #             war_text = self.get_text(self.warning_texts)
    #             self.click(self.close_warning)
    #             log1.info(war_text)
    #             return war_text
    #         if suc == '0':
    #             war_error = self.get_text(self.warning_texts)
    #             self.click(self.close_warning)
    #             log1.info(war_error)
    #             return war_error
    #     except Exception as e:
    #         log1.error('用例执行失败，原因：%s' %e)

    def visit_domain_vip_club(self):
        """
        访问太阳城贵宾会
        :return:
        """
        vip_club = data['links'].get('link_domain_vip_club')  # 太阳城贵宾会
        self.click(vip_club)

    def visit_domain_phone_login(self):
        """
        访问手机下载页面
        :return:
        """
        phone_login = data['links'].get('link_domain_app_download')  # 手机端下载
        self.click(phone_login)

    def visit_domain_browser_down(self):
        """
        访问资讯端下载页面
        :return:
        """
        browser_down = data['links'].get('link_domain_browser_download')  # 浏览器下载
        self.click(browser_down)

    def visit_domain_agent_login(self):
        """
        访问代理登录页面
        :return:
        """
        agent_login = data['links'].get('link_domain_agent_pattern')
        self.click(agent_login)

    def visit_domain_customer(self):
        """
        访问在线客服
        :return:
        """
        online_ser = data['links'].get('link_domain_customer')  # 在线客服页面
        self.click(online_ser)

    def visit_domain_pretreatment(self):
        """
        访问优惠办理页面
        :return:
        """
        pre_treatment = data['links'].get('link_domain_preferential')  # 访问优惠办理页面
        self.click(pre_treatment)