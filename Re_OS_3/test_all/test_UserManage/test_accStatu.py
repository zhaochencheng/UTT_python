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
    def Users_joingroups(self):
        u'''将临时用户全部加入分组'''
        #表头
        all = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th[1]/input")
        all.click()
        # 移动到 定位
        move = self.driver.find_element_by_id("move")
        move.click()
        #分组 定位
        groupArr = self.driver.find_element_by_xpath(".//select[@name='groupArr']")
        l = []
        l= Select(groupArr).options
        print("当前分组个数为：",len(l))
        if len(l)==0:
            print("当前无分组!无法移动到分组中！")
            #关闭 定位
            close = self.driver.find_element_by_id("modal-hide")
            close.click()
            raise BaseException("当前无分组!无法移动到分组中！")
        else:
            Select(groupArr).select_by_index(0)
            time.sleep(2)
            #保存 定位
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(2)

        # except BaseException as  E:
        #     print("当前无分组!")





    def test_14_001_accStatu(self):
        u'''用户状态显示与操作'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        #用户状态 定位
        accStatus = self.driver.find_element_by_link_text("用户状态")
        accStatus.click()
        #将页面 用户状态列表 信息输出
        Output_info(self.driver).output_all()

        #将临时用户加入分组中
        self.Users_joingroups()

        #将页面 用户状态列表 信息输出
        time.sleep(5)
        self.driver.refresh()
        time.sleep(3)
        Output_info(self.driver).output_all()

        '''黑名单生效'''






if __name__ == '__main__':
    unittest.main()