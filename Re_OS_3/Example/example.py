# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
# from nose.tools import assert_equal
# coding:utf-8

inport = ["80"]
outport = ["8081"]
a = "80~80:8081~8081"
b = inport+outport
c = "80~80:8081~8081"
# if a in c:
#     print("T")
# else:
#     print("Error")
for i in c:
    print(i)