import os
import time
from enum import Enum, unique
from threading import Thread

# import win32con
# import win32gui
#from win32 import win32gui
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common import keys
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import *  # 导入所有的异常类
from selenium.webdriver.support import expected_conditions as EC

from Common.getYaml import get_yaml
from Common.log import log1
from Common.config import Config
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

path = os.getcwd()
config = Config()


class BasePage():
    data = get_yaml()
    """测试基类"""
    _by_char = None

    # driver = None

    def __init__(self, driver):
        self.driver = driver

    # def __init__(self, driver,browser_type=0, download_path="c:\\Users\\tester\\Downloads", by_char=",", profile=None):
    #     """
    #            构造方法：实例化 BoxDriver 时候使用
    #            :param browser_type: 浏览器类型
    #            :param by_char: 分隔符，默认使用","
    #            :param profile:
    #                可选择的参数，如果不传递，就是None
    #                如果传递一个 profile，就会按照预先的设定启动火狐
    #                去掉遮挡元素的提示框等
    #            """
    #     self.driver = driver
    #     self._by_char = by_char
    #     if browser_type == 0 or browser_type == Browser.Chrome:
    #
    #         profile = webdriver.ChromeOptions()
    #         # profile.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
    #
    #         # download.default_directory：设置下载路径
    #         # profile.default_content_settings.popups：设置为 0 禁止弹出窗口
    #         prefs = {'profile.default_content_settings.popups': 0,
    #                  'download.default_directory': download_path}
    #         profile.add_experimental_option('prefs', prefs)
    #
    #         driver = webdriver.Chrome(chrome_options=profile)
    #         # driver = webdriver.Chrome(executable_path='D:\\chromedriver.exe', chrome_options=options)
    #
    #     elif browser_type == 1 or browser_type == Browser.Firefox:
    #         # if profile is not None:
    #         # profile = FirefoxProfile(profile)
    #
    #         profile = webdriver.FirefoxProfile()
    #         # 指定下载路径
    #         profile.set_preference('browser.download.dir', download_path)
    #         # 设置成 2 表示使用自定义下载路径；设置成 0 表示下载到桌面；设置成 1 表示下载到默认路径
    #         profile.set_preference('browser.download.folderList', 2)
    #         # 在开始下载时是否显示下载管理器
    #         profile.set_preference('browser.download.manager.showWhenStarting', False)
    #         # 对所给出文件类型不再弹出框进行询问
    #         profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
    #
    #         driver = webdriver.Firefox(firefox_profile=profile)
    #
    #     elif browser_type == Browser.Ie:
    #         driver = webdriver.Ie()
    #     else:
    #         driver = webdriver.PhantomJS()
    #     try:
    #         self.driver = driver
    #         self._by_char = by_char
    #     except Exception:
    #         raise NameError("Browser %s Not Found! " % browser_type)

    def open_browser(self):
        """
        Open a browser and access the url
        :return:
        """
        browser = config.config_read('environment', 'browser')
        log1.info('Read browser configuration, value：%s' % browser)
        url = config.config_read('environment', 'url')
        log1.info('Read url configuration, value：%s' % url)
        # noinspection PyBroadException
        try:
            # lists = ['chrome', 'firefox']
            # # 通过不同的浏览器执行脚本
            # for browser in lists:
            #     print(browser)
            #     self.driver = webdriver.Remote(
            #         command_executor='http://10.10.104.71:4444/wd/hub',
            #         desired_capabilities={'platform': 'ANY', 'browserName': 'chrome', 'version': '',
            #                               'javascriptEnabled': True})
            self.driver = webdriver.Remote(
                command_executor='http://10.10.104.79:5558/wd/hub',
                desired_capabilities={'platform': 'ANY', 'browserName': browser, 'version': '',
                                      'javascriptEnabled': True})
            #self.driver = webdriver.Firefox()
            self.navigate(url)
            log1.info('Visit website：%s' % url)
            self.maximize_window()
            # self.driver.maximize_window()
            log1.info('Browser maximization')
            self.driver.implicitly_wait(10)
            log1.info('Set static wait time 10 seconds')
            return self.driver
        except BaseException:
            log1.error('Browser open error', exc_info=1)
            self.dr_quit()

    # def get_element(self, selector):
    #     """定位元素"""
    #     by = selector[0]
    #     value = selector[1]
    #     bys = ['id', 'name', 'class', 'tag', 'link', 'plink', 'css', 'xpath']
    #     element = None
    #     if by in bys:
    #         try:
    #             if by == 'id':
    #                 element = self.driver.find_element_by_id(value)
    #             elif by == 'name':
    #                 element = self.driver.find_element_by_name(value)
    #             elif by == 'class':
    #                 element = self.driver.find_element_by_class_name(value)
    #             elif by == 'tag':
    #                 element = self.driver.find_element_by_tag_name(value)
    #             elif by == 'link':
    #                 element = self.driver.find_element_by_link_text(value)
    #             elif by == 'plink':
    #                 element = self.driver.find_element_by_partial_link_text(value)
    #             elif by == 'css':
    #                 element = self.driver.find_element_by_css_selector(value)
    #             elif by == 'xpath':
    #                 element = self.driver.find_element_by_xpath(value)
    #             log1.info('元素定位成功。定位方式：%s，使用的值：%s' % (by, value))
    #             return element
    #         except NoSuchElementException:
    #             log1.error('没有定位到元素,定位方式：%s，使用的值：%s' % (by, value), exc_info=1)
    #     else:
    #         log1.error('元素定位方式错误，请使用id，name，class，tag，link，plink，css，xpath为定位方式参数')

    """
    Private method
    """

    def _convert_selector_to_locator(self, selector):
        """
        Convert custom selector to Selenium supported locator
        :param selector: Positioning character, string type，"i, xxx"
        :return: locator
        """
        if self._by_char not in selector:
            return By.ID, selector

        selector_by = selector.split(self._by_char)[0].strip()
        selector_value = selector.split(self._by_char)[1].strip()
        if selector_by == "i" or selector_by == 'id':
            locator = (By.ID, selector_value)
        elif selector_by == "n" or selector_by == 'name':
            locator = (By.NAME, selector_value)
        elif selector_by == "c" or selector_by == 'class_name':
            locator = (By.CLASS_NAME, selector_value)
        elif selector_by == "l" or selector_by == 'link_text':
            locator = (By.LINK_TEXT, selector_value)
        elif selector_by == "p" or selector_by == 'partial_link_text':
            locator = (By.PARTIAL_LINK_TEXT, selector_value)
        elif selector_by == "t" or selector_by == 'tag_name':
            locator = (By.TAG_NAME, selector_value)
        elif selector_by == "x" or selector_by == 'xpath':
            locator = (By.XPATH, selector_value)
        elif selector_by == "s" or selector_by == 'css_selector':
            locator = (By.CSS_SELECTOR, selector_value)
        else:
            raise NameError("Please enter a valid selector of targeting elements.")
        return locator

    def find_element(self, selector, timeout=10):
        """
        Positioning element, parameter selector is element ancestor type

        :param selector: selector = ("id","xxx"),driver.find_element(selector)
        :param timeout: 10
        :return:
        """
        try:

            element = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_element_located(selector))
            log1.info('Successful positioning of elements.Positioning method and values used：%s' % selector)
            return element
        except NoSuchElementException:
            log1.error('Error positioning of elements,Positioning method and values used：%s' % selector, exc_info=1)

    def find_elements(self, selector, timeout=10):
        """
        Locate a set of elements
        :param selector: selector = ("id","xxx"),driver.find_element(selector)
        :param timeout: 10
        :return:
        """
        try:
            elements = WebDriverWait(self.driver, timeout, 1).until(EC.presence_of_all_elements_located(selector))
            log1.info('Successful positioning of elements.Positioning method and values used：%s' % selector)
            return elements
        except NoSuchElementException:
            log1.error('Error positioning of elements,Positioning method and values used：%s' % selector, exc_info=1)

    """
    Browser related methods
    """

    def refresh(self, url=None):
        """
        refresh page
        If the url is null, the current page is refreshed, otherwise the specified page is refreshed.
        :param url: 默认值是空的
        :return:
        """
        if url is None:
            self.driver.refresh()
        else:
            self.driver.get(url)

    def maximize_window(self):
        """
        Maximize the current browser window
        :return:
        """
        self.driver.maximize_window()

    def navigate(self, url):
        """
        open URL
        :param url:
        :return:
        """
        self.driver.get(url)

    def dr_quit(self):
        """
        Exit driver
        :return:
        """
        self.driver.quit()

    def close_browser(self):
        """
        Close the browser
        :return:
        """
        self.driver.close()

    def back(self):
        """
        Back to old window.
        Usage:
        driver.back()
        """
        self.driver.back()

    def forward(self):
        """
        Forward to old window.
        Usage:
        driver.forward()
        """
        self.driver.forward()

    """
    cookies Related operations
    """

    def clear_cookies(self):
        """
        clear all cookies after driver init
        """
        self.driver.delete_all_cookies()

    def add_cookies(self, cookies):
        """
        Add cookie by dict
        :param cookies:
        :return:
        """
        self.driver.add_cookie(cookie_dict=cookies)

    def add_cookie(self, cookie_dict):
        """
        Add single cookie by dict
        添加 单个 cookie
        如果该 cookie 已经存在，就先删除后，再添加
        :param cookie_dict: 字典类型，有两个key：name 和 value
        :return:
        """
        cookie_name = cookie_dict["name"]
        cookie_value = self.driver.get_cookie(cookie_name)
        if cookie_value is not None:
            self.driver.delete_cookie(cookie_name)

        self.driver.add_cookie(cookie_dict)

    def remove_cookie(self, name):
        """
        移除指定 name 的cookie
        :param name:
        :return:
        """
        # 检查 cookie 是否存在，存在就移除
        old_cookie_value = self.driver.get_cookie(name)
        if old_cookie_value is not None:
            self.driver.delete_cookie(name)

    """
    Basic element related method
    """

    def type_send(self, selector, value):
        """
        Enter content in the input box
        :param selector:
        :param value:
        :return:
        """
        element = self.find_element(selector)
        element.send_keys(Keys.CONTROL+'a')
        element.send_keys(Keys.DELETE)
        #element.send_keys(chr(127) * len('30'))
        try:
            element.send_keys(value)
            log1.info('Input content：%s' % value)
        except BaseException:
            log1.error('Content input error', exc_info=1)
            self.save_window_snapshot('Content input error')

    def type(self, selector, value):
        """
        Enter content in the input box
        :param selector:
        :param value:
        :return:
        """
        element = self.find_element(selector)
        element.clear()
        try:
            element.send_keys(value)
            log1.info('Input content：%s' % value)
        except BaseException:
            log1.error('Content input error', exc_info=1)
            self.save_window_snapshot('Content input error')

    def click(self, selector):
        """
        Click element
        :param selector:
        :return:
        """
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            #ActionChains(self.driver).click(element).perform()
            element.click()
            log1.info('Click on the element success,location method and value used：%s' % selector)
        except BaseException:
            isdisplay = self.get_displayed(element)
            if isdisplay is True:
                self.forced_wait(2)
                #ActionChains(self.driver).click(element).perform()
                element.click()
                log1.info('Click on the element success,location method and value used：%s' % selector)
            else:
                log1.error('Click on the element error,location method and value used：%s' % selector, exc_info=1)

    def click_eles(self, selector,locator,cator,span_text):
        """
        Loop through each element of a set of elements
        :param selector:
        :return:
        """
        counts = self.count_elements(selector,locator)
        el = self.find_element(selector)
        eles = el.find_elements_by_xpath(locator)
        spans = el.find_elements_by_xpath(cator)
        for i in range(counts):
            if spans[i].text == span_text:
                _url = eles[i].get_attribute("href")
                log1.info("_url：%s" % _url)
                eles[i].click()
                open_url = self.driver.current_url
                log1.info("open_url：%s" % open_url)
                assert _url.split("/")[2] == open_url.split("/")[2], "进入官网站失败，网页中地址{%s}，打开的网站{%s}" % (_url, open_url)
                log1.info("成功进入官网，打开的网站{%s}" % open_url)
                self.save_window_snapshot("线路检测：%s" % open_url)
                self.forced_wait(5)
                self.close_browser()
                self.forced_wait(5)
                click_line = self.data['links'].get('link_domain_detection_page')  # 线路检测
                self.click(click_line)
                return _url, open_url

    def click_eles_i(self, selector, i):
        """
        Click on the first element of a set of elements
        :param selector:
        :param i: The first few elements
        :return:
        """
        eles = self.find_elements(selector)
        url = eles[i].get_attribute("address")
        log1.info("_url：%s" % url)
        eles[i].click()
        open_url = self.driver.current_url
        log1.info("open_url：%s" % open_url)
        assert url.split("/")[2] == open_url.split("/")[2], "进入官网站失败，网页中地址{%s}，打开的网站{%s}" % (url, open_url)
        log1.info("成功进入官网，打开的网站{%s}" % open_url)
        self.save_window_snapshot("线路检测：%s" % open_url)
        self.forced_wait(3)
        self.close_browser()

    def click_enter(self, selector):
        """
        It can type any text / image can be located  with ENTER key
        :param selector:
        :return:
        """
        el = self.find_element(selector)
        el.send_keys(Keys.ENTER)

    def click_esc(self, selector):
        """
        ESC event instead of close button
        :param selector:
        :return:
        """
        el = self.find_element(selector)
        el.send_keys(Keys.ESCAPE)

    def click_action_esc(self):
        action = ActionChains(self.driver)
        action.key_down(Keys.ESCAPE).perform()
        action.key_up(Keys.ESCAPE).perform()

    def right_click(self, selector):
        """
        Right mouse click
        :param selector:
        :return:
        """
        el = self.find_element(selector)
        try:
            el.context_click()
            log1.info('Right click on the element success,location method and value used：%s' % selector)
        except BaseException:
            isdisplay = self.get_displayed(el)
            if isdisplay is True:
                self.forced_wait(2)
                # ActionChains(self.driver).click(element).perform()
                el.context_click()
                log1.info('Right click on the element success,location method and value used：%s' % selector)
            else:
                log1.error('Right click on the element error,location method and value used：%s' % selector, exc_info=1)

    def double_click(self, selector):
        """
        Double click the mouse
        :param selector:
        :return:
        """
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            # ActionChains(self.driver).click(element).perform()
            element.double_click()
            log1.info('Double click on the element success,location method and value used：%s' % selector)
        except BaseException:
            isdisplay = self.get_displayed(element)
            if isdisplay is True:
                self.forced_wait(2)
                # ActionChains(self.driver).click(element).perform()
                element.double_click()
                log1.info('Double click on the element success,location method and value used：%s' % selector)
            else:
                log1.error('Double click on the element error,location method and value used：%s' % selector, exc_info=1)

    def move_to_element(self, selector):
        """
        Mouse hover operation
        :param selector:
        :return:
        """
        element = self.find_element(selector)
        ActionChains(self.driver).move_to_element(element).perform()

    def drag_element(self, source, target):
        """
        Drag and drop element
        :param source:
        :param target:
        :return:
        """

        el_source = self.find_element(source)
        el_target = self.find_element(target)

        if self.driver.w3c:
            ActionChains(self.driver).drag_and_drop(el_source, el_target).perform()
        else:
            ActionChains(self.driver).click_and_hold(el_source).perform()
            ActionChains(self.driver).move_to_element(el_target).perform()
            ActionChains(self.driver).release(el_target).perform()

    def lost_focus(self):
        """
        Current element loses focus
        :return:
        """
        ActionChains(self.driver).key_down(Keys.TAB).key_up(Keys.TAB).perform()

    """
    Element attribute related method
    """

    def get_text(self, selector):
        """
        Get element text information.
        :param selector:
        :return:

        Usage:
        driver.get_text("i,el")
        """
        el = self.find_element(selector)
        #text = el.text
        log1.info("Obtained text：%s" % el.text)
        return el.text

    def get_attribute(self, selector, attribute):
        """
         Gets the value of an element attribute.
        :param selector:
        :param attribute:
        :return:

        usage:
        driver.get_attribute("i,el","type")
        """
        el = self.find_element(selector)
        return el.get_attribute(attribute)

    def get_displayed(self, selector):
        """
        Gets the element to display,The return result is true or false.

        Usage:
        driver.get_display("i,el")
        """
        el = self.find_element(selector)
        return el.is_displayed()

    def get_exist(self, selector):
        '''
        该方法用来确认元素是否存在，如果存在返回flag=true，否则返回false
        :param self:
        :param selector: 元素定位，如'id,account'
        :return: 布尔值
        '''
        flag = True
        try:
            self.find_element(selector)
            return flag
        except:
            flag = False
            return flag

    def get_enabled(self, selector):
        '''
        Determine if the page element is clickable
        :param selector: 元素定位
        :return: Boolean value
        '''
        if self.find_element(selector).is_enabled():
            return True
        else:
            return False

    def get_title(self):
        '''
        Get window title.

        Usage:
        driver.get_title()
        '''
        _title = self.driver.title
        log1.info("Obtained title：%s" % _title)
        return _title

    def get_url(self):
        """
        Get the URL address of the current page.

        Usage:
        driver.get_url()
        """
        return self.driver.current_url

    def get_value(self, locator, value, timeout=10):
        """
        Determines the value of the element, does not locate the element and returns false, and locates the boolean value that returns the judgment result.
        :param locator:
        :param value:
        :param timeout:
        :return:

        Usage:
        result = driver.text_in_element(locator, text)
        """
        try:
            result = WebDriverWait(self.driver, timeout, 1).until(
                EC.text_to_be_present_in_element_value(locator, value))
        except TimeoutException:
            print("Element failed to locate：" + str(locator))
            return False
        else:
            return result

    def get_selected(self, selector):
        """
        to return the selected status of an WebElement
        :param selector: selector to locate
        :return: True False
        """
        el = self.find_element(selector)
        return el.is_selected()

    def get_text_list(self, selector):
        """
        Get multiple elements based on the selector, get the text list of the element
        :param selector:
        :return: list
        """
        el_list = self.find_element(selector)
        results = []
        for el in el_list:
            results.append(el.text)
        return results

    """
    Enter the frame, exit the frame
    """

    def switch_menue(self, parentelement, secelement, targetelement):
        """
        Three-level menu switch
        :param parentelement:
        :param secelement:
        :param targetelement:
        :return:
        """
        self.forced_wait(3)
        # noinspection PyBroadException
        try:
            self.driver.switch_to_default_content()
            self.click(parentelement)
            log1.info('Successfully click on the first level menu：%s' % parentelement)
            self.click(secelement)
            log1.info('Successfully click on the secondary menu：%s' % secelement)
            self.click(targetelement)
            log1.info('Successfully click on the third level menu：%s' % targetelement)
        except BaseException:
            log1.error('Switch frame error', exc_info=1)

    def switch_to_frame(self, selector):
        """
        Switch to the specified frame
        :param selector:
        :return:
        Usage:
        driver.switch_to_frame("i,el")
        """
        element = self.find_element(selector)
        # noinspection PyBroadException
        try:
            self.driver.switch_to.frame(element)
            log1.info('Switch frame successfully')
        except BaseException:
            log1.error('Switch frame error', exc_info=1)

    def switch_to_default(self):
        """
        Switch to the specified frame
        :param selector:
        :return:
        Usage:
        driver.switch_to_frame("i,el")
        """
        try:
            self.driver.switch_to.default_content()
            log1.info('Switch frame successfully')
        except BaseException:
            log1.error('Switch frame failed', exc_info=1)

    """
    Switch between different page windows
    """

    def switch_to_window_by_title(self, title):
        for handle in self.driver.window_handles:
            self.driver.switch_to.window(handle)
            if self.driver.title == title:
                break
            self.driver.switch_to.default_content()

    def open_new_window(self, selector):
        """
        Open the new window and switch the handle to the newly opened window.
        :param selector:
        :return:

        Usage:
        driver.open_new_window()
        """
        original_windows = self.driver.current_window_handle
        el = self.find_element(selector)
        el.click()
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    def get_new_handle(self):
        """
        switch the handle to the newly opened window.
        :param selector:
        :return:

        Usage:
        driver.get_new_handle()
        """
        original_windows = self.driver.current_window_handle
        all_handles = self.driver.window_handles
        for handle in all_handles:
            if handle != original_windows:
                self.driver.switch_to.window(handle)

    def save_window_snapshot(self, img_name):
        """
        save screen snapshot
        :param img_name: the image file name and path
        :return:
        """
        # img文件夹路径
        img_path = os.path.join(os.getcwd(), 'img/')
        # img文件夹不存在，新建该文件夹
        if not os.path.exists(img_path):
            os.makedirs(img_path)
        # 获取当前日期
        # local_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
        # 日期文件夹路径
        date_file_path = os.path.join(img_path, 'pass_img/')
        # 日期文件夹不存在，新建该文件夹
        if not os.path.exists(date_file_path):
            os.makedirs(date_file_path)
        # 截图存放路径
        # local_time = time.strftime('%Y-%m-%d %H%M%S', time.localtime(time.time()))
        # jt_name = local_time + '.png'
        # jt_path = os.path.join(date_file_path, jt_name)
        try:
            # self.driver.get_screenshot_as_file(jt_path)
            self.driver.get_screenshot_as_file('{}/{}.png'.format(os.path.join(date_file_path), img_name))
            log1.info('Screenshot saved successfully!')
        except BaseException as e:
            log1.error('Screenshot failed!', format(e), exc_info=1)

    def save_window_snapshot_by_io(self):
        """
        Save screenshot as file stream
        :return:
        """
        return self.driver.get_screenshot_as_base64()

    def save_element_snapshot_by_io(self, selector):
        """
        Control screenshot
        :param selector:
        :return:
        """
        el = self.find_element(selector)
        return el.screenshot_as_base64

    """
    Waiting method
    """

    @staticmethod
    def forced_wait(seconds):
        """
        Forced wait
        :param secondes:
        :return:
        """
        time.sleep(seconds)
        log1.info('Forced wait %d second' % seconds)

    def implicitly_wait(self, seconds):
        """
        Implicitly wait. All elements on the page.
        :param seconds 等待时间 秒
        Implicit wait

        Usage:
        driver.implicitly_wait(10)
        """

        self.driver.implicitly_wait(seconds)
        log1.info('Implicit wait %d second' % seconds)

    def explicitly_wait(self, selector, seconds=10):
        """
        explicitly wait
        :param selector: 定位字符
        :param seconds: 最长等待时间，秒
        :return:
        """
        locator = self.get_element(selector)
        WebDriverWait(self.driver, seconds, 1).until(EC.presence_of_element_located(locator))

    """
    Upload
    """

    def upload_input(self, selector, file):
        '''
        Upload file (labeled as input type, this type is the most common, the easiest)
        :param selector: Upload button positioning
        :param file: The file to be uploaded (absolute path)
        :return: 无
        '''
        self.find_element(selector).send_keys(file)

    # def upload_not_input(self, file, browser_type='Chrome'):
    #     '''
    #     Upload file (label is not input type, use win32gui, you must first install pywin32 dependency package::pip install pywin32)
    #     :param browser_type: Browser type (the difference between Chrome browser and Firefox browser)
    #     :param file: The file to be uploaded (absolute path)
    #     Single file：file1 = 'C:\\Users\\list_tuple_dict_test.py'
    #     Upload multiple files at the same time：file2 = '"C:\\Users\\list_tuple_dict_test.py" "C:\\Users\\class_def.py"'
    #     :return: 无
    #     '''
    #     # Chrome 浏览器是'打开'
    #     # 对话框
    #     # 下载个 Spy++ 工具，定位“打开”窗口，定位到窗口的类(L):#32770, '打开'为窗口标题
    #     if browser_type == 'Chrome':
    #         dialog = win32gui.FindWindow('#32770', u'打开')
    #     elif browser_type == 'Firefox':
    #         # Firefox 浏览器是'文件上传'
    #         # 对话框
    #         dialog = win32gui.FindWindow('#32770', u'文件上传')
    #     ComboBoxEx32 = win32gui.FindWindowEx(dialog, 0, 'ComboBoxEx32', None)
    #     ComboBox = win32gui.FindWindowEx(ComboBoxEx32, 0, 'ComboBox', None)
    #     # 上面三句依次寻找对象，直到找到输入框Edit对象的句柄
    #     Edit = win32gui.FindWindowEx(ComboBox, 0, 'Edit', None)
    #     # 确定按钮Button
    #     button = win32gui.FindWindowEx(dialog, 0, 'Button', None)
    #     # 往输入框输入绝对地址
    #     win32gui.SendMessage(Edit, win32con.WM_SETTEXT, None, file)
    #     # 按button
    #     win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)
    #     # 获取属性
        # print(upload.get_attribute('value'))

    #
    # """下载 //TODO"""
    #
    # def download(self, download_path, file_type, download_selector):
    #     '''
    #     下载（设置指定下载路径，不用每次都弹出对话框选择保存路径）
    #     :param download_path: 设置默认下载路径
    #     :param file_type: 默认下载文件类型
    #     :param download_selector: 下载元素定位
    #     :return:
    #     '''
    #     profile = webdriver.FirefoxProfile()
    #     profile.set_preference('browser.download.dir', download_path)
    #     profile.set_preference('browser.download.folderList', 2)
    #     profile.set_preference('browser.download.manager.showWhenStarting', False)
    #     profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'application/zip')
    #
    #     driver = webdriver.Firefox(firefox_profile=profile)

    """
    Form data submission:
        1. Page check
        2. Database check
        3. Select, edit, delete a record
    """

    def del_edit_choose_the_row(self, selector_of_next_page, selector_of_trs_td, selector_of_del_edit_choose,
                                expected_td_value):
        """
        页面表单，选中/编辑/删除 指定内容的行（带多页翻页功能）
        :param selector_of_next_page: ‘下一页’定位，如：'l,下页'
        :param selector_of_trs_td: 所有行的某一列的定位，如 ranzhi 成员列表中，获取所有行的“真实姓名”那列：'x,/html/body/div/div/div/div[2]/div/div/table/tbody//tr/td[2]'
        :param selector_of_del_edit_choose: 指定要操作(删除/编辑/选择)的列，如 ranzhi 成员列表中,获取期望删除的列：'x,/html/body/div/div/div/div[2]/div/div/table/tbody/tr[%d]/td[11]/a[3]'
        :param expected_td_value: 期望的列内容，如ranzhi 成员列表中期望的“真实姓名”: '华仔'
        :return:无
        """

        td_values = self.get_text_list(selector_of_trs_td)
        for i in range(len(td_values)):
            if td_values[i] == expected_td_value:
                print('%s在第%d行显示(首页)！' % (td_values[i], i + 1))
                self.forced_wait(2)
                self.click(selector_of_del_edit_choose % (i + 1))
                break
        try:
            while (self.get_enabled(selector_of_next_page)):
                self.click(selector_of_next_page)
                self.forced_wait(2)
                td_values = self.get_text_list(selector_of_trs_td)
                for i in range(len(td_values)):
                    if td_values[i] == expected_td_value:
                        print('%s在第%d行显示(非首页)' % (td_values[i], i + 1))
                        self.forced_wait(3)
                        self.click(selector_of_del_edit_choose % (i + 1))
                continue
        except Exception as e:
            print('%s 操作成功！' % expected_td_value)

    def assert_new_record_exist_in_table(self, selector_of_next_page, selector_of_trs_td, expected_td_value):
        '''
        此方法针对页面列表（带多页翻页功能），都可以判断新增记录是否添加成功！
        若新增成功，则返回 True 布尔值；否则返回 False 布尔值
        :param selector_of_next_page: "下一页"定位，如：
        :param selector_of_trs_td:所有行的某一列的定位，如： 'l,下页''x,/html/body/div/div[2]/div/div[1]/div/table/tbody//tr/td[2]'
        :param expected_td_value:期望的列内容,如：'华仔'
        :return: 布尔值
        '''
        # first_count_per_page = self.count_elements(selector_of_real_record)
        # print('当前设置为每页显示 %s 条记录' % first_count_per_page)
        real_records = self.get_text_list(selector_of_trs_td)
        for real_record in real_records:
            if real_record == expected_td_value:
                return True
        # count_per_page_whiles = 0
        try:

            while (self.get_enabled(selector_of_next_page)):
                self.click(selector_of_next_page)
                self.forced_wait(2)
                # count_per_page_while = driver.count_elements("x,//tbody//tr/td[2]")
                # count_per_page_whiles += count_per_page_while
                next_page_real_records = self.get_text_list(selector_of_trs_td)
                for next_page_real_record in next_page_real_records:
                    if next_page_real_record == expected_td_value:
                        # self.log.info('记录新增成功！新增记录 %s 不是在第一页被找到！'%expect_new_record)
                        return True
                continue
        except Exception as e:
            # count_page_real_show = count_per_page_whiles + first_count_per_page
            # print("页面实际显示记录条数：%s" % count_page_real_show)
            # 页面统计总数 VS 页面实际显示记录总数
            # assert count_page_real_show == int(total_num)
            # print("‘页面实际显示记录总数’ 与 ‘页面统计显示记录总数’ 相同！")

            # raise NameError("页面表单中无此数据，原因：(1)请查询待验证的数据是否输入正确？(2)或者'下页'翻页定位是否正确？")
            print("页面表单中无此数据，原因：(1)请查询待验证的数据是否输入正确？(2)或者'下页'翻页定位是否正确？")
            return False

    # def assert_new_record_exist_mysql(self, db_yaml_path, db_yaml_name, sql_file_path, select_field_num,
    #                                   expected_td_value):
    #     '''
    #     数据库校验，True为数据库中存在该数据
    #     :param db_yaml_path: 数据库的yaml格式的配置文件路径
    #     :param db_yaml_name: 数据库的yaml格式的配置文件中设置的数据库名（默认是在'DbConfig'下面）
    #     :param sql_file_path: sql文件路径
    #     :param select_field_num: 查询语句中第几个字段（默认0表示第1个字段）
    #     :param expected_td_value: 期望要断言的值
    #     :return: True / False
    #     '''
    #     ydata = YamlHelper().get_config_dict(db_yaml_path)
    #     host = ydata['DbConfig'][db_yaml_name]['host']
    #     port = ydata['DbConfig'][db_yaml_name]['port']
    #     user = ydata['DbConfig'][db_yaml_name]['user']
    #     pwd = ydata['DbConfig'][db_yaml_name]['pwd']
    #     db = ydata['DbConfig'][db_yaml_name]['db']
    #
    #     db_helper = DbHelper(host, port, user, pwd, db)
    #     sql = db_helper.read_sql(sql_file_path)
    #     result = db_helper.execute(sql)['data']
    #     db_helper.close()
    #     try:
    #         for i in result:
    #             if i[select_field_num] == expected_td_value:
    #                 return True
    #     except Exception:
    #         return False

    """
    <select> element related
    """

    def select_by_index(self, selector, index):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self.find_element(selector)
        Select(el).select_by_index(index)

    def get_selected_text(self, selector):
        """
        Get the selected content of the Select element
        :param selector: 选择字符 "i, xxx"
        :return: 字符串
        """
        el = self.find_element(selector)
        selected_opt = Select(el).first_selected_option()
        return selected_opt.text

    def select_by_visible_text(self, selector, text):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self.find_element(selector)
        Select(el).select_by_visible_text(text)

    def select_by_value(self, selector, value):
        """
        It can click any text / image can be clicked
        Connection, check box, radio buttons, and even drop-down box etc..

        Usage:
        driver.select_by_index("i,el")
        """
        el = self.find_element(selector)
        Select(el).select_by_value(value)

    """
    JavaScript element related
    """

    def js_focus_element(self, selector):
        """
        Focusing element
        :param selector:
        :return:
        """
        target = self.find_element(selector)
        self.driver.execute_script("arguments[0].scrollIntoView();", target)

    def js_scroll_top(self):
        """
        Scroll to the top
        :return:
        """
        js = "var q=document.documentElement.scrollTop=0"
        self.driver.execute_script(js)
        self.forced_wait(1)
        log1.info('JavaScript execution is successful，JavaScript content is：%s' % js)

    def js_scroll_end(self):
        """
        Scroll to the bottom
        :return:
        """
        js = "var q=document.documentElement.scrollTop=100000"
        self.driver.execute_script(js)

    def use_js(self, js):
        """
        Calling JavaScript
        :param js:
        :return:
        """
        # noinspection PyBroadException
        try:
            self.driver.execute_script(js)
            log1.info('JavaScript execution is successful，JavaScript content is：%s' % js)
        except BaseException:
            log1.error('JavaScript execution is error，JavaScript content is：%s' % js, exc_info=1)

    def count_elements(self, selector, elector):
        """
        Find the number of elements.
        :param selector: 定位符
        :return:
        """
        el = self.find_element(selector)
        els = el.find_elements_by_xpath(elector)
        return len(els)

    """
    弹出窗口相关方法
    * 如果弹框的元素可以F12元素查看，则直接使用点击，获取元素等方法
    * 如果弹框元素无法查看，则使用如下方法可以搞定
    """

    def accept_alert(self):
        '''
            Accept warning box.

            Usage:
            driver.accept_alert()
            '''
        self.driver.switch_to.alert.accept()

    def dismiss_alert(self):
        '''
        Dismisses the alert available.

        Usage:
        driver.dismissAlert()
        '''
        self.driver.switch_to.alert.dismiss()

    def get_alert_text(self):
        '''
        获取 alert 弹出框的文本信息
        :return: String
        '''
        return self.driver.switch_to.alert.text

    def type_in_alert(self, text):
        '''在prompt对话框内输入内容'''
        self.driver.switch_to.alert.send_keys(text)
        self.forced_wait(1)

    def alert_new_display_none(self, selector_by_id_value):
        '''
        使用 JS 处理新型弹出框
        :param selector_by_id_value: id方式定位弹出框(div)的 value 值
        :return: 无
        '''
        js = 'document.getElementById("%s").style.display="none";' % selector_by_id_value
        self.driver.execute_script(js)


@unique
class Browser(Enum):
    """
    定义支持的浏览器，支持Chrome，Firefox，Ie
    """
    Chrome = 0
    Firefox = 1
    Ie = 2
