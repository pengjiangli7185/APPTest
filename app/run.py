# coding = utf-8
# @Time : 2021/7/5 19:57
# @Author : pengjiangli
# @File : run.py
# @Software: PyCharm
# @contact: 292617625@qq.com
# -*- coding: UTF-8 -*-
import os
import time
import unittest

from HTMLTestRunner import HTMLTestRunner

test_dir = './testcase'
case_path = os.path.join(os.getcwd(), "")
discover=unittest.defaultTestLoader.discover(case_path, pattern='Test*.py')

if __name__ == "__main__":
    report_dir = './test_report'
    os.makedirs(report_dir, exist_ok=True)
    now = time.strftime("%Y-%m-%d %H-%M-%S")
    report_name = '{0}/{1}.html'.format(report_dir, now)

    with open(report_name, 'wb')as f:
        runner = HTMLTestRunner(stream=f, title="测试报告", description="本测试报告内容包含超级计算器的简单测试")
        runner.run(discover)