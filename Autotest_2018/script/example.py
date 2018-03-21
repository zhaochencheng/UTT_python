# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 9:30
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : example.py
# @Software: PyCharm Community Edition
import time
import unittest
import configparser

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Autotest_2018.public_script.function_public import *

# DDNS_Server = get_data("DDNS_config", "DDNS_server")
# DDNS_addr = get_data("DDNS_config", "DDNS_address")
# print("1",DDNS_addr)
# DDNS_addr = '1160504195.uttcare.com'
# print(DDNS_addr)
# cf = configparser.ConfigParser()
# config_file="/Config/config.ini"
# file_path = os.path.abspath(os.path.join(os.path.realpath(__file__), "../.."))   + config_file
# cf.read(file_path)
# print(file_path)
# # s = cf.sections()
# # print(s)
# # o = cf.options("lan_config")
# # print(o)
# # v = cf.items("DDNS_config")
# # print(v)
# cf.set("DDNS_config","DDNS_address","11222225.uttcare.com")
#
# v1 = cf.items("DDNS_config")
# print(v1)
# # cf.write(open(file_path,"w+"))
# with open(file_path,'w+') as f:
#     cf.write(f)
class 我(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_81(self):
        print("a01")
    def test_82(self):
        print("a02")
    def test_91(self):
        print("a31")
    def test_93(self):
        print("a03")
    def test_91(self):
        print("a11")
    def test_61(self):
        print("a21")
class 阿(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_01(self):
        print("b01")
    def test_02(self):
        print("b02")
    def test_31(self):
        print("b31")
    def test_03(self):
        print("b03")
    def test_11(self):
        print("b11")
    def test_21(self):
        print("b21")
if __name__ == '__main__':
    suit1 = unittest.TestSuite()
    suit1.addTest(我("test_81"))
    suit1.addTest(我("test_82"))
    suit1.addTest(阿("test_01"))
    suit1.addTest(阿("test_11"))
    suit1.addTest(我("test_81"))
    suit1.addTest(我("test_82"))
    suit1.addTest(阿("test_01"))
    suit1.addTest(阿("test_11"))
    runner = unittest.TextTestRunner()
    runner.run(suit1)
    # unittest.main()