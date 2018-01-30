# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
# from nose.tools import assert_equal
# coding:utf-8
from Re_OS_3.Public.Login_Router import Login
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

host = "http://192.168.32.115"
port = ":8081"
url = host+port
# print(host+port)
# driver = webdriver.Chrome()
# Login(driver).login_router(url,"admin","admin")
# print(driver.title)
# print(driver.current_url)
# driver.quit()
import time
try:
    driver = webdriver.Chrome()
    driver.get(url)
    driver.implicitly_wait(10)
    webwait = WebDriverWait(driver, 10, 1)
    # 用户名输入
    # user = webwait.until(lambda x: x.find_element_by_name("username"))
    # webwait.until(EC.visibility_of(By.NAME("username")))
    for i in range(10):
        if driver.find_element_by_name("username").is_displayed():
            driver.find_element_by_name("username").clear()
            driver.find_element_by_name("username").send_keys("admin")
            # 密码输入
            driver.find_element_by_name("pwd").clear()
            driver.find_element_by_name("pwd").send_keys("admin")
            # 点击登陆按钮
            driver.find_element_by_id("login_btn").click()
            break
        else:
            time.sleep(1)
            print(i)
        if i == 9:
            raise BaseException("not open url")
    # print("当前页面为：%s"%self.driver.title)
    # time.sleep(3)
except BaseException as  E:

    print(E)