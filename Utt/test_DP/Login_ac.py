# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 16:07
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Login_ac.py
# @Software: PyCharm Community Edition

from selenium import webdriver
import time
def login_ac():
    driver = webdriver.Chrome()
    driver.get("http://192.168.2.252")
    #cookies 输出
    # cookies_before = driver.get_cookies()
    # print(cookies_before)
    driver.find_element_by_css_selector("#username").clear()
    driver.find_element_by_css_selector("#username").send_keys('admin')
    driver.find_element_by_css_selector("#login_password").clear()
    driver.find_element_by_css_selector("#login_password").send_keys("admin_default")
    code = input("enter code:")#验证码
    driver.find_element_by_css_selector("#code").send_keys(code)
    driver.find_element_by_css_selector("#loginIn").click()
    time.sleep(3)
    # cookies 输出
    # cookies_after = driver.get_cookies()
    # print(cookies_after)
    print(driver.title)