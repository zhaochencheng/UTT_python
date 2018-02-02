# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 18:49
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_Dns_dnsFilter.py
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
from Re_OS_3.Public.Delect_sameConfig import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
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
        print("*" * 30, '\n')
        ## 查看 域名过滤 开启状态
        status = self.driver.find_element_by_xpath(".//input[@name='DnsFilterEnable' and @value = 'on']")
        self.check_status(status)
        #
        #规则名称 定位
        DNSfiltername = self.driver.find_element_by_xpath(".//input[@name= 'DnsFilterName']")
        DNSfiltername.clear()
        DNSfiltername.send_keys(DNS_filter_rulename[0])

        #过滤域名 定位
        for v in range(len(DNS_filter_hostname)):
            domainFilter = self.driver.find_element_by_xpath(".//input[@name= 'addHostFilter']")
            domainFilter.clear()
            domainFilter.send_keys(DNS_filter_hostname[v])
            # 新增 定位
            add = self.driver.find_element_by_id("addDns")
            add.click()
            time.sleep(1)

        #域名列表 定位
        domain_list = self.driver.find_element_by_xpath(".//select[@name = 'DnsLists']")
        list = Select(domain_list).options
        print("域名列表个数：",len(list))
        print("域名列表：")
        for domain_hosname in list:
            print(domain_hosname.text)

        #保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(3)
        print("开启域名过滤！")
        print("*" * 30, '\n')

        # # **判断开启域名过滤 是否生效**  # #
        for i in range(len(DNS_filter_hostname)):
            httpcode().http200("http://"+DNS_filter_hostname[i])


        time.sleep(2)
        print("*" * 30, '\n')
        # # ** 删除域名列表中的某一项 查看该 域名 是否可以访问 ** # #
        #随机选择其中一条域名 进行删除
        domain_list1 = self.driver.find_element_by_xpath(".//select[@name = 'DnsLists']")
        delect_anyone = random.randint(0,len(DNS_filter_hostname)-1)
        Select(domain_list1).select_by_value(DNS_filter_hostname[delect_anyone])
        # 删除 定位
        delect = self.driver.find_element_by_id("deleteDns")
        delect.click()
        print("随机选择其中一条域名 进行删除,%s" % DNS_filter_hostname[delect_anyone])
        time.sleep(5)
        httpcode().http200("http://"+DNS_filter_hostname[delect_anyone])


        time.sleep(2)
        # # 关闭域名过滤
        print("*" * 30, '\n')
        status_off = self.driver.find_element_by_xpath(".//input[@name='DnsFilterEnable' and @value = 'off']")
        status_off.click()
        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        print("关闭域名过滤！")
        time.sleep(10)
        # # **判断关闭域名过滤后 是否生效**  # #
        for i in range(len(DNS_filter_hostname)):
            httpcode().http200("http://"+DNS_filter_hostname[i])



if __name__ == '__main__':
    unittest.main()
