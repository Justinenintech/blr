"""
@Version: 1.0
@Project: BeautyReport
@Author: Vincent
@Data: 2019/10/17 下午3:48
@File: sample.py
@License: MIT
"""
import datetime
import os
import unittest
from BeautifulReport import BeautifulReport

from Common.sentTelegramMessage import sent_telegram_message

if __name__ == '__main__':
    report_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'report')
    test_dir = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'testcase')
    test_suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    result = BeautifulReport(test_suite)
    now_time = datetime.datetime.now()
    report_name = 'AutomatedTestReport_blr' + now_time.strftime('_%Y%m%d%H%M%S')
    # print(report_name)
    result.report(filename=report_name, description='blr.9161252.com', report_dir=report_dir)
    sent_telegram_message()
