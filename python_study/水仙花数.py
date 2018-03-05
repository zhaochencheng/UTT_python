# -*- coding: utf-8 -*-
# @Time    : 2018/3/3 15:38
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : 水仙花数.py
# @Software: PyCharm Community Edition
for i in range(100, 1000):
    sum = 0
    temp = i
    while temp:
        sum = sum + (temp%10) ** 3
        temp //= 10
    if sum == i:
        print(i)
