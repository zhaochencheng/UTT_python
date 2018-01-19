# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 16:25
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : wan_config.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Config_data.config import *

class Wan_config():
    def __init__(self,driver):
        self.driver = driver
    def wan1_static(self):
        driver = self.driver
        #引入Login 公共类
        Login(self.driver).login_router(url,username,pwd)
        time.sleep(3)
        #网络配置 定位
        netconfig = driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span")
        netconfig.click()
        print("当前位置：",netconfig.text)
        #外网配置定位
        wan_config = driver.find_element_by_link()







if __name__ == '__main__':
    driver = webdriver.Chrome()
    Wan_config(driver).wan1_static()
    time.sleep(3)
    driver.quit()

