import os

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

from Common.config import Config
from Common.message import TelegramMessageBackend, CLIMessageBackend
from Common.report_copy import new_file

config = Config()

d = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'report')
abspath = os.path.join(os.path.abspath(d)+'/')
#copy_file = abspath+"/"

def sent_telegram_message():
    # opt = Options()
    # opt.add_argument('--headless')
    # opt.add_argument('--disable-gpu')
    # driver = webdriver.Firefox(options=opt)
    firefox_opt = webdriver.FirefoxOptions()
    firefox_opt.add_argument("--headless")
    driver = webdriver.Firefox(firefox_options=firefox_opt)
    # # 如果没有日期文件夹，创建该文件夹
    # if not os.path.exists(copy_file):
    #     os.makedirs(copy_file)
    file_name = new_file(abspath)
    pro = config.config_read('reports', 'pro')
    # print(pro)
    report_url = pro + file_name
    # print(report_url)
    driver.get(report_url)

    _name = driver.find_element(By.ID, "testName")
    _all = driver.find_element(By.ID, "testAll")
    _pass = driver.find_element(By.ID, "testPass")
    _fail = driver.find_element(By.ID, "testFail")
    _skip= driver.find_element(By.ID, "testSkip")
    _begin = driver.find_element(By.ID, "beginTime")
    _total = driver.find_element(By.ID, "totalTime")
    title_pro = config.config_read('title', 'pro')
    url = config.config_read('environment', 'url')
    case_name = url.split("/")[2]
    text_con = '      <b>%s</b>' % title_pro + '\n' + \
               '<code>用例名称：%s</code>' % case_name + '\n' \
               '<code>用例总数：%s</code>' % _all.text + '\n' \
               '<code>用例通过：%s</code>' % _pass.text + '\n' \
               '<code>用例失败：%s</code>' % _fail.text + '\n' \
               '<code>用例跳过：%s</code>' % _skip.text + '\n' \
               '<code>开始时间：%s</code>' % _begin.text + '\n' \
               '<code>运行时间：%s</code>' % _total.text + '\n' \
               '<code>报告地址：</code>' '<a href="%s"> AutomatedTestReport</a>' % report_url +  '\n'
    # 获取telegram机器人的token
    token = config.config_read('telegram', 'token')
    # 获取频道Id
    chat_id = config.config_read('telegram', 'chat_id')
    #message_backend = CLIMessageBackend()
    message_backend = TelegramMessageBackend(token, chat_id)
    #message_backend.send_raw_message(' <b style="background-color:red">用例名称:</b>' +te+ '\n' '<a href="http://10.10.104.71/tycijt/pro/AutomatedTestReport_20190912105039.html"></a>.')
    message_backend.send_raw_message(text_con)

if __name__ == '__main__':
    sent_telegram_message()