# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 19:42
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Wan_config.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time
from Utt.Config.config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utt.test_case.blog_login.login import *
import Utt.test_case.blog_login.login
class Network_Wan_config(uttlogin):
    def Wan_config(self):
        try:
            # self.driver = uttlogin.
            # self.driver = webdriver.Chrome()
            uttlogin.login_web(self)
            driver = self.driver
            time.sleep(2)
            driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
            driver.find_element_by_link_text(u"外网配置").click()
            driver.find_element_by_css_selector("span.glyphicon.glyphicon-edit").click()
            driver.find_element_by_id("save").click()
            driver.find_element_by_xpath("//ul[@id='otherBtns']/button").click()
            driver.find_element_by_id("sizzle-1513078668309").click()
            driver.find_element_by_link_text(u"已连接").click()

        except Exception as E:
            print(E)

if __name__ == '__main__':
    A =Network_Wan_config
    A.Wan_config()