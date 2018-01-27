# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 17:44
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_router_config.py
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

class Router_config(unittest.TestCase):
    u'''**路由配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_05_staticRouter(self):
        u'''静态路由配置与删除'''

        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：",netconfig.text)
        #路由配置 定位
        router_config = self.driver.find_element_by_link_text("路由配置")
        router_config.click()
        time.sleep(2)

        #静态路由配置
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()

        # 判断页面是否存在与配置 相同的配置
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for j in range(len(router_static_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == new_rulename[j]:
                        # 删除按钮 定位
                        delete = self.driver.find_element_by_xpath(
                            ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]" % i)
                        delete.click()
                        # 确认删除 定位
                        ok = self.driver.find_element_by_id("u-cfm-ok")
                        ok.click()
                        time.sleep(4)
                        print("已有%s 规则，先将其删除" % name_rule, "*" * 30, '\n')
                    else:
                        pass
                else:
                    break





