# coding = utf-8
# @Time : 2021/7/9 16:41
# @Author : pengjiangli
# @File : ChromeTest.py
# @Software: PyCharm
# @contact: 292617625@qq.com
# get the path of chromedriver
import os

from selenium import webdriver

dir = os.path.dirname(__file__)
chrome_driver_path = dir + "\chromedriver.exe"
# remove the .exe extension on linux or mac platform
# create a new Chrome session
driver = webdriver.Chrome(chrome_driver_path)
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("https://www.baidu.com/")
# get the search textbox
search_field = driver.find_element_by_name("wd")
search_field.clear()
# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()
# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpathmethod
products = driver.find_elements_by_xpath("//h2[@class='product-name']/a")

# get the number of anchor elements found
print ("Found " + str(len(products)) + " products: ")
# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print (product.text)
# close the browser window
driver.quit()