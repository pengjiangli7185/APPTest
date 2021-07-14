# coding = utf-8
# @Time : 2021/7/5 19:56
# @Author : pengjiangli
# @File : MyTests.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import time
import unittest

from appium import webdriver

'''
测试环境搭建：Appium+pyhton+duofenAPP+夜游仿真机
测试前，注意事项：需要设置夜游仿真机设置开发模式,网络改成不桥接
'''
class TestAPP(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '7.1.2',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.gt.magicbox',  # apk的包名
                        'appActivity': 'com.gt.magicbox.main.LoadingActivity'  # activity 名称
                        # 'unicodeKeyboard':'True',  # 绕过手机键盘操作，unicodeKeyboard是使用unicode编码方式发送字符串
                        # 'resetKeyboard':'True'     # 绕过手机键盘操作，resetKeyboard是将键盘隐藏起来

                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_calculator(self, t=500, n=4):
        """测试多粉系统"""
        time.sleep(3)


        time.sleep(3)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()