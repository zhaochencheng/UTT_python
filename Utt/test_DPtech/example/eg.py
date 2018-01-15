# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 17:21
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : eg.py
# @Software: PyCharm Community Edition
import os

print(os.getcwd())
os.chdir(r"F:\untitled\Utt\test_DPtech\file_text")
print(os.getcwd())
f = open("1.txt","w")
f.write("1")
f.write("2")
f.close()