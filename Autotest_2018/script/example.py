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
cf = configparser.ConfigParser()
config_file="/Config/config.ini"
file_path = os.path.abspath(os.path.join(os.path.realpath(__file__), "../.."))   + config_file
cf.read(file_path)
print(file_path)
# s = cf.sections()
# print(s)
# o = cf.options("lan_config")
# print(o)
# v = cf.items("DDNS_config")
# print(v)
cf.set("DDNS_config","DDNS_address","11222225.uttcare.com")

v1 = cf.items("DDNS_config")
print(v1)
# cf.write(open(file_path,"w+"))
with open(file_path,'w+') as f:
    cf.write(f)