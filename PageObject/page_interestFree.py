from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1


class InterestFreePage(BasePage):
    data = get_yaml()
    link_interestFree_loan = data['links'].get('link_interestFree_loan')  # 免息借呗
    link_interestFreeIn_home_tab = data['links'].get('link_interestFreeIn_home_tab')  # 首页
    link_interestFreeIn_live_tab = data['links'].get('link_interestFreeIn_live_tab')  # 视讯额度
    link_interestFreeIn_chess_tab = data['links'].get('link_interestFreeIn_chess_tab')  # 棋牌额度
    link_interestFreeIn_lottery_tab = data['links'].get('link_interestFreeIn_lottery_tab')  # 彩票额度
    link_interestFreeIn_casino_tab = data['links'].get('link_interestFreeIn_casino_tab')  # 电子额度
    link_interestFreeIn_account_tab = data['links'].get('link_interestFreeIn_account_tab')  # 账号买卖
    link_interestFreeIn_records_tab = data['links'].get('link_interestFreeIn_records_tab')  # 借还款记录
    link_interestFreeIn_borrow_moeny = data['links'].get('link_interestFreeIn_borrow_moeny')  # 我要借款
    link_interestFreeIn_repay_moeny = data['links'].get('link_interestFreeIn_repay_moeny')  # 我要还款
    input_interestFreeIn_user = data['inputs'].get('input_interestFreeIn_user')  # 会员账号输入框
    input_interestFreeIn_jk_amount = data['inputs'].get('input_interestFreeIn_jk_amount')  # 输入框状态
    input_interestFreeIn_hk_amount = data['inputs'].get('input_interestFreeIn_hk_amount')  # 还款金额
    btn_interestFreeIn_search = data['buttons'].get('btn_interestFreeIn_search')  # 额度查询
    input_interestFreeIn_search = data['inputs'].get('input_interestFreeIn_search')  # 额度查询-会员账号
    link_interestFreeIn_live_but = data['links'].get('link_interestFreeIn_live_but')  # 视讯信用额度-立即查看
    link_interestFreeIn_chess_but = data['links'].get('link_interestFreeIn_chess_but')  # 棋牌信用额度-立即查看
    link_interestFreeIn_lottery_but = data['links'].get('link_interestFreeIn_lottery_but')  # 彩票信用额度-立即查看
    link_interestFreeIn_casino_but = data['links'].get('link_interestFreeIn_casino_but')  # 电子信用额度-立即查看、
    link_interestFreeIn_customer_tab = data['links'].get('link_interestFreeIn_customer_tab')  # 在线客服
    assert_public_email_element = data['asserts'].get('assert_public_email_element')
    assert_public_en_element = data['asserts'].get('assert_public_en_element')
    link_interestFreeIn_live_genero = data['links'].get('link_interestFreeIn_live_genero')  # 视讯金管家
    link_interestFreeIn_chess_genero = data['links'].get('link_interestFreeIn_chess_genero')  # 棋牌金管家
    link_interestFreeIn_lottery_genero = data['links'].get('link_interestFreeIn_lottery_genero')  # 彩票金管家
    link_interestFreeIn_casino_genero = data['links'].get('link_interestFreeIn_casino_genero')  # 电子金管家
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')  # 关闭警告提示框
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')  # 获取警告提示框信息
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网页公告
    pop_interestFreeIn_waring_text = data['pop_box'].get('pop_interestFreeIn_waring_text')
    pop_interestFreeIn_waring_close = data['pop_box'].get('pop_interestFreeIn_waring_close')

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def visit_interest_free_loan(self):
        """
        Visit the interest-free lending page
        :return:
        """
        self.open_new_window(self.link_interestFree_loan)

    def input_interestFree_search_text(self, suc, username):
        """
        Enter the member account to be queried in the quota inquiry input box.
        :param suc: 0
        :param username: Enter member account information
        :return: war_text，war_error
        """
        try:
            self.type(self.input_interestFreeIn_search, username)
            self.click(self.btn_interestFreeIn_search)
            self.forced_wait(1)
            if suc == '1':
                _war_text = self.get_text(self.pop_interestFreeIn_waring_text)
                self.click(self.pop_interestFreeIn_waring_close)
                return _war_text
            if suc == '0':
                _war_error = self.get_text(self.pop_interestFreeIn_waring_text)
                self.click(self.pop_interestFreeIn_waring_close)
                # log1.info(war_error)
                return _war_error
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_interest_video_genero(self):
        """访问视讯金管家"""
        self.open_new_window(self.link_interestFreeIn_live_genero)

    def visit_interest_chess_genero(self):
        """访问棋牌金管家"""
        self.open_new_window(self.link_interestFreeIn_chess_genero)

    def visit_interest_lottery_genero(self):
        """访问彩票金管家"""
        self.open_new_window(self.link_interestFreeIn_lottery_genero)

    def visit_interest_casino_genero(self):
        """访问电子金管家"""
        self.open_new_window(self.link_interestFreeIn_casino_genero)

    def visit_interest_video_page(self):
        """从立即查看访问视讯额度"""
        self.click(self.link_interestFreeIn_live_but)

    def visit_interest_chess_page(self):
        """从立即查看访问棋牌额度"""
        self.click(self.link_interestFreeIn_chess_but)

    def visit_interest_lottery_page(self):
        """从立即查看访问彩票额度"""
        self.click(self.link_interestFreeIn_lottery_but)

    def visit_interest_casino_page(self):
        """从立即查看访问电子额度"""
        self.click(self.link_interestFreeIn_casino_but)

    def visit_interest_home_page(self):
        """
        点击首页
        :return:
        """
        self.click(self.link_interestFreeIn_home_tab)

    def visit_interest_video_quota(self):
        """视讯额度"""
        self.click(self.link_interestFreeIn_live_tab)

    def visit_interest_chess_quota(self):
        """棋牌额度"""
        self.click(self.link_interestFreeIn_chess_tab)

    def visit_interest_lottery_quota(self):
        """彩票额度"""
        self.click(self.link_interestFreeIn_lottery_tab)

    def visit_interest_casino_quota(self):
        """电子额度"""
        self.click(self.link_interestFreeIn_casino_tab)

    def visit_interest_account_sale(self):
        """账号买卖"""
        self.click(self.link_interestFreeIn_account_tab)

    def visit_interest_records(self):
        """借还款记录"""
        self.click(self.link_interestFreeIn_records_tab)

    def visit_interest_customer(self):
        """在线客服"""
        self.open_new_window(self.link_interestFreeIn_customer_tab)


    def visit_interest_borrow_money(self):
        """我要借款"""
        self.click(self.link_interestFreeIn_borrow_moeny)

    def visit_interest_repay_money(self):
        """我要还款"""
        self.click(self.link_interestFreeIn_repay_moeny)

    def type_user_disabled(self):
        """判断输入框是否为disabled状态"""
        #type_user = self.find_element(self.input_interestFreeIn_user).is_enabled()
        type_user = self.get_enabled(self.input_interestFreeIn_user)
        return type_user

    def type_borrow_disabled(self):
        """判断输入框是否为disabled状态"""
        type_borrow =self.get_enabled(self.input_interestFreeIn_jk_amount)
        #type_borrow = self.find_element(self.input_interestFreeIn_jk_amount).is_enabled()
        return type_borrow

    def type_repay_disabled(self):
        """判断输入框是否为disabled状态"""
        #type_repay = self.find_element(self.input_interestFreeIn_hk_amount).is_enabled()
        type_repay = self.get_enabled(self.input_interestFreeIn_hk_amount)
        return type_repay

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

    def click_close_warning(self):
        """
        Close the warning box
        :return:
        """
        self.click(self.pop_public_waring_close)

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_public_waring_text)
        return war_text

    def click_interest_close_warning(self):
        """
        Close the warning box
        :return:
        """
        self.click(self.pop_interestFreeIn_waring_close)

    def get_interest_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_interestFreeIn_waring_text)
        return war_text
    # pop_interestFreeIn_waring_text = data['pop_box'].get('pop_interestFreeIn_waring_text')
    # pop_interestFreeIn_waring_close = data['pop_box'].get('pop_interestFreeIn_waring_close')