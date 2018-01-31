# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 13:55
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_Netname.py
# @Software: PyCharm Community Edition
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Config_data.config import *

class Netname_config(unittest.TestCase):
    u'''**网络名称配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def check_wirless(self,num):
        #点击无线扩展--网络名称/设备管理-- 判断页面是否有弹窗，来开启无线扩展功能
        #num 为有弹窗页面的div 标签数；
        # div = self.driver.find_elements_by_xpath("/html/body/div")
        # 发现有弹窗时（未开启无线扩展功能），div标签数为2；---无弹窗时（已开启无线扩张功能），div标签数为 1；
        if num > 1:
            cfm_nox = self.driver.find_element_by_xpath("//*[@id='u-cfm-nox']")
            print("*" * 30, '\n')
            print("当前无线扩展功能为关闭状态，是否开启？")
            # 点击确认  开启无线扩展功能
            ok = self.driver.find_element_by_id("u-cfm-ok")
            ok.click()
            print("现在开启！")
            time.sleep(2)
            print("*" * 30, '\n')
        else:
            print("*" * 30, '\n')
            print("当前无线扩展功能为开启状态")


    def test_07_001_natname_config(self):
        u'''网络名称配置与删除'''

        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #无线扩展 定位
        wirelessExtension = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[4]/div/h4/span"))
        wirelessExtension.click()
        print("当前位置：",wirelessExtension.text)
        #网络名称 定位
        netname = self.driver.find_element_by_link_text("网络名称")
        netname.click()
        print("当前位置：",netname.text)
        time.sleep(2)
        #判断无线扩展是否开启---
        div = self.driver.find_elements_by_xpath("/html/body/div")
        print("div个数：",len(div))
        self.check_wirless(len(div))


        for i in range(len(net_name)):
            # 点击新增
            add = self.driver.find_element_by_id("add")
            add.click()
            time.sleep(2)
            #网络名称 定位
            add_natname = self.driver.find_element_by_xpath(".//input[@name='zoneName']")
            add_natname.clear()
            add_natname.send_keys(new_rulename[i])
            #ssid 定位
            add_ssid = self.driver.find_element_by_xpath(".//input[@name='ssid']")
            add_ssid.clear()
            add_ssid.send_keys(ssid[i])
            #
            next_tab = self.driver.find_element_by_xpath(".//button[@id='next_tab']")
            next_tab.click()
            time.sleep(2)
            next_tab.click()
            time.sleep(2)
            #保存 定位
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(3)




if __name__ == '__main__':
    unittest.main()
