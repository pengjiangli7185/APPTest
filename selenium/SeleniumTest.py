# coding = utf-8
# @Time : 2021/7/9 16:31
# @Author : pengjiangli
# @File : SeleniumTest.py
# @Software: PyCharm
# @contact: 292617625@qq.com
from time import sleep

from selenium import webdriver

driver = webdriver.Firefox()
#用30秒隐式等待时间
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("https://login.deeptel.com.cn/")
# get the search textbox
search_field = driver.find_element_by_name("username")
# search_field.clear()
# # enter search keyword and submit
search_field.send_keys("goodtom")
# search_field.submit()
driver.find_element_by_name("password").send_keys("duo123456")

submit=driver.find_elements_by_class_name('submit')
print("submit:%s",submit)
submit[0].click()

sleep(5)
huiyan=driver.find_element_by_xpath("//li[contains(text(),'会员')]")
print("huiyan:%s",huiyan)
huiyan.click()

sleep(5)
driver.switch_to.frame("iframeMain")
sleep(10)
xinzenhuiyun=driver.find_element_by_xpath("//div/a/p[contains(text(),'新增会员')]")
xinzenhuiyun.click()
sleep(5)


#新增会员功能
addMember=driver.find_elements_by_xpath("//div[@class='el-form-item__content']/ul[@class='clearfix']//li");
#选择白银仔
for i in addMember:
    print(i.text)
addMember[2].click()



phone=driver.find_element_by_xpath("//div/input[@placeholder='请输入手机号']")
phone.send_keys("13610102325")

pay=driver.find_element_by_xpath("//div[contains(text(),'现金支付')]")
pay.click()

driver.find_element_by_xpath("//button/span[contains(text(),' 确定')]").click()

print("新增会员结束")





