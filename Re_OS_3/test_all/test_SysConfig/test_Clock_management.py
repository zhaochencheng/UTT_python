# -*- coding: utf-8 -*-
# @Time    : 2018/2/6 21:16
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_Clock_management.py
# @Software: PyCharm
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

class Clock_management(unittest.TestCase):
    u'''**时钟管理**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def check_status(self,location):
        u'''检查radio 标签是否被选中'''
        if location.is_selected():
            print("*" * 30, '\n')
            print("已选中该操作！")

        else:
            location.click()
            print("*" * 30, '\n')
            print("现该操作未被选中，现在选中")
            time.sleep(1)
            # 保存定位
            save = self.driver.find_element_by_id("save")
            save.click()

    def check_serverip(self,location):
        u'''检查服务器地址 ip是否为空，非空 则输出；空，则赋值'''
        NTPServer1_IP = location.get_attribute("value")
        if NTPServer1_IP is None:
            location.clear()
            ip  = NtpServerip[random.randint(0,len(NtpServerip)-1)]
            location.send_keys(ip)
        else:
            print("服务器 IP地址为：",NTPServer1_IP)


    def test_31_001_Clock_management(self):
        u'''时钟管理的配置'''

        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：",Sysconfig.text)
        #时钟管理 定位
        clock = self.driver.find_element_by_link_text("时钟管理")
        clock.click()
        print("当前位置：",clock.text)
        date = self.driver.find_element_by_id("dates")
        times = self.driver.find_element_by_id("times")
        print("系统当前时间：",date.text," ",times.text)
        print("电脑当前时间：",time.ctime())
        #网络时间同步 定位
        clock_net = self.driver.find_element_by_xpath(".//input[@name='SntpEnable' and @value='on']")
        self.check_status(clock_net)
        #服务器1 ip 定位
        NTPServer1 = self.driver.find_element_by_xpath(".//input[@name = 'NTPServerIP']")
        #检查服务器地址 ip是否为空，非空 则输出；空，则赋值
        self.check_serverip(NTPServer1)

        #服务器2 ip 定位
        NTPServer2 = self.driver.find_element_by_xpath(".//input[@name = 'server2']")
        self.check_serverip(NTPServer2)

        #服务器3 ip 定位
        NTPServer3 = self.driver.find_element_by_xpath(".//input[@name = 'server3']")
        self.check_serverip(NTPServer3)

        #保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        print("点击保存！")
        time.sleep(2)

        date_save = self.driver.find_element_by_id("dates")
        times_save = self.driver.find_element_by_id("times")
        print("系统当前时间：",date_save.text," ",times_save.text)
        print("电脑当前时间：",time.ctime())







if __name__ == '__main__':
    unittest.main()