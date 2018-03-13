# -*- coding: utf-8 -*-
# @Time    : 2018/3/13 17:15
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_BlackList.py
# @Software: PyCharm Community Edition
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time,random
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class Black_List(unittest.TestCase):
    u'''**黑名单**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def enter_BlackList(self):
        u"进入用户管理---黑名单页面"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        print("当前位置：", usermanage.text)
        #黑名单 定位
        blackList = self.driver.find_element_by_link_text("黑名单")
        blackList.click()
        print("当前位置：",blackList.text)

    def BlackList_config(self):
        u'''黑名单配置'''
        #新增定位
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(3)
        #用户名
        username = self.driver.find_element_by_xpath(".//input[@name = 'username']")
        username.clear()
        username.send_keys(blacklist_name[0])
        #mac 地址
        filterMac = self.driver.find_element_by_xpath(".//input[@name = 'filterMac']")
        filterMac.clear()
        filterMac.send_keys(blacklist_mac[0])
        #保存
        save = self.driver.find_element_by_id("save")
        save.click()

    def test_16_001_blacklist_config(self):
        u'''黑名单配置'''
        #进入用户管理---黑名单页面
        self.enter_BlackList()
        '''黑名单配置'''
        self.BlackList_config()
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("blacklist_config")
        '''判断黑名单在页面是否生效'''

    def test_16_002_blacklist_show(self):
        u'''黑名单页面信息显示'''
        # 进入用户管理---黑名单页面
        self.enter_BlackList()
        #输出页面信息
        Output_info(self.driver).output_content(blacklist_name)
        '''#输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("blacklist_show")
    def test_16_003_blacklist_validate(self):
        u'''黑名单功能验证'''
        '''验证思路：拉黑用户为下层路由器--通过telnet进路由器后台，ping外网；看是否拉黑成功'''
        pass

    def test_16_004_blacklist_delete(self):
        u'''黑名单配置删除'''
        # 进入用户管理---黑名单页面
        self.enter_BlackList()
        '''黑名单配置删除'''
        Delect_config(self.driver).delect_sameconfig(blacklist_name)
        '''#删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("blacklist_delete")

if __name__ == '__main__':
    unittest.main()
