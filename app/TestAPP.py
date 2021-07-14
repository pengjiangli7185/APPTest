# coding = utf-8
# @Time : 2021/7/5 19:56
# @Author : pengjiangli
# @File : MyTests.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import time
import unittest

from appium import webdriver


class TestAPP(unittest.TestCase):
    # 测试开始前执行的方法
    def setUp(self):
        desired_caps = {'platformName': 'Android', # 平台名称
                        'platformVersion': '7.1.2',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.sh.mww.calc',  # apk的包名
                        'appActivity': 'com.activity.RSplashActivityCheck'  # activity 名称
                        # 'unicodeKeyboard':'True',
                        # 'resetKeyboard':'True'
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    def test_calculator(self, t=500, n=4):
        """计算器测试"""
        time.sleep(3)
        self.driver.find_element_by_id("com.sh.mww.calc:id/ok_btn").click()
        var2=self.driver.find_element_by_id("com.sh.mww.calc:id/digit2").click();
        add = self.driver.find_element_by_id("com.sh.mww.calc:id/plus").click();
        var3=self.driver.find_element_by_id("com.sh.mww.calc:id/digit5").click();
        self.driver.find_element_by_id("com.sh.mww.calc:id/equal").click();
        el2 = self.driver.find_element_by_accessibility_id("5")
        a=2+3;
        self.assertEqual(el2,a)
        print(el2)



        # self.driver.find_element_by_xpath(btn_xpath.format(7)).click()
        # self.driver.find_element_by_xpath(btn_xpath.format(10)).click()
        # self.driver.find_element_by_xpath(btn_xpath.format(8)).click()
        time.sleep(3)

    # 测试结束后执行的方法
    def tearDown(self):
        self.driver.quit()