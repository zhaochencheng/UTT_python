# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
# from nose.tools import assert_equal
# coding:utf-8
#
from selenium import webdriver
from time import sleep
import unittest,re
# import Readexcel
import os

#excel表格获取url、用户名、密码
# B=Readexcel.read_xls_file()
url1="192.168.2.1"
username="admin1"
pwd="admin"

def login_A():
	print(url1)
	driver.get("http://192.168.2.1")
	driver.implicitly_wait(8)
	driver.find_element_by_name("username").clear()
	driver.find_element_by_name("username").send_keys(username)
	driver.find_element_by_name("pwd").clear()
	driver.find_element_by_name("pwd").send_keys(pwd)
	driver.find_element_by_id("login_btn").click()
	sleep(1)

def check():
#检测是否登录成功
	for num in range(1,3):
		if "index.html" in driver.current_url:
			print('login successful')
			#break #跳出当前循环
			return #跳出检测函数
		else:
			error_mes=driver.find_element_by_xpath(".//*[@id='warning-msg']").text #获取错误信息
			print (error_mes)
			sleep(1)
			login_A()
#检测最后是否登录成功
	if "index.html" in driver.current_url:
		print('login successful')
	else:
		print("ERROR!")
        raise BaseException("无法登陆页面！")
if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    login_A()
    check()
    driver.quit()