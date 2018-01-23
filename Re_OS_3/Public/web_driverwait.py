# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 19:12
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : web_driverwait.py
# @Software: PyCharm Community Edition
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
driver = webdriver.Chrome()
def find_element(location,timeout = 10):
    element =WebDriverWait(driver=driver).until()