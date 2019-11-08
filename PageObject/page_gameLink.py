import os
import urllib.request

from aip import AipOcr
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Common.basePage import BasePage
from Common.getYaml import get_yaml
from Common.log import log1

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')


class GameLinkPage(BasePage):
    # 获取yaml文件内容
    data = get_yaml()

    link_game_move_sport = data['links'].get('link_game_move_sport')
    link_game_sport_hg = data['links'].get('link_game_sport_hg')
    link_game_sport_sb = data['links'].get('link_game_sport_sb')
    link_game_sport_bbin = data['links'].get('link_game_sport_bbin')
    link_game_sport_ag = data['links'].get('link_game_sport_ag')
    link_game_live = data['links'].get('link_game_live')
    link_game_live_ag_1 = data['links'].get('link_game_live_ag_1')
    link_game_live_ag = data['links'].get('link_game_live_ag')
    link_game_casino = data['links'].get('link_game_casino')  #
    link_game_start1 = data['links'].get('link_game_start1')  #
    input_game_casino_search = data['inputs'].get('input_game_casino_search')
    btn_game_casino_search = data['buttons'].get('btn_game_casino_search')
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')
    pop_public_waring_close_two = data['pop_box'].get('pop_public_waring_close_two')
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')
    link_game_move_chess = data['links'].get('link_game_move_chess')  # 棋牌游戏
    link_game_chess_ly = data['links'].get('link_game_chess_ly')  # 乐游棋牌
    link_game_chess_ky = data['links'].get('link_game_chess_ky')  # 开元棋牌
    link_game_chess_vg = data['links'].get('link_game_chess_vg')  # VG棋牌
    link_game_chess_fg = data['links'].get('link_game_chess_fg')  # FG棋牌
    link_game_chess_th = data['links'].get('link_game_chess_th')  # 天豪棋牌
    link_game_fish = data['links'].get('link_game_fish')  # 捕鱼达人
    link_game_fish_beauty = data['links'].get('link_game_fish_beauty')  # 捕鱼达人-美人捕鱼
    link_game_lottery = data['links'].get('link_game_lottery')  # 彩票游戏
    link_game_chess_1 = data['links'].get('link_game_chess_1')  #
    link_game_chess_2 = data['links'].get('link_game_chess_2')  #
    link_game_chess_3 = data['links'].get('link_game_chess_3')  #
    link_game_chess_4 = data['links'].get('link_game_chess_4')  #
    link_game_chess_5 = data['links'].get('link_game_chess_5')  #


    input_login_username = data['inputs'].get('input_login_username')
    input_login_password = data['inputs'].get('input_login_password')
    input_login_code = data['inputs'].get('input_login_code')
    btn_login = data['buttons'].get('btn_login')  # 登录按钮
    btn_code_login = data['buttons'].get('btn_code_login')  # 验证码登录按钮
    btn_login_code_image = data['buttons'].get('btn_login_code_image')  # 登录验证码

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def type_login_username(self, username):
        """
        登录方法，输入账号信息
        :param username:
        :return:
        """
        self.type(self.input_login_username, username)

    def type_login_password(self, password):
        """
        登录方法，输入密码
        :param password:
        :return:
        """
        self.type(self.input_login_password, password)

    def type_login_code(self, code):
        """
        验证码输入框
        :param code:
        :return:
        """
        self.type(self.input_login_code, code)

    def click_login_btn(self):
        """
        没有验证码的登录按钮
        :return:
        """
        self.click(self.btn_login)

    def click_code_login_btn(self):
        """
        存在验证码的登录按钮
        :return:
        """
        self.click(self.btn_code_login)

    # def get_toast_text(self):
    #     """
    #     弹出提示信息
    #     :return:
    #     """
    #     _toast_text = self.get_text(self.toast_text)
    #     return _toast_text

    def click_close_warning(self):
        """
        Close the warning box /html/body/div[4]/div[2]/div/div/a/i
        :return:/html/body/div[5]/div[2]/div/div/a/i
        """
        #self.click_action_esc()
        self.click(self.pop_public_waring_close)

    def get_war_text(self):
        """
        Get warning box information
        :return: war_text
        """
        war_text = self.get_text(self.pop_public_waring_text)
        return war_text

    def click_check_code_img(self):
        """
        点击验证码图标，刷新验证码
        :return:
        """
        self.click(self.btn_login_code_image)

    def find_type_login_code(self):
        """
        登录系统
        :param suc: 0
        :param username: yusheng
        :param password: 12345678
        :return:
        """
        try:
            notice_element = self.find_element(self.input_login_code)
            if self.get_displayed(notice_element):
                log1.info("teastt111111")
                # self.type(self.input_login_username, username)
                # self.type(self.input_login_password, password)
                img_str = self.driver.find_element_by_id('vPic')
                # log1.info(img_str)
                code_str = img_str.get_attribute('src')
                # log1.info(code_str)
                urllib.request.urlretrieve(code_str, code_path)
                APP_ID = '17161646'
                API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
                SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
                client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
                i = open(code_path, 'rb')
                img = i.read()
                msg = client.basicGeneral(img)
                # msg是一个字典，其中words_result中包含了文字信息
                for i in msg.get('words_result'):
                    print(i.get('words'))
                    self.code = i.get('words')
                self.type_login_code(self.code)
                self.click_code_login_btn()
                # self.click(self.btn_login)
                while self.get_war_text() == '请输入4位验证码' or self.get_war_text() == '验证码错误':
                    self.click_close_warning()
                    self.click_check_code_img()
                    img_str = self.driver.find_element_by_id('vPic')
                    # log1.info(img_str)
                    code_str = img_str.get_attribute('src')
                    # log1.info(code_str)
                    urllib.request.urlretrieve(code_str, code_path)
                    APP_ID = '17161646'
                    API_KEY = 'WYR9qe7GLUXRvEqr1Lb2Z0PD'
                    SECRET_KEY = 'B8GWc3unaUEIEA8r3KTe8pDex0kGqoyF'
                    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
                    i = open(code_path, 'rb')
                    img = i.read()
                    msg = client.basicGeneral(img)
                    # msg是一个字典，其中words_result中包含了文字信息
                    for i in msg.get('words_result'):
                        print(i.get('words'))
                        self.code = i.get('words')
                    self.type_login_code(self.code)
                    self.click_code_login_btn()
                    # self.click(self.btn_login)
        except Exception as e:
            log1.error('定位验证码元素失败，原因：界面不存在验证码-%s' % e)

    def visit_sport_hg_page(self, suc):
        """
        Start the HG game on the sport page without login
        :param suc: 0
        :return: _war_text
        """
        try:
            self.move_to_element(self.link_game_move_sport)
            self.forced_wait(1)
            self.click(self.link_game_sport_hg)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_sport_sb_page(self, suc):
        """
        Start the SB game on the sport page without login
        :param suc: 0
        :return: _war_text
        """
        try:
            self.move_to_element(self.link_game_move_sport)
            self.forced_wait(1)
            self.click(self.link_game_sport_sb)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_sport_bbin_page(self, suc):
        """
        Start the BBin game on the sport page without login
        :param suc: 0
        :return: _war_text
        """
        try:
            self.move_to_element(self.link_game_move_sport)
            self.forced_wait(1)
            self.click(self.link_game_sport_bbin)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_sport_ag_page(self, suc):
        """
        Start the AG game on the sport page without login
        :param suc: 0
        :return: _war_text
        """
        try:
            self.move_to_element(self.link_game_move_sport)
            self.forced_wait(1)
            self.click(self.link_game_sport_ag)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_game_live_ag_page(self, suc):
        """
        Start the AG game on the liveCasino page without login
        :param suc: 0
        :return: _war_text
        """
        try:
            self.click(self.link_game_live)
            self.forced_wait(1)
            self.click(self.link_game_live_ag)
            self.forced_wait(1)
            self.click_close_warning()
            # self.move_to_element(self.link_game_live)
            # self.forced_wait(1)
            # self.click(self.link_game_live_ag_1)
            # self.forced_wait(1)
            # self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_game_casino_page(self, suc, game_name):
        """
        Start the xxxx game on the casino page without login
        :param suc: 0
        :param game_name: 侠盗，游戏查询条件
        :return:  _war_text
        """
        try:
            self.click(self.link_game_casino)
            self.forced_wait(1)
            self.type(self.input_game_casino_search, game_name)
            self.forced_wait(1)
            self.click(self.btn_game_casino_search)
            self.forced_wait(1)
            self.js_scroll_end()
            self.forced_wait(1)
            self.click(self.link_game_start1)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_game_chess_ly(self, suc):
        """
        Start the ly game on the chess page without login
        :param suc:
        :return:
        """
        try:
            self.move_to_element(self.link_game_move_chess)
            self.forced_wait(1)
            self.click(self.link_game_chess_ly)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_game_chess_ky(self, suc):
        """
        Start the KY game on the chess page without login
        :param suc:
        :return:
        """
        try:
            self.move_to_element(self.link_game_move_chess)
            self.forced_wait(1)
            self.click(self.link_game_chess_ky)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_game_chess_vg(self, suc):
        """
        Start the VG game on the chess page without login
        :param suc:
        :return:
        """
        try:
            self.move_to_element(self.link_game_move_chess)
            self.forced_wait(1)
            self.click(self.link_game_chess_vg)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_game_chess_fg(self, suc):
        """
        Start the FG game on the chess page without login
        :param suc:
        :return:
        """
        try:
            self.move_to_element(self.link_game_move_chess)
            self.forced_wait(1)
            self.click(self.link_game_chess_fg)
            self.forced_wait(1)
            #self.click(self.link_game_start1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)

    def visit_game_chess_th(self, suc):
        """
        Start the TH game on the chess page without login
        :param suc:
        :return:
        """
        try:
            self.move_to_element(self.link_game_move_chess)
            self.forced_wait(1)
            self.click(self.link_game_chess_th)
            #self.click(self.link_game_start1)
            self.forced_wait(1)
            self.click_close_warning()
            if suc == '0':
                _war_text = self.get_text(self.pop_public_waring_text)
                return _war_text
        except BaseException as e:
            log1.error('Failure of test case execution! Reason：%s' % e)
