# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
# from nose.tools import assert_equal
# coding:utf-8
import os
from selenium import webdriver
import time
driver = webdriver.Chrome()
driver.get("http://192.168.2.1")
driver.implicitly_wait(10)
#用户名输入
driver.find_element_by_name("username").clear()
driver.find_element_by_name("username").send_keys("admin")
#密码输入
driver.find_element_by_name("pwd").clear()
driver.find_element_by_name("pwd").send_keys("admin")
#点击登陆按钮
driver.find_element_by_id("login_btn").click()
# 网络配置  定位
netconfig = driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span")
netconfig.click()
print("当前位置：", netconfig.text)
# 外网配置 定位
wan_config = driver.find_element_by_link_text("外网配置")
wan_config.click()
print("当前位置：", wan_config.text)
time.sleep(3)
driver.refresh()