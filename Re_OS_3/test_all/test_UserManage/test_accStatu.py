# -*- coding: utf-8 -*-
# @Time    : 2018/2/4 15:44
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_accStatu.py
# @Software: PyCharm
from datetime import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time,random
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_sameConfig import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping

class AccStatu(unittest.TestCase):
    u'''**用户状态**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_14_001_accStatu(self):
        u'''用户状态显示与操作'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        #用户状态 定位
        accStatus = self.driver.find_element_by_link_text("用户状态")
        accStatus.click()
        Output_info(self.driver).output_content()



        pass





if __name__ == '__main__':
    unittest.main()