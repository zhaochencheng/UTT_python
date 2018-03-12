# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 13:55
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_PPTP.py
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
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class PPTP(unittest.TestCase):
    u'''**PPTP配置与操作**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def enter_pptp(self):
        u'''进入VPN配置--PPTP/L2TP页面'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # VPN配置 定位
        VPN = webwait.until(lambda x: x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
        VPN.click()
        print("当前位置：", VPN.text)
        # PPTP/L2TP页面 定位
        pptp = self.driver.find_element_by_link_text("PPTP/L2TP")
        pptp.click()
        print("当前位置：",pptp.text)

    def open_pptp_server(self):
        u'''开启pptp服务器'''
        self.enter_pptp()
        #pptp服务器全局配置
        PPTP_server_global_configuration= self.driver.find_element_by_link_text("PPTP服务器全局配置")
        PPTP_server_global_configuration.click()
        print("当前位置：",PPTP_server_global_configuration.text)
        time.sleep(2)
        #判断 服务器状态是否开启
        state_open = self.driver.find_element_by_xpath(".//input[@name = 'enable' and @value = 'ENABLE']")
        if state_open.is_selected():
            print("目前状态为开启状态")
        else:
            state_open.click()
            print("现在开启PPTP服务器")
        #地址池起始地址
        poolStart = self.driver.find_element_by_xpath(".//input[@name = 'poolStart']")
        print("地址池起始地址:",poolStart.get_attribute("value"))
        #最大连接数
        poolCount = self.driver.find_element_by_xpath(".//input[@name = 'poolCount']")
        print("最大连接数 :",poolCount.get_attribute("value"))
        #服务器端IP地址
        localIp = self.driver.find_element_by_xpath(".//input[@name = 'localIp']")
        print("服务器端IP地址:",localIp.get_attribute("value"))
        #主DNS服务器
        priDns = self.driver.find_element_by_xpath(".//input[@name = 'priDns']")
        priDns.clear()
        priDns.send_keys("114.114.114.114")
        #保存定位
        save = self.driver.find_element_by_id("save")
        save.click()

    def PPTP_config(self):
        u'''PPTP配置'''


    def test_27_001_PPTP_server_config(self):
        u'''PPTP服务器配置'''
        #开启PPTP服务器
        self.open_pptp_server()
    def test_27_002_PPTP_config(self):
        u'''PPTP配置'''
        pass