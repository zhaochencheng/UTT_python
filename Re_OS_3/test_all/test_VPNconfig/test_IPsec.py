# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 13:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_IPsec.py
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

class IPSec(unittest.TestCase):
    u'''**IPSec配置与操作**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_26_001_IPsec(self):
        u'''IPsec配置--对方动态连接到本地'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #VPN配置 定位
        VPN = webwait.until(lambda x:x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
        VPN.click()
        print("当前位置：",VPN.text)
        #IPSec 定位
        IPSec= self.driver.find_element_by_link_text("IPSec")
        IPSec.click()
        print("当前位置：",IPSec.text)
        # 配置前 先测试一下是否可以ping 同对端内网
        try:
            Ping().ping_IP(remoteip[0])
        except BaseException as E:
            if E:
                print("未配置VPN，无法ping同该ip")
            else:
                raise BaseException("功能生效不生效；")

        # #　* 配置VPN * # #
        #新增 定位
        time.sleep(2)
        add = self.driver.find_element_by_id("add")
        add.click()
        #连接方式
        conntype= self.driver.find_element_by_xpath(".//select[@name = 'connType']")
        Select(conntype).select_by_visible_text("对方动态连接到本地")
        #隧道名称
        ids = self.driver.find_element_by_xpath(".//input[@name='ids']")
        ids.clear()
        ids.send_keys(tunnelName[0])
        #远端内网地址
        remoteAddr = self.driver.find_element_by_xpath(".//input[@name = 'remoteAddr']")
        remoteAddr.clear()
        remoteAddr.send_keys(remoteip[0])

        #预共享密钥
        preshareKey = self.driver.find_element_by_xpath(".//input[@name = 'preshareKey']")
        preshareKey.clear()
        preshareKey.send_keys(shareKey[0])

        # 保存
        save =self.driver.find_element_by_id("save")
        save.click()
        # #

        #输出页面 隧道列表 信息
        Output_info(self.driver).output_all()

        #判断配置VPN 后是否生效
        Ping().ping_IP(remoteip[0])

        # 删除刚配置的 VPN
        # ----在这提出 前端页面 格式一会带id 一会不带id 套用随意  导致公共函数不能使用；



        #
    def test_26_002_IPsec(self):
        u'''IPsec配置--动态连接到网关'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # VPN配置 定位
        VPN = webwait.until(lambda x: x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
        VPN.click()
        print("当前位置：", VPN.text)
        # IPSec 定位
        IPSec = self.driver.find_element_by_link_text("IPSec")
        IPSec.click()
        print("当前位置：", IPSec.text)
        # 配置前 先测试一下是否可以ping 同对端内网
        # try:
        #     Ping().ping_IP(remoteip[0])
        # except BaseException as E:
        #     if E:
        #         print("未配置VPN，无法ping同该ip")
        #     else:
        #         raise BaseException("功能生效不生效；")

        # #　* 配置VPN * # #
        # 新增 定位
        time.sleep(2)
        add = self.driver.find_element_by_id("add")
        add.click()
        # 连接方式
        conntype = self.driver.find_element_by_xpath(".//select[@name = 'connType']")
        Select(conntype).select_by_visible_text("动态连接到网关")
        # 隧道名称
        ids = self.driver.find_element_by_xpath(".//input[@name='ids']")
        ids.clear()
        ids.send_keys(tunnelName[1])
        #远端网关地址（域名）
        peer = self.driver.find_element_by_xpath(".//input[@name = 'peer']")
        peer.clear()
        peer.send_keys(peerip[1])

        # 远端内网地址
        remoteAddr = self.driver.find_element_by_xpath(".//input[@name = 'remoteAddr']")
        remoteAddr.clear()
        remoteAddr.send_keys(remoteip[1])

        # 预共享密钥
        preshareKey = self.driver.find_element_by_xpath(".//input[@name = 'preshareKey']")
        preshareKey.clear()
        preshareKey.send_keys(shareKey[1])

        # 保存
        save = self.driver.find_element_by_id("save")
        save.click()
        # #

        # 输出页面 隧道列表 信息
        Output_info(self.driver).output_all()

        # 判断配置VPN 后是否生效
        # Ping().ping_IP(remoteip[1])

        # 删除刚配置的 VPN
        # ----在这提出 前端页面 格式一会带id 一会不带id 套用随意  导致公共函数不能使用；



        #



if __name__ == '__main__':
    unittest.main()