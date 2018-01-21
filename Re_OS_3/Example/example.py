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
# print(os.getcwd())

# print(os.path.dirname(png))

# print(type(png))
# nowTime = time.strftime("%Y%m%d.%H.%M.%S")
# # nowdate = str1 + hour + 'h' + minute + 'min' + second + 's'
# png2= png+"%s" % nowTime +'.png'
# print(type(png2))
nowTime = time.strftime("%Y%m%d.%H.%M.%S")
str = "_234"
print("%s"%(nowTime+str))