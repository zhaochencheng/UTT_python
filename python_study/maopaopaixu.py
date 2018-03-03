# -*- coding: utf-8 -*-
# @Time    : 2018/3/2 10:03
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : maopaopaixu.py
# @Software: PyCharm Community Edition

L = [1,23,12,4,3,66,32,5]
# print(L)
for i in range(len(L)):
    for j in range(i,len(L)):
        if L[i] > L[j]:
            a = L[i]
            L[i] = L[j]
            L[j] = a
            # print(L)
        else:
            pass
print(L)
