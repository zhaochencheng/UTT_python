# -*- coding: utf-8 -*-
# @Time    : 2018/2/8 17:07
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_Application_priority.py
# @Software: PyCharm Community Edition
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_sameConfig import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.Ping import Ping

class Application_priority(unittest.TestCase):
    u'''**应用优先**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def check_imgopen(self,location):
        u'''检查应用优先总开关 是否开启'''
        if location.get_attribute("checktype") == "0" :
            print(location.get_attribute("checktype"))
            print("应用优先总开关 -- 未开启！")
            print("现在开启")
            location.click()
            time.sleep(3)
        else:
            print("应用优先总开关 -- 已开启！")

    def select_apptype(self,location):
        l = Select(location).options
        for i in range(len(l)):
            name = l[i].text
            print("%d:" % i, name)
            if name == '自定义':
                pass
            else:
                Select(location).select_by_index(i)
                # 确定 定位
                changeAppType = self.driver.find_element_by_id("changeAppType")
                changeAppType.click()
                time.sleep(2)
                #输出配置的 模板样式
                # Output_info(self.driver).output_all()
                time.sleep(2)





    def test_21_001_Application_priority(self):
        u'''应用管理开启-操作-关闭'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #流量管理 菜单栏 定位
        trafficManagement = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[7]/div/h4/span"))
        trafficManagement.click()
        print("当前位置:",trafficManagement.text)
        #应用优先 定位
        app_priority =self.driver.find_element_by_link_text("应用优先")
        app_priority.click()
        print("当前位置:",app_priority.text)
        #检查应用优先总开关 是否开启
        img = self.driver.find_element_by_id("checkOpen")
        self.check_imgopen(img)
        time.sleep(2)

        #选择应用场景:
        apptype = self.driver.find_element_by_xpath(".//select[@name='appType']")
        # self.select_apptype(apptype)
        l = Select(apptype).options
        # print(len(l))
        for i in range(len(l)):
            # print(l[i])
            name = l[i].text
            print("%d:" % i, name)
            Select(apptype).select_by_index(i)
            time.sleep(3)
            if name == '自定义':
                pass
            else:
                # apptype = self.driver.find_element_by_xpath(".//select[@name='appType']")
                # Select(apptype).select_by_index(i)
                # 确定 定位
                changeAppType = self.driver.find_element_by_id("changeAppType")
                changeAppType.click()
                time.sleep(2)
                # 输出配置的 模板样式
                # Output_info(self.driver).output_all()
                time.sleep(2)
            # if name == '娱乐优先':
            #     Select(apptype).select_by_index(i)
            #     # 确定 定位
            #     changeAppType = self.driver.find_element_by_id("changeAppType")
            #     changeAppType.click()
            #     time.sleep(2)
            #     # 输出配置的 模板样式
            #     # Output_info(self.driver).output_all()
            #     time.sleep(2)









if __name__ == '__main__':
    unittest.main()