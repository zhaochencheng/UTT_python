# -*- coding: utf-8 -*-
# @Time    : 2018/3/1 17:21
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test12312.py
# @Software: PyCharm Community Edition
import os
print(__file__)
#获取当前脚本的真实路径
cur_path = os.path.realpath(__file__)
print("获取当前脚本的真实路径",cur_path)
#获取脚本的名称
name = os.path.basename(cur_path)
print("获取脚本的名称",name)
