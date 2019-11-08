from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1


class GeneroPage(BasePage):
    data = get_yaml()
    link_genero_page = data['links'].get('link_genero_page')  # 金管家
    link_genero_interest_page = data['links'].get('link_genero_interest_page')  # 免息借呗
    link_genero_account_page = data['links'].get('link_genero_account_page')  # 账号交易
    link_genero_app_page = data['links'].get('link_genero_app_page')  # App下载
    link_genero_online_customer = data['links'].get('link_genero_online_customer')  # 在线客服页面
    link_genero_home_page = data['links'].get('link_genero_home_page')  # 官方首页
    assert_public_email_element = data['asserts'].get('assert_public_email_element')
    assert_public_en_element = data['asserts'].get('assert_public_en_element')
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')
    pop_genero_toast_text = data['pop_box'].get('pop_genero_toast_text')  # 弹出即消失的提示框
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')
    input_genero_search = data['inputs'].get('input_genero_search')
    btn_genero_search = data['buttons'].get('btn_genero_search')
    link_interestFree_loan = data['links'].get('link_interestFree_loan')
    link_interestFreeIn_live_genero = data['links'].get('link_interestFreeIn_live_genero')

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def visit_genero_page(self):
        """
        Visit the generos page
        :return:
        """
        self.open_new_window(self.link_genero_page)

    def visit_genero_interest_page(self):
        """
        Visit the generos interest page
        :return:
        """
        self.open_new_window(self.link_genero_interest_page)

    def visit_genero_account_page(self):
        """
        Visit the generos account page
        :return:
        """
        self.click(self.link_genero_account_page)

    def visit_genero_app_page(self):
        """
        Visit the generos app download page
        :return:
        """
        self.open_new_window(self.link_genero_app_page)

    def visit_genero_customer_page(self):
        """
        Visit the generos online customer page
        :return:
        """
        self.open_new_window(self.link_genero_online_customer)

    def visit_genero_home_page(self):
        """
        Visit the generos return home page
        :return:
        """
        self.open_new_window(self.link_genero_home_page)

    def visit_interest_free_loan(self):
        """
        Visit the interest-free lending page
        :return:
        """
        self.open_new_window(self.link_interestFree_loan)

    def visit_interest_video_genero(self):
        """访问视讯金管家"""
        self.open_new_window(self.link_interestFreeIn_live_genero)

    def get_genero_customer_cn(self):
        """
        Get description information of online customer service(Chinese Version)
        :return:
        """
        customer_text_cn = self.get_text(self.assert_public_email_element)
        return customer_text_cn

    def get_genero_customer_en(self):
        """
        Get description information of online customer service(English Version)
        :return:
        """
        customer_text_en = self.get_text(self.assert_public_en_element)
        return customer_text_en

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_public_waring_text)
        return war_text

    def click_close_warning(self):
        """
        Close the warning box
        :return:
        """
        self.click(self.pop_public_waring_close)

    def input_search_text(self, suc, username):
        """
        在额度查询输入框输入要查询的会员账号
        :param suc: 弹出提示框的描述信息
        :param username: 输入的会员账号信息
        :return: war_text，war_error
        """
        try:
            self.type(self.input_genero_search, username)
            self.click(self.btn_genero_search)
            self.forced_wait(1)
            if suc == '0':
                _toast_text = self.get_text(self.pop_genero_toast_text)
                return _toast_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)
