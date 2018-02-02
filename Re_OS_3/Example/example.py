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
import random

# a = ["uttcare.com",'www.163.com','werew','erw']
# i = random.randint(1,len(a))
# print(i)
# for i in range(len(a)):
#     print("http://"+a[i])
# print(len(a))
# print(a[1])
delect_anyone = random.randint(0,len(DNS_filter_hostname))
print(delect_anyone)
print(DNS_filter_hostname[delect_anyone])