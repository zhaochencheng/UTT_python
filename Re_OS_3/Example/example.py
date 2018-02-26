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
path = r"G:\github\UTT_python\Re_OS_3\Screenshot"
def del_file(path):
    ls = os.listdir(path)
    for i in ls:
        c_path = os.path.join(path, i)
        if os.path.isdir(c_path):
            del_file(c_path)
        else:
            os.remove(c_path)

del_file(path)