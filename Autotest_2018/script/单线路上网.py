#!/usr/bin/env python
#coding:utf-8

import os
import unittest
import time

from selenium.webdriver.support.ui import Select

from Autotest_2018.public_script.function_public import *


class 单线路_固定IP上网(unittest.TestCase):
    #class静态参数
    #
    #配置参数获取
    #
    Wan_ip = get_data("wan_Config","static_ip")
    Gateway = get_data("wan_Config","gateway")
    PriDns = get_data("wan_Config","pridns")

    def setUp(self):
        pass 

    def tearDown(self):
        pass

    def test_上网配置(self):
        
        #
        #vlan 配置
        #
        #vlan_config(2,"2",1,"2_3_4")
        #
        #登录web页面
        #
        driver = Login_web()
        driver.implicitly_wait(10)

        #
        #配置固定IP地址上网
        #
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
        driver.find_element_by_link_text(u"外网配置").click()
        driver.find_element_by_css_selector("span.glyphicon.glyphicon-edit").click()
        Select(driver.find_element_by_name("connectionType")).select_by_visible_text(u"固定接入")
        driver.find_element_by_name("staticIp").clear()
        driver.find_element_by_name("staticIp").send_keys(self.Wan_ip)
        driver.find_element_by_name("staticPriDns").clear()
        driver.find_element_by_name("staticPriDns").send_keys(self.PriDns)
        driver.find_element_by_id("save").click()
        #
        #等待配置返回页面
        #
        for i in range(1,10):
            flag = True
            try:
                driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[2]")
            except:
                flag=False
            time.sleep (1)
            if i==9:
                self.fail()
                driver.quit()
                return
            #
            #判断WAN口连接状态与WAN口IP地址是否正确
            #                        
            if flag:
                driver.find_element_by_link_text(u"外网配置").click()
                Wan_stat = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[2]").text
                Wan_addr = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[3]").text
                Wan_type = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[4]").text
                if Wan_stat == "已连接" and Wan_addr == self.Wan_ip:
                    print("WAN口接入方式：" + Wan_type)
                    print("WAN口状态：" + Wan_stat)
                    print("WAN口IP地址：" + Wan_addr)
                    driver.quit()
                    return

    def test_Cli验证(self):
        #
        #NAT规则检查
        #
        for i in range(1,5):
            if i == 4:
                self.fail()
            NAT_flag = telnet('iptables -t nat -S wan1_default_nat |grep SNAT','-j SNAT --to-source '+self.Wan_ip)
            if NAT_flag is None:
                pass
            else:
                print("NAT规则检查 pass！")
                return

    def test_上网测试(self):
        #
        #测试ping外网
        #
        icmp_result=os.system('ping www.qq.com.cn -n 3 -w 1')
        if icmp_result:
            print ('ping测试 fail！')
            self.fail()
        else:
            print ('ping测试 pass！')

        #
        #测试打开网页
        #
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 

        self.driver.get("http://www.baidu.com")  
        try:  
            assert '百度一下，你就知道' in self.driver.title
            print ('打开网页测试 pass！')  
        except Exception as e:  
            print ('打开网页测试 fail！')  
            self.fail()
        time.sleep(1)
        self.driver.quit()


class 单线路_动态IP上网(unittest.TestCase):
    #class静态参数
    #
    Wan_ip = get_data("wan_Config","static_ip")

    def setUp(self):
        pass 

    def tearDown(self):
        pass

    def test_上网配置(self):
        
        #
        #vlan 配置
        #
        #vlan_config(2,"2",1,"2_3_4")
        #
        #登录web页面
        #
        driver = Login_web()
        driver.implicitly_wait(10)

        #
        #配置动态IP地址上网
        #
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
        driver.find_element_by_link_text(u"外网配置").click()
        driver.find_element_by_css_selector("span.glyphicon.glyphicon-edit").click()
        Select(driver.find_element_by_name("connectionType")).select_by_visible_text(u"动态接入")
        driver.find_element_by_id("save").click()
        #
        #等待配置返回页面
        #
        for i in range(1,10):
            flag = True
            try:
                driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[2]")
            except:
                flag=False
            time.sleep (1)
            if i==9:
                self.fail()
                driver.quit()
                return
            #
            #判断WAN口连接状态与WAN口IP地址是否正确
            #                      
            if flag:
                driver.find_element_by_link_text(u"外网配置").click()
                Wan_stat = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[2]").text
                Wan_addr = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[3]").text
                Wan_type = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[4]").text
                if Wan_stat == "已连接" and Wan_addr.index(self.Wan_ip[:(len(self.Wan_ip) -3)]) == 0:
                    print("WAN口接入方式：" + Wan_type)
                    print("WAN口状态：" + Wan_stat)
                    print("WAN口IP地址：" + Wan_addr)
                    driver.quit()
                    return

    def test_Cli验证(self):
        #
        #NAT规则检查
        #
        NAT_flag = telnet('iptables -t nat -S wan1_default_nat ','-j MASQUERADE')

        if NAT_flag is None:
            self.fail()
        else:
            print("NAT规则检查 pass！")


    def test_上网测试(self):
        #
        #测试ping外网
        #
        icmp_result=os.system('ping www.qq.com.cn -n 3 -w 1')
        if icmp_result:
            print ('ping测试 fail！')
            self.fail()
        else:
            print ('ping测试 pass！')

        #
        #测试打开网页
        #
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 

        self.driver.get("http://www.baidu.com")  
        try:  
            assert '百度一下，你就知道' in self.driver.title
            print ('打开网页测试 pass！')  
        except Exception as e:  
            print ('打开网页测试 fail！')  
            self.fail()
        time.sleep(1)
        self.driver.quit()


class 单线路_PPPoE拨号上网(unittest.TestCase):
    #class静态参数
    #
    #配置参数获取
    #
    PPPoE_username = get_data("wan_Config","wan1_PPPoE_username")
    PPPoE_passwd = get_data("wan_Config","wan1_PPPoE_passwd")
    Wan_ip = get_data("wan_Config","PPPoE_server_iprang")
 
    def setUp(self):
        pass 

    def tearDown(self):
        pass

    def test_上网配置(self):
        
        #
        #vlan 配置
        #
        #vlan_config(2,"2",1,"2_3_4")
        #
        #登录web页面
        #
        driver = Login_web()
        driver.implicitly_wait(10)

        #
        #配置PPPoE上网
        #
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
        driver.find_element_by_link_text(u"外网配置").click()
        driver.find_element_by_css_selector("span.glyphicon.glyphicon-edit").click()
        Select(driver.find_element_by_name("connectionType")).select_by_visible_text(u"PPPoE接入")
        driver.find_element_by_name("pppoeUser").clear()
        driver.find_element_by_name("pppoeUser").send_keys(self.PPPoE_username)
        driver.find_element_by_name("pppoePass").clear()
        driver.find_element_by_name("pppoePass").send_keys(self.PPPoE_passwd)
        driver.find_element_by_id("save").click()
        #
        #等待配置返回页面
        #
        for i in range(1,10):
            flag = True
            try:
                driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[2]")
            except:
                flag=False
            time.sleep (1)
            if i==9:
                self.fail()
                driver.quit()
                return
            #
            #判断WAN口连接状态与WAN口IP地址是否正确
            #                      
            if flag:
                driver.find_element_by_link_text(u"外网配置").click()
                Wan_stat = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[2]").text
                Wan_addr = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[3]").text
                Wan_type = driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[4]").text
                if Wan_stat == "已连接" and Wan_addr.index(self.Wan_ip[:(len(self.Wan_ip) -3)]) == 0:
                    print("WAN口接入方式：" + Wan_type)
                    print("WAN口状态：" + Wan_stat)
                    print("WAN口IP地址：" + Wan_addr)
                    driver.quit()
                    return

    def test_Cli验证(self):
        #
        #NAT规则检查
        #
        NAT_flag = telnet('iptables -t nat -S wan1_default_nat |grep SNAT','-j SNAT --to-source '+ self.Wan_ip[:(len(self.Wan_ip) -3)])
        if NAT_flag is None:
            self.fail()
        else:
            print("NAT规则检查 pass！")


    def test_上网测试(self):
        #
        #测试ping外网
        #
        icmp_result=os.system('ping www.qq.com.cn -n 3 -w 1')
        if icmp_result:
            print ('ping测试 fail！')
            self.fail()
        else:
            print ('ping测试 pass！')

        #
        #测试打开网页
        #
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 

        self.driver.get("http://www.baidu.com")  
        try:  
            assert '百度一下，你就知道' in self.driver.title
            print ('打开网页测试 pass！')  
        except Exception as e:  
            print ('打开网页测试 fail！')  
            self.fail()
        time.sleep(1)
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()

