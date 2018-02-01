# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 18:49
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_Dns_dnsFilter.py
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

class DNS_filter(unittest.TestCase):
    u'''**域名过滤开启与关闭**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def check_status(self,status):
        if status.is_selected():
            print("域名过滤已开启")
            pass
        else:
            status.click()
            print("现在开启域名过滤")

    def test_18_001_dnsfilter(self):
        u'''域名过滤开启与关闭'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 行为管理 菜单栏定位
        behaviorMange = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[6]/div/h4/span"))
        behaviorMange.click()
        print("当前位置：", behaviorMange.text)
        #域名过滤 定位
        dnsfilter = self.driver.find_element_by_link_text("域名过滤")
        dnsfilter.click()
        print("当前位置：",dnsfilter.text)

        # #开启域名过滤

        ## 查看状态
        status = self.driver.find_element_by_xpath(".//input[@name='DnsFilterEnable' and @value = 'on']")
        self.check_status(status)
        #规则名称 定位
        DNSfiltername = self.driver.find_element_by_xpath(".//input[@name= 'DnsFilterName']")
        DNSfiltername.clear()
        DNSfiltername.send_keys(DNS_filter_rulename[0])

        #过滤域名 定位
        domainFilter = self.driver.find_element_by_xpath(".//input[@name= 'addHostFilter']")
        domainFilter.clear()
        domainFilter.send_keys(DNS_filter_hostname[0])
        # 新增 定位
        add = self.driver.find_element_by_id("addDns")
        add.click()
        #
        domain_list = self.driver.find_element_by_xpath(".//select[@name = 'DnsLists']")
        list = Select(domain_list).options
        print("域名列表：",len(list))
        for domain_hosname in list:
            print(domain_hosname.text)



if __name__ == '__main__':
    unittest.main()