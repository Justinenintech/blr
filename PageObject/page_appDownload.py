from Common.basePage import BasePage
from Common.getYaml import get_yaml


class AppDownloadPage(BasePage):
    data = get_yaml()
    link_app_download = data['links'].get('link_app_download')  # APP下载页面
    link_app_ios_help = data['links'].get('link_app_ios_help')  # 打开ios安装教程
    link_app_return_pc = data['links'].get('link_app_return_pc')  # 访问网站首页
    link_float_app = data['links'].get('link_float_app')  # APP下载
    pop_web_notice_close = data['pop_box'].get('pop_web_notice_close')  # 关闭网站公告
    btn_app_iosHelp_close = data['buttons'].get('btn_app_iosHelp_close')  # 关闭ios安装教程
    assert_app_iosHelp_element = data['asserts'].get('assert_app_iosHelp_element')  # 获取ios教程title

    def find_click_notice(self):
        """
        Closing website notice
        :return:
        """
        if self.get_enabled(self.pop_web_notice_close):
            self.click(self.pop_web_notice_close)
        else:
            pass

    def visit_app_download_page(self):
        """
        Visit the app download page
        :return:
        """
        self.open_new_window(self.link_float_app)


    def visit_ios_help_page(self):
        """
        Visit the ios help page
        :return:
        """
        self.click(self.link_app_ios_help)

    def click_ios_help_close(self):
        """
        Close the ios help
        :return:
        """
        self.click(self.btn_app_iosHelp_close)

    def visit_pc_home_page(self):
        """
        Visit the pc home page
        :return:
        """
        self.open_new_window(self.link_app_return_pc)

    def get_ios_help_title(self):
        """
        Get title of ios help
        :return:
        """
        title = self.get_text(self.assert_app_iosHelp_element)
        return title
