# -*- coding: utf-8 -*-
# @Time    : 2018/1/15 17:21
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : eg.py
# @Software: PyCharm Community Edition
import os
import unittest
class A(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_1(self):
        a= 1
        b= 2
        if a == b :
            print("equal")
        else:
            print("222")
            raise Exception("not equal")

if __name__ == '__main__':
    unittest.main()

