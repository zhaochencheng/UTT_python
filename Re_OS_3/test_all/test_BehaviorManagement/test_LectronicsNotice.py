# -*- coding: utf-8 -*-
# @Time    : 2018/2/2 16:44
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_LectronicsNotice.py
# @Software: PyCharm Community Edition
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
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping

class lectronicsNotice(unittest.TestCase):
    u'''**电子通告开启与关闭**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def check_status(self,status):
        if status.is_selected():
            print("电子通告已开启")
            pass
        else:
            status.click()
            print("现在开启电子通告")
    def check_lectronicsNotice(self):
        self.driver1 = webdriver.Chrome()
        self.driver1.get("http://www.163.com")
        self.driver1.implicitly_wait(4)
        print(self.driver1.current_url)
        if url in self.driver1.current_url:
            print("电子通告生效")
            print("当前网页标题为:",self.driver1.title)
            print("*" * 30, '\n')
        else:
            raise BaseException("电子通告不生效！")

    def test_20_001_lectronicsNotice(self):
        u'''电子通告开启与关闭'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 行为管理 菜单栏定位
        behaviorMange = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[6]/div/h4/span"))
        behaviorMange.click()
        print("当前位置：", behaviorMange.text)
        #电子通告 定位
        lectronicsNotice = self.driver.find_element_by_link_text("电子通告")
        lectronicsNotice.click()
        print("当前位置：",lectronicsNotice.text)

        # # ** 配置电子通告** # #

        #规则名称 定位
        print("*" * 30, '\n')
        rulename = self.driver.find_element_by_xpath(".//input[@name = 'rulename']")
        rulename.clear()
        rulename.send_keys("123")
        #判断 状态---若未开启，则开启
        status = self.driver.find_element_by_xpath(".//input[@name='status' and @ value='on']")
        self.check_status(status)
        #保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(2)
        # # * *  判断电子通告是否开启  * * # #
        self.check_lectronicsNotice()


        #　# ** 关闭电子通告*　*# #
        time.sleep(2)
        status_off = self.driver.find_element_by_xpath(".//input[@name='status' and @ value='off']")
        status_off.click()
        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        print("现在关闭电子通告！")
        print("*" * 30, '\n')



if __name__ == '__main__':
    unittest.main()