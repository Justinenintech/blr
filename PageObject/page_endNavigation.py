import os

from Common.basePage import BasePage
from Common.getYaml import get_yaml
import urllib.request
from Common.log import log1
from aip import AipOcr
d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'img',
                 'code')
code_path = os.path.join(os.path.abspath(d)+'/test_code.jpg')

data = get_yaml()


class EndNavigation(BasePage):
    data = get_yaml()
    pop_public_waring_close = data['pop_box'].get('pop_public_waring_close')
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网站公告
    pop_public_waring_text = data['pop_box'].get('pop_public_waring_text')  # 获取警告提示框信息
    pop_register_war_text = data['pop_box'].get('pop_register_war_text')

    link_about_us = data['links'].get('link_about_us')  # 关于我们
    link_contact_us = data['links'].get('link_contact_us')  # 联系我们
    link_deposit_help = data['links'].get('link_deposit_help')  # 存款帮助
    link_withdrawal_help = data['links'].get('link_withdrawal_help')  # 取款帮助
    link_common_problem = data['links'].get('link_common_problem')  # 常见问题

    link_partner = data['links'].get('link_partner') # 代理加盟
    link_agent_course_1 = data['links'].get('link_agent_course_1') # 代理模式
    link_agent_course_2 = data['links'].get('link_agent_course_2') # 代理教程
    link_responsible_betting = data['links'].get('link_responsible_betting')

    assert_about_us_el = data['asserts'].get('assert_about_us_el')  # 关于我们
    assert_contact_us_el = data['asserts'].get('assert_contact_us_el')  # 联系我们
    assert_deposit_help_el = data['asserts'].get('assert_deposit_help_el')  # 存款帮助
    assert_withdrawal_help_el = data['asserts'].get('assert_withdrawal_help_el')  # 取款帮助
    assert_questions1 = data['asserts'].get('assert_questions1')  #常见问题-一帮常见问题
    assert_questions2 = data['asserts'].get('assert_questions2')  #常见问题-游戏及投注问题

    assert_common_problem_el1 = data['asserts'].get('assert_common_problem_el1')  #常见问题-一帮常见问题
    assert_common_problem_el2 = data['asserts'].get('assert_common_problem_el2')  #常见问题-游戏及投注问题
    assert_common_problem_el3 = data['asserts'].get('assert_common_problem_el3')  #技术常见问题
    assert_responsible_betting_el = data['asserts'].get('assert_responsible_betting_el')
    assert_rules_terms_el = data['asserts'].get('assert_rules_terms_el')
    assert_responsible_betting_el1 = data['asserts'].get('assert_responsible_betting_el1')
    assert_responsible_betting_el2 = data['asserts'].get('assert_responsible_betting_el2')

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def visit_link_about_us(self):
        """
        访问关于我们页面
        :return:
        """
        self.click(self.link_about_us)

    def get_about_us(self):
        """
        获取关于我们校验文字
        :return:
        """
        p_text = self.get_text(self.assert_about_us_el)
        return p_text

    def visit_link_contact_us(self):
        """
        访问联系我们页面
        :return:
        """
        self.click(self.link_contact_us)

    def get_contact_us(self):
        """
        获取联系我们校验文字
        :return:
        """
        p_text = self.get_text(self.assert_contact_us_el)
        return p_text

    def visit_link_deposit_help(self):
        """
        访问存款帮助页面
        :return:
        """
        self.click(self.link_deposit_help)

    def get_deposit_help(self):
        """
        获取存款帮助校验文字
        :return:
        """
        p_text = self.get_text(self.assert_deposit_help_el)
        return p_text

    def visit_link_withdrawal_help(self):
        """
        访问取款帮助页面
        :return:
        """
        self.click(self.link_withdrawal_help)

    def get_withdrawal_help(self):
        """
        获取取款帮助校验文字
        :return:
        """
        p_text = self.get_text(self.assert_withdrawal_help_el)
        return p_text

    def visit_link_common_problem(self):
        """
        访问常见问题页面-默认一般常见问题
        :return:
        """
        self.click(self.link_common_problem)

    def get_questions1(self):
        """
        获取一般常见问题校验文字
        :return:
        """
        p_text = self.get_text(self.assert_common_problem_el1)
        return p_text

    def visit_tab_questions_2(self):
        """
        访问常见问题页面-游戏及投注问题
        :return:
        """
        self.click(self.assert_common_problem_el2)

    def get_questions2(self):
        """
        获取游戏及投注问题校验文字
        :return:
        """
        p_text = self.get_text(self.assert_common_problem_el2)
        return p_text

    def visit_tab_questions_3(self):
        """
        访问常见问题页面-技术常见问题
        :return:
        """
        self.click(self.assert_common_problem_el3)

    def get_questions3(self):
        """
        获取技术常见问题校验文字
        :return:
        """
        p_text = self.get_text(self.assert_common_problem_el3)
        return p_text

    def visit_link_partner(self):
        """
        访问代理加盟页面
        :return:
        """
        self.click(self.link_partner)

    def get_link_agent_course_1(self):
        """
        获取代理模式的校验文字
        :return:
        """
        p_text = self.get_text(self.link_agent_course_1)
        return p_text

    def visit_link_agent_course_2(self):
        """
        访问代理教程
        :return:
        """
        self.click(self.link_agent_course_2)

    def visit_link_responsible_betting(self):
        """
        访问责任博彩页面
        :return:
        """
        self.click(self.link_responsible_betting)

    def get_responsible_betting_el1(self):
        """
        获取代理模式的校验文字
        :return:
        """
        p_text = self.get_text(self.assert_responsible_betting_el1)
        return p_text

    def visit_responsible_betting_el2(self):
        """
        访问责任博彩页面-条款与规则
        :return:
        """
        self.click(self.assert_responsible_betting_el2)

    def get_responsible_betting_el2(self):
        """
        获取代理模式的校验文字
        :return:
        """
        p_text = self.get_text(self.assert_responsible_betting_el2)
        return p_text