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
# *trailing,current = [12,23,43,54,13,4,12,"sd"]
# print(*trailing)
# print(current)
# print(type(current))
from collections import deque
q = deque()
q.append(1)
q.append(2)
q.append(3)
print(q)
q.append(4)
print(q)
q.appendleft(6)
print(q)
print(q.pop())
print(q)