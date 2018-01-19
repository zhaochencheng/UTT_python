# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 20:39
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_wan_config.py
# @Software: PyCharm Community Edition
import unittest
from selenium import webdriver
import time
#导入Select 模块
from selenium.webdriver.support.select import Select
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Config_data.config import *

class Wan_config(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_wan_config(self):
        #网络配置  定位
        netconfig = self.driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span")
        netconfig.click()
        print("当前位置：",netconfig.text)
        #外网配置 定位
        wan_config = self.driver.find_element_by_link_text("外网配置")
        wan_config.click()
        print("当前位置：",wan_config.text)
        #wan 口编辑按钮  定位
        edit = self.driver.find_element_by_class_name("glyphicon-edit")
        edit.click()

        #连接类型定位  ----选择 固定接入
        connType = self.driver.find_element_by_xpath(".//select[@name ='connectionType']")
        Select(connType).select_by_value("STATIC")
        #ip 地址
        IP = self.driver.find_element_by_xpath(".//input[@name = 'staticIp']")
        IP.clear()
        IP.send_keys(wan_ip)
        #子网掩码
        Static_netmark = self.driver.find_element_by_xpath(".//input[@name = 'staticNetmask']")
        Static_netmark.clear()
        Static_netmark.send_keys(netmask)
        #网关地址
        GateWay = self.driver.find_element_by_xpath(".//input[@name = 'staticGateway']")
        GateWay.clear()
        GateWay.send_keys(GWaddr)
        # 主DNS
        DNS = self.driver.find_element_by_xpath(".//input[@name = 'staticPriDns']")
        DNS.clear()
        DNS.send_keys(DNSaddr)
        #保存
        Save_button = self.driver.find_element_by_xpath(".//button[@id='save']")
        Save_button.click()
        time.sleep(10)
        #判断页面显示wan口ip 与 配置的wan口ip是否相同；
        web_ip = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[3]/span").text
        self.assertEqual(web_ip,wan_ip)




if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(Wan_config("test_wan_config"))
    runner = unittest.TextTestRunner()
    runner.run(suit)






