# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 11:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
# from nose.tools import assert_equal
# coding:utf-8
import os
#
# cwd = os.getcwd()
# print(cwd)
# # print(os.listdir())
# parent_path = os.path.dirname(cwd)
# print("上级目录为：",parent_path)
# ScreenShot = parent_path + "\Screenshot"
# print(ScreenShot)
# print(os.listdir(ScreenShot))
# print(os.path.basename(cwd))
# print(os.path.splitext(os.path.basename(cwd)))
# path = r"G:\github\UTT_python\Re_OS_3\Screenshot"
# def del_file(path):
#     ls = os.listdir(path)
#     for i in ls:
#         c_path = os.path.join(path, i)
#         if os.path.isdir(c_path):
#             del_file(c_path)
#         else:
#             os.remove(c_path)
#
# # del_file(path)
# # 当前脚本所在文件真实路径
# # cur_path = os.path.dirname(os.path.realpath(__file__))
# cur_path = os.path.realpath(__file__)
# cur_path = r"G:\github\UTT_python\Re_OS_3\test_all\test_netConfig"
# print(cur_path)
# if os.path.isdir(cur_path):
#     list = os.listdir(cur_path)
#     print(list)
# elif os.path.isfile(cur_path):
#     print("file")

from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.Ping import Ping
# def ping12(ip):
#     a = os.system('ping -n 2 -w 2 %s' % ip)
#     # ping 通 a = 0  ;ping 不通a = 1
#     if a == True:
#         print('ping %s is fail' % ip)
#         # 如果ping 不通 会抛出异常
#         raise BaseException("ping 不通该%s 地址 " % ip)
#     else:
#         # print(a)
#         print('ping %s is ok' % ip)
#         return False
# ping12("192.168.34.1")
# l = []
# print(len(l))
# if l == None :
#     print("0")
#
# a = [1,2]
# b = ['a','b']
# c = []
# for i in range(len(a)):
#     add = str(a[i])+b[i]
#     c.append(add)
# print(c)
# for i in range(1,3):
#     print(i)
# a = [1,2,3,4]
# print("len（a）:",len(a))
# Ping().ping_IP(PPTP_remoteInIp[0])from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium import webdriver
from PIL import Image
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com/')
#
# driver.save_screenshot('button.png')
# element = driver.find_element_by_id("su")
# print(element.location)
# print(element.size)
# left = element.location['x']
# top = element.location['y']
# right = element.location['x'] + element.size['width']
# bottom = element.location['y'] + element.size['height']
# im = Image.open('button.png')
# im = im.crop((left,top,right,bottom))
# im.save('button.png')
# driver.quit()
import unittest
# a = ["fc:2f:ef:e9:0a:af"]
# L = [1,3,5,6,"fc:2f:ef:e9:0a:af"]
# print(a[0] in L)
# nowTime = time.strftime("%Y-%m-%d.%H_%M_%S")
# print(nowTime)
# class aa:
#     w =  10
#     def __init__(self):
#         self.x = 11
#         self.y = 12
#     def add(self):
#         return self.x+self.y
# a = aa()
# print(a.add())
# aa.w= 20
# a.w =13
# print(aa.w,a.w)
