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
from Re_OS_3.Public.Delect_Config import Delect_config
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

    def switch_check_open(self,state):
        u"0代表关闭,1代表开启"
        # 策略路由开关按钮 定位
        checkopen = self.driver.find_element_by_id("checkOpen")
        checkopen_status = int(checkopen.get_attribute("checktype"))
        # print("checkopen_status:",checkopen_status,type(checkopen_status))
        # print("state:",state,type(state))
        if checkopen_status == state:
            print("no operation")
            pass
        else:
            checkopen = self.driver.find_element_by_id("checkOpen")
            checkopen.click()
            print("操作按钮")
        time.sleep(2)
    def enter_app_priority(self):
        u'''进入流量管理---应用优先页面'''

        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 流量管理 菜单栏 定位
        trafficManagement = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[7]/div/h4/span"))
        trafficManagement.click()
        print("当前位置:", trafficManagement.text)
        # 应用优先 定位
        app_priority = self.driver.find_element_by_link_text("应用优先")
        app_priority.click()
        print("当前位置:", app_priority.text)




    def test_21_001_Application_priority(self):
        u'''应用管理开启-操作-关闭'''
        #
        self.enter_app_priority()

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

    def test_21_001_Application_priority_open(self):
        u"应用管理--开启"
        #进入流量管理---应用优先页面
        self.enter_app_priority()
        #开启应用优先按钮
        #0代表关闭,1代表开启
        self.switch_check_open(1)
        '''判断按钮是否开启'''
        checkopen = self.driver.find_element_by_id("checkOpen")
        checktype = checkopen.get_attribute("checktype")
        self.assertEqual(int(checktype),1,"按钮当前状态为关闭状态；开启功能--失败！！")
        print("现在已开启--应用优先 功能")
    def test_21_002_Application_priority_Office_priority_config(self):
        u'''办公优先配置'''
        # 进入流量管理---应用优先页面
        self.enter_app_priority()
        #选择办公优先
        # 选择应用场景:
        apptype = self.driver.find_element_by_xpath(".//select[@name='appType']")
        Select(apptype).select_by_visible_text("办公优先")
        # 确定 定位
        changeAppType = self.driver.find_element_by_id("changeAppType")
        changeAppType.click()
    def test_21_002_Application_priority_Office_priority_show(self):
        u'''办公优先配置页面内容输出'''
        # 进入流量管理---应用优先页面
        self.enter_app_priority()
        #输出页面内容
        Output_info(self.driver).output_all()
    def test_21_002_Application_priority_Office_priority_validate(self):
        u'''办公优先配置 功能生效'''
        pass
    def test_21_002_Application_priority_Office_priority_delect(self):
        u'''办公优先配置删除'''
        # 进入流量管理---应用优先页面
        self.enter_app_priority()
        #删除 办公优先配置
        Delect_config(self.driver).delect_all_config()





















if __name__ == '__main__':
    unittest.main()