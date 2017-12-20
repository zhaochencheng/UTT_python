# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 16:21
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_01_login.py
# @Software: PyCharm Community Edition
from Utt.Config.config import *
from Utt.test_case.blog_login.login import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class Test_login(unittest.TestCase):
    u'''web登陆'''
    def setUp(self):
        print('start!')
        # self.driver = webdriver.Chrome()
        # self.driver.get(URL)
        # print("web title:", self.driver.title)
        # self.driver.implicitly_wait(10)

    def tearDown(self):
        print("end!")

    def test_01_login(self):
        u'''web登陆'''

        try:
            self.driver = webdriver.Chrome()
            # print(i)
            self.driver.get(URL)
            print("web title:", self.driver.title)
            self.driver.implicitly_wait(10)
            #用户名
            wait = WebDriverWait(self.driver, 10)
            user = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#wrap > form > div.row.first-line > input[type="text"]')))
            user.clear()
            user.send_keys(Username)
            time.sleep(1)
            #密码
            self.driver.find_element_by_xpath('//*[@id="wrap"]/form/div[2]/input').clear()
            #
            pwd = self.driver.find_element_by_xpath('//*[@id="wrap"]/form/div[2]/input').send_keys(Pwd)
            #登陆按钮
            login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#login_btn')))
            login.click()
            print("登陆web时间：", time.ctime())
            time.sleep(5)
        except TimeoutError as timeout:
            print(' setup is time out! %s ', timeout)
            return

    def test_02_login(self):
        try:
            # self.driver = uttlogin.
            # self.driver = webdriver.Chrome()
            uttlogin.login_web(self)
            driver = self.driver
            time.sleep(2)
            driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
            time.sleep(1)
            wan=driver.find_element_by_link_text(u"外网配置")
            print(wan.get_attribute('data-local'))
            # driver.find_element_by_css_selector("span.glyphicon.glyphicon-edit").click()
            # driver.find_element_by_id("save").click()
            # driver.find_element_by_xpath("//ul[@id='otherBtns']/button").click()
            # driver.find_element_by_id("sizzle-1513078668309").click()
            # driver.find_element_by_link_text(u"已连接").click()

        except Exception as E:
            print(E)


    # def test_02_http200(self):
    #     '''访问 URL ；输出http 状态码；'''
    #     '''
    #         访问 URL ；输出http 状态码；
    #         查看访问状态
    #     :return:
    #     '''
    #     http200(URL)
    #
    #     pass
    # def test_02_logout(self):
    #     try:
    #         self.driver.quit()
    #     except Exception as  e:
    #         print(e)
    #
    #


if __name__ == '__main__':
    # for i in range(2):
    #     testunit = unittest.TestSuite()
    #     testunit.addTests(Test_login('test_01_login'))
    #     unittest.TextTestRunner(verbosity=2).run(testunit)
    unittest.main()