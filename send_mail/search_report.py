# -*- coding: utf-8 -*-
# @Time    : 2017/12/20 14:36
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : search_report.py
# @Software: PyCharm Community Edition
import os, datetime, time

# def Search_testReport():
result_dir = 'F:\\untitled\\send_mail'
lists = os.listdir(result_dir)
lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn) if not
os.path.isdir(result_dir + "\\" + fn) else 0)
print('最新的文件为： ' + lists[-1])
file = os.path.join(result_dir, lists[-1])
print(file)