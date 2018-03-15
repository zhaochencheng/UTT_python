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
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

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

    def enter_dnsfilter(self):
        u'''进入行为管理---域名过滤页面'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 行为管理 菜单栏定位
        behaviorMange = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[6]/div/h4/span"))
        behaviorMange.click()
        print("当前位置：", behaviorMange.text)
        # 域名过滤 定位
        dnsfilter = self.driver.find_element_by_link_text("域名过滤")
        dnsfilter.click()
        print("当前位置：", dnsfilter.text)
    def dnsfilter_open(self):
        ## 查看 域名过滤 开启状态
        status = self.driver.find_element_by_xpath(".//input[@name='DnsFilterEnable' and @value = 'on']")
        self.check_status(status)
        time.sleep(1)
        '''判断状态是否开启'''
        self.assertTrue(status.is_selected())
        #保存 定位
        save =self.driver.find_element_by_id("save")
        save.click()
        time.sleep(2)

    def dnsfilter_config(self):
        # 规则名称 定位
        DNSfiltername = self.driver.find_element_by_xpath(".//input[@name= 'DnsFilterName']")
        DNSfiltername.clear()
        DNSfiltername.send_keys(DNS_filter_rulename[0])

        # 过滤域名 定位
        for v in range(len(DNS_filter_hostname)):
            domainFilter = self.driver.find_element_by_xpath(".//input[@name= 'addHostFilter']")
            domainFilter.clear()
            domainFilter.send_keys(DNS_filter_hostname[v])
            # 新增 定位
            add = self.driver.find_element_by_id("addDns")
            add.click()
            time.sleep(1)

        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(3)
    def dnsfilter_show(self):
        u'''域名列表信息输出'''
        # 域名列表 定位
        domain_list = self.driver.find_element_by_xpath(".//select[@name = 'DnsLists']")
        list = Select(domain_list).options
        print("域名列表个数：", len(list))
        print("域名列表：")
        for domain_hosname in list:
            print(domain_hosname.text)

    def check_open_dnsfilter(self):
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
    def dnsfilter_close(self):
        # # 关闭域名过滤
        status_off = self.driver.find_element_by_xpath(".//input[@name='DnsFilterEnable' and @value = 'off']")
        status_off.click()
        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        print("关闭域名过滤！")
    def check_close_dnsfilter(self):
        # time.sleep(10)
        # # **判断关闭域名过滤后 是否生效**  # #
        for i in range(len(DNS_filter_hostname)):
            httpcode().http200("http://" + DNS_filter_hostname[i])

    # def test_18_001_dnsfilter(self):
    #     u'''域名过滤开启与关闭'''
    #     # 显示等待
    #     webwait = WebDriverWait(self.driver, 10, 1)
    #     # 行为管理 菜单栏定位
    #     behaviorMange = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[6]/div/h4/span"))
    #     behaviorMange.click()
    #     print("当前位置：", behaviorMange.text)
    #     #域名过滤 定位
    #     dnsfilter = self.driver.find_element_by_link_text("域名过滤")
    #     dnsfilter.click()
    #     print("当前位置：",dnsfilter.text)
    #
    #     # #开启域名过滤
    #     print("*" * 30, '\n')
    #     ## 查看 域名过滤 开启状态
    #     status = self.driver.find_element_by_xpath(".//input[@name='DnsFilterEnable' and @value = 'on']")
    #     self.check_status(status)
    #     #
    #     #规则名称 定位
    #     DNSfiltername = self.driver.find_element_by_xpath(".//input[@name= 'DnsFilterName']")
    #     DNSfiltername.clear()
    #     DNSfiltername.send_keys(DNS_filter_rulename[0])
    #
    #     #过滤域名 定位
    #     for v in range(len(DNS_filter_hostname)):
    #         domainFilter = self.driver.find_element_by_xpath(".//input[@name= 'addHostFilter']")
    #         domainFilter.clear()
    #         domainFilter.send_keys(DNS_filter_hostname[v])
    #         # 新增 定位
    #         add = self.driver.find_element_by_id("addDns")
    #         add.click()
    #         time.sleep(1)
    #
    #     #域名列表 定位
    #     domain_list = self.driver.find_element_by_xpath(".//select[@name = 'DnsLists']")
    #     list = Select(domain_list).options
    #     print("域名列表个数：",len(list))
    #     print("域名列表：")
    #     for domain_hosname in list:
    #         print(domain_hosname.text)
    #
    #     #保存 定位
    #     save = self.driver.find_element_by_id("save")
    #     save.click()
    #     time.sleep(3)
    #     print("开启域名过滤！")
    #     print("*" * 30, '\n')
    #
    #     # # **判断开启域名过滤 是否生效**  # #
    #     for i in range(len(DNS_filter_hostname)):
    #         httpcode().http200("http://"+DNS_filter_hostname[i])
    #
    #
    #     time.sleep(2)
    #     print("*" * 30, '\n')
    #     # # ** 删除域名列表中的某一项 查看该 域名 是否可以访问 ** # #
    #     #随机选择其中一条域名 进行删除
    #     domain_list1 = self.driver.find_element_by_xpath(".//select[@name = 'DnsLists']")
    #     delect_anyone = random.randint(0,len(DNS_filter_hostname)-1)
    #     Select(domain_list1).select_by_value(DNS_filter_hostname[delect_anyone])
    #     # 删除 定位
    #     delect = self.driver.find_element_by_id("deleteDns")
    #     delect.click()
    #     print("随机选择其中一条域名 进行删除,%s" % DNS_filter_hostname[delect_anyone])
    #     time.sleep(5)
    #     httpcode().http200("http://"+DNS_filter_hostname[delect_anyone])
    #
    #
    #     time.sleep(2)
    #     # # 关闭域名过滤
    #     print("*" * 30, '\n')
    #     status_off = self.driver.find_element_by_xpath(".//input[@name='DnsFilterEnable' and @value = 'off']")
    #     status_off.click()
    #     # 保存 定位
    #     save = self.driver.find_element_by_id("save")
    #     save.click()
    #     print("关闭域名过滤！")
    #     time.sleep(10)
    #     # # **判断关闭域名过滤后 是否生效**  # #
    #     for i in range(len(DNS_filter_hostname)):
    #         httpcode().http200("http://"+DNS_filter_hostname[i])

    def test_18_001_dnsfilter_open(self):
        u'''开启域名过滤功能'''
        #进入行为管理---域名过滤页面
        self.enter_dnsfilter()
        '''开启域名过滤功能'''
        self.dnsfilter_open()
        print("开启域名过滤功能")
        '''#开启域名后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("dnsfilter_open")
    def test_18_002_dnsfilter_config(self):
        u'''配置域名过滤'''
        #进入行为管理---域名过滤页面
        self.enter_dnsfilter()
        '''配置域名过滤'''
        self.dnsfilter_config()
        print("域名过滤配置完成")
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("dnsfilter_config")
    def test_18_003_dnsfilter_show(self):
        u'''域名配置信息输出'''
        # 进入行为管理---域名过滤页面
        self.enter_dnsfilter()
        '''域名配置信息输出'''
        self.dnsfilter_show()
        print("域名过滤列表输出完成")
        '''#输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("dnsfilter_show")
    def test_18_004_dnsfilter_validate(self):
        u'''域名过滤功能验证'''
        #域名配置信息输出
        self.enter_dnsfilter()
        '''域名过滤功能验证'''
        self.check_open_dnsfilter()
    def test_18_005_dnsfilter_close(self):
        u'''域名过滤功能关闭'''
        #域名配置信息输出
        self.enter_dnsfilter()
        '''域名过滤功能关闭'''
        self.dnsfilter_close()
        print("域名过滤功能关闭")
        '''#输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("dnsfilter_close")
    def test_18_006_dnsfilter_close_check(self):
        u'''域名过滤关闭功能验证'''
        '''域名过滤关闭功能验证'''
        self.check_close_dnsfilter()








if __name__ == '__main__':
    unittest.main()
