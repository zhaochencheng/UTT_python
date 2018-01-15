# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 15:05
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : login_ac.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time
import unittest


class Login_DP_ac():
    '''登陆ac'''
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, pwd):
        u'''  登陆模块'''
        #用户名
        self.driver.find_element_by_css_selector("#username").clear()
        self.driver.find_element_by_css_selector("#username").send_keys(username)
        #密码
        self.driver.find_element_by_css_selector("#login_password").clear()
        self.driver.find_element_by_css_selector("#login_password").send_keys(pwd)
        code = input("enter code:")  # 验证码
        self.driver.find_element_by_css_selector("#code").send_keys(code)
        self.driver.find_element_by_css_selector("#loginIn").click()
        time.sleep(3)
        print(self.driver.title)

class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        url = "http://192.168.2.252"
        self.driver.get(url)
        self.driver.implicitly_wait(10)
    def tearDown(self):
        self.driver.quit()
    def test_login_AC(self):
        Login_DP_ac(self.driver).login("admin","admin_default")
if __name__ == '__main__':
    unittest.main()

# if __name__ == '__main__':
#     brower = webdriver.Chrome()
#     url = "http://192.168.2.252"
#     brower.get(url)
#     AC_login = Login_DP_ac(brower)
#     AC_login.login("admin","admin_default")
#     # print(type(AC_login))