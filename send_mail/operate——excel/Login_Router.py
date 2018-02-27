# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 15:57
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Login_Router.py
# @Software: PyCharm Community Edition
'''
路由器web 登陆

'''
from selenium import webdriver
import time
import unittest

class Login():
    '''登陆'''
    #公共类须 初始化：
    def __init__(self,driver):
        self.driver = driver
    def login_router(self,url,username,pwd):
        # self.driver = webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        #用户名输入
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send_keys(username)
        #密码输入
        self.driver.find_element_by_name("pwd").clear()
        self.driver.find_element_by_name("pwd").send_keys(pwd)
        #点击登陆按钮
        self.driver.find_element_by_id("login_btn").click()
        # print("当前页面为：%s"%self.driver.title)
        time.sleep(3)


#下为： 类的实例化 调用

class T(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router("http://192.168.2.1","admin","admin")
    def tearDown(self):
        self.driver.quit()
    def test_001(self):
        print(self.driver.title)
if __name__ == '__main__':
    unittest.main()

