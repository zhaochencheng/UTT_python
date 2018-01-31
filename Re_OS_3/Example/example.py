# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
# from nose.tools import assert_equal
# coding:utf-8
import unittest
import time
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Config_data.config import *

class BehaviorManage(unittest.TestCase):
    u'''**行为管理配置**'''
    def setUp(self):
        print("start!")
        # self.driver = webdriver.Chrome()
        # Login(self.driver).login_router(url,username,pwd)
    def tearDown(self):
        print("end!")
        # time.sleep(5)
        # self.driver.quit()
    def test_17_001_behaviorMange(self):
        print("17")
    def test_01_001_behaviorMange(self):
        print("01")
    def test_01_002_behaviorMange(self):
        print("01_002")
    def test_02_002_behaviorMange(self):
        print("02_002")

if __name__ == '__main__':
    unittest.main()