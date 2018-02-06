# -*- coding: utf-8 -*-
# @Time    : 2018/2/6 21:54
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_System_maintenance.py
# @Software:PyCharm
from datetime import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time,random
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_sameConfig import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping

class System_maintenance(unittest.TestCase):
    u'''**系统维护**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_32_001_System_upgrade(self):
        u'''系统升级操作'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：",Sysconfig.text)
        #系统维护 定位
        system_maintenance = self.driver.find_element_by_link_text("系统维护")
        system_maintenance.click()
        print("当前位置：",system_maintenance.text)
        #系统升级页面定位
        system_upgrade = self.driver.find_element_by_link_text("系统升级")
        system_upgrade.click()
        print("当前位置：",system_upgrade.text)
        #软件版本 定位
        softwareVersion = self.driver.find_element_by_xpath(".//input[@name = 'softwareVersion1']")
        version = softwareVersion.get_attribute("value")
        print("软件版本为：",version)
        # time.sleep(4)
        # self.driver.refresh()
        # time.sleep(10)
        #版本检测情况
        check_version = self.driver.find_element_by_xpath("//*[@id='iframe1']/table/tbody/tr[2]/td[3]/span")
        print("版本检查情况：",check_version.text)
        #输入 软件
        # send_software = self.driver.find_element_by_name("updatesoftware")
        #     # .send_keys("//*[@id='iframe1']/table/tbody/tr[3]/td[2]/input[2]")
        # send_software.send_keys("‪C:\\Users\\zcc\\Desktop\\123.txt")

if __name__ == '__main__':
    unittest.main()



