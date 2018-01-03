# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 19:05
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Uttlogin.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time

# class uttlogin:
#     def webLogin(self):
#         driver = webdriver.Chrome()
#         base_url = "http://192.168.2.5"
#         driver.implicitly_wait(20)
#         print("当前时间： " + time.ctime() + '\n')
#         driver.get(base_url + "/noAuth/login.html")
#         # self.driver.maximize_window()  #最大化窗口
#         driver.find_element_by_name("username").clear()
#         driver.find_element_by_name("username").send_keys("admin")
#         driver.find_element_by_name("pwd").clear()
#         driver.find_element_by_name("pwd").send_keys("cc329b")
#         time.sleep(2)
#         driver.find_element_by_id("login_btn").click()
#         time.sleep(1)
#
# # if __name__ == '__main__':
# A =uttlogin
# A.webLogin()
# class Utt:
#     def __int__(self):
#         self.driver = webdriver.Chrome()
#     def webLogin(self):
#         self.base_url = "http://192.168.2.5"
#         self.driver.implicitly_wait(20)
#         print("当前时间： " + time.ctime() + '\n')
#         self.driver.get(self.base_url + "/noAuth/login.html")
#         # self.driver.maximize_window()  #最大化窗口
#         self.driver.find_element_by_name("username").clear()
#         self.driver.find_element_by_name("username").send_keys("admin")
#         self.driver.find_element_by_name("pwd").clear()
#         self.driver.find_element_by_name("pwd").send_keys("cc329b")
#         time.sleep(2)
#         self.driver.find_element_by_id("login_btn").click()
#         time.sleep(1)

# # if __name__ == '__main__':
# Utt.webLogin()
# class Test:
#     def ppr(self):
#         print(self)
#         print(self.__class__)
#
# t = Test()
# t.ppr()
#
# class MyClass:
#     """一个简单的类实例"""
#     i = 12345
#
#     def f(self):
#         return 'hello world'
#
#
# # 实例化类
# x = MyClass()
#
# # 访问类的属性和方法
# # print("MyClass 类的属性 i 为：", x.i)
# # print("MyClass 类的方法 f 输出为：", x.f())
# class Complex:
#     def __init__(self, realpart, imagpart):
#         self.r = realpart
#         self.i = imagpart
# x = Complex(3.0, -4.5)
# print(x.r, x.i)   # 输出结果：3.0 -4.5
# 类定义
class people:
    # 定义基本属性
    name = ''
    age = 0
    # 定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0

    # 定义构造方法
    def __init__(self, n, a, w):
        self.name = n
        self.age = a
        self.__weight = w

    def speak(self):
        print("%s 说: 我 %d 岁。" % (self.name, self.age))


# 实例化类
p = people('runoob', 10, 30)
p.speak()