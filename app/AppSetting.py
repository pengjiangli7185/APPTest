# coding = utf-8
# @Time : 2021/7/12 16:22
# @Author : pengjiangli
# @File : AppSetting.py
# @Software: PyCharm
# @contact: 292617625@qq.com
import os
import unittest
from time import sleep

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class Appsetting(unittest.TestCase):
    def setUp(self):
        desired_caps = {'platformName': 'Android',  # 平台名称
                        'platformVersion': '7.1.2',  # 系统版本号
                        'deviceName': '127.0.0.1:62001',  # 设备名称。如果是真机，在'设置->关于手机->设备名称'里查看
                        'appPackage': 'com.android.settings',  # apk的包名
                        'appActivity': '.Settings',  # activity 名称
                        'unicodeKeyboard': True,  # unicode设置(允许中文输入)
                        'resetKeyboard': True  # 键盘设置(允许中文输入)
                        }
        self.driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_caps)  # 连接Appium
        self.driver.implicitly_wait(8)

    # 现在手机设置wift
    # def testCase(self):
    #     setList=self.driver.find_element_by_id("com.android.settings:id/dashboard_tile")
    #     setList.click()
    #     wift=self.driver.find_element_by_xpath("//*[contains(@text,'添加网络')]")
    #     wift.click();
    #     wiftName = self.driver.find_element_by_id("com.android.settings:id/ssid")
    #     wiftName.clear()
    #     wiftName.send_keys("pjl")
    #     self.driver.find_element_by_id("android:id/button1").click()
    #     print("第一个测试")

    # 搜索
    # def testSearch(self):
    #     search = self.driver.find_element_by_id("com.android.settings:id/search")
    #     search.click()
    #     searchInput=self.driver.find_element_by_id("android:id/search_src_text")
    #     searchInput.clear()
    #     searchInput.send_keys("设置")
    #
    #     sleep(5)
    #     searchInput.clear()
    #     searchInput.send_keys("w")

    # 手指轻敲操作
    # 通过元素定位方式敲击屏幕
    # def testTap(self):
    #     el = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
    #     TouchAction(self.driver).tap(el).perform()

    # 手指轻敲操作
    # 通过坐标方式敲击屏幕，WLAN坐标:x=155,y=250
    # [0,768][1080,912] https://blog.csdn.net/songsallyjin/article/details/47150703
    # def testcoordinate(self):
    #     TouchAction(self.driver).tap(x=0, y=900).perform()

    # 手指按操作
    # 模拟手指按下屏幕,按就要对应着离开.
    # def testPress(self):
    #     el = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
    #     TouchAction(self.driver).press(el).release().perform()
    #
    # #通过坐标方式按下屏幕，WLAN坐标:x=155,y=250
    # def testPressCoordinate(self):
    #     TouchAction(self.driver).press(x=0, y=900).release().perform()

    '''
        业务场景:
      1.进入设置
      2.点击WLAN选项
      3.长按WiredSSID选项5秒
    '''
    # def testWait(self):
    #     # 点击WLAN
    #     self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
    #     # 定位到WiredSSID
    #     el= self.driver.find_element_by_xpath("//*[contains(@text,'WiredSSID')]")
    #     TouchAction(self.driver).press(el).wait(5000).perform()

    '''
    模拟手机按下屏幕一段时间,按就要对应着离开.
    方法：long_press(el=None, x=None, y=None, duration=1000)
     参数：
      1.element：被定位到的元素
      2.x：通常会使用元素的X轴坐标
      3.y：通常会使用元素的Y轴坐标
      4.duration：持续时间，默认为1000ms
      
    业务场景:
      1.进入设置
      2.点击WLAN选项
      3.长按WiredSSID选项5秒
      
    '''

    # def testlong_press(self):
    #     # 点击WLAN
    #     self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]").click()
    #     # 定位到WiredSSID
    #     el = self.driver.find_element_by_xpath("//*[contains(@text,'WiredSSID')]")
    #     # 通过元素定位方式长按元素
    #     TouchAction(self.driver).long_press(el, duration=5000).release().perform()

    '''
    手指移动操作
    模拟手机的滑动操作
      方法：move_to(el=None, x=None, y=None)
      参数:
          1.el:定位的元素
          2.x:相对于前一个元素的X轴偏移量
          3.y:相对于前一个元素的Y轴偏移量
          
     业务场景1：
      1.进入设置
      2.向上滑动屏幕      
    '''

    # def testMove_to(self):
    #     list= self.driver.find_elements_by_id("android:id/title")
    #     for i in list:
    #         print(i.text)
    #     # 定位到存储
    #     el2 = self.driver.find_element_by_xpath("//*[contains(@text,'更多')]")
    #     print(el2.text)
    #     #定位到更多
    #     el1 = self.driver.find_element_by_xpath("//*[contains(@text,'应用')]")
    #     # print(el1.text)
    #     # 元素方式滑动
    #     #TouchAction(self.driver).press(el2).move_to(el1).release().perform()
    #
    #
    #     # 坐标的方式滑动
    #     TouchAction(self.driver).press(x=240,y=600).wait(100).move_to(x=100,y=100).release().perform()

    # drag_and_drop拖拽事件
    # def testdrag_and_drop(self):
    #     el1 = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
    #     el2 = self.driver.find_element_by_xpath("//*[contains(@text,'应用')]")
    #     self.driver.drag_and_drop(el2,el1)
    #     # 注意 这次使用drag_and_drop方法，传入的"存储定位"仍使用其原始在屏幕上的位置，所以是由存储滑动到用户才可以上滑，否则需要重新"定位存储"
    #     # 存储上滑倒用户位置
    #     sleep(5)
    #     el3 = self.driver.find_element_by_xpath("//*[contains(@text,'安全')]")
    #     self.driver.drag_and_drop(el3,el2)
    #     # 点击安全按钮
    #     self.driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
    #     # # 点击屏幕锁定方式按钮
    #     self.driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
    #     # # 点击图案按钮
    #     self.driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()
    #
    #     # 绘制图案四个坐标 1:(80,256) 2:(240,256) 3:(240,418) 4:(400,418)
    #     TouchAction(self.driver).press(x=80, y=256).wait(100).move_to(x=160, y=0).wait(100) \
    #         .move_to(x=0, y=162).wait(100).move_to(x=160, y=0).release().perform()

    # 解锁
    # def testlogin_unlock(self):
    #     el1 = self.driver.find_element_by_xpath("//*[contains(@text,'WLAN')]")
    #     el2 = self.driver.find_element_by_xpath("//*[contains(@text,'应用')]")
    #     self.driver.drag_and_drop(el2,el1)
    #     # 注意 这次使用drag_and_drop方法，传入的"存储定位"仍使用其原始在屏幕上的位置，所以是由存储滑动到用户才可以上滑，否则需要重新"定位存储"
    #     # 存储上滑倒用户位置
    #     sleep(5)
    #     el3 = self.driver.find_element_by_xpath("//*[contains(@text,'安全')]")
    #     self.driver.drag_and_drop(el3,el2)
    #     # 点击安全按钮
    #     self.driver.find_element_by_xpath("//*[contains(@text,'安全')]").click()
    #     # # 点击屏幕锁定方式按钮
    #     self.driver.find_element_by_xpath("//*[contains(@text,'屏幕锁定')]").click()
    #     # # 点击图案按钮
    #     self.driver.find_element_by_xpath("//*[contains(@text,'图案')]").click()
    #
    #
    #     # 通过ID找到九宫格的View
    #     lock_pattern = self.driver.find_element_by_id("com.android.settings:id/lockPattern")
    #     # 获取View的x,y坐标值
    #     x = lock_pattern.location.get('x')
    #     y = lock_pattern.location.get('y')
    #     # 获取View的宽度和高度
    #     width = lock_pattern.size.get('width')
    #     height = lock_pattern.size.get('height')
    #     # 偏移量
    #     offset = width / 6
    #     # 计算九宫格内九个点的x,y坐标值
    #     p11 = int(x + width / 6), int(y + height / 6)
    #     p12 = int(x + width / 2), int(y + height / 6)
    #     p13 = int(x + width - offset), int(y + height / 6)
    #     p21 = int(x + width / 6), int(y + height / 2)
    #     p22 = int(x + width / 2), int(y + height / 2)
    #     p23 = int(x + width - offset), int(y + height / 2)
    #     p31 = int(x + width / 6), int(y + height - offset)
    #     p32 = int(x + width / 2), int(y + height - offset)
    #     p33 = int(x + width - offset), int(y + height - offset)
    #     # 计算移动到下一个点的偏移量
    #     p3 = p13[0] - p11[0]
    #     sleep(3)
    #     TouchAction(self.driver).press(x=p11[0], y=p11[1]).move_to(x=p12[0],y=p12[1]).wait(1000).move_to(x=p13[0],y=p13[1]).\
    #         wait(1000).move_to(x=p23[0],y=p23[1]).wait(1000).move_to(x=p22[0],y=p22[1]).wait(1000).release().perform()

    def testAppApi(self):
        #获取当前手机的时间
        # print("系统时间："+self.driver.device_time)
        # #.获取手机的宽高
        # print(self.driver.get_window_size())
        # #发送键到设备
        # for i in range(3):
        #     self.driver.keyevent(24)
        #
        # #操作手机通知栏
        # '''
        # 业务场景:
        #   1.启动设置
        #   2.打开通知栏
        # '''
        # self.driver.open_notifications()


        #获取手机当前连接的网络
        '''
                获取当前网络的状态
                :return:
                '''
        info = {0: "NO_CONNECTION（没网络）",

                1: "AIRPLANE_MODE（飞行模式）",

                2: "WIFI_ONLY（仅wifi）",

                4: "DATA_ONLY（仅数据）",

                6: "ALL_NETWORK_ON（所有网络都打开）"}
        # network=self.driver.network_connection
        # print("获取%s",str(info.get(network)))
        #
        # #设置手机网络
        # self.driver.set_network_connection(1)

        '''
          业务场景：
          1.打开设置页面
          2.截图当前页面保存到当前目录，命名为screen.png
        '''
        #手机截图
        self.driver.get_screenshot_as_file(os.getcwd() + os.sep + './screen.png')


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
