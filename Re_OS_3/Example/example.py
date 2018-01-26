# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
# from nose.tools import assert_equal
# coding:utf-8
#

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Config_data.config import *

driver = webdriver.Chrome()
Login(driver).login_router(url,username,pwd)
webwait = WebDriverWait(driver, 10, 1)
# 网络配置  定位
netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
netconfig.click()
print("当前位置：", netconfig.text)
# 端口映射 定位
port_map = driver.find_element_by_link_text("端口映射")
port_map.click()
print("当前位置:", port_map.text)
# nat规则
nat_rule = driver.find_element_by_link_text("NAT规则")
nat_rule.click()
time.sleep(3)
# 新增 按钮 定位
print("add qian ")
# add = driver.find_element_by_id("add")
adds = driver.find_elements_by_xpath("//*[@id='add']")

print(len(adds))

add = adds[1]
print(add.get_attribute("data-local"))
print(add)
print("add.text:",add.text)
print("add.is_enabled():",add.is_enabled())
print("add.is_displayed():",add.is_displayed())
# js = 'document.'
# add.click()
# add = webwait.until(lambda x: x.find_element_by_id("add"))
add.click()
time.sleep(3)

driver.quit()