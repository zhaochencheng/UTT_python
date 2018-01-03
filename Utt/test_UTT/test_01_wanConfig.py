# -*- coding: utf-8 -*-
# @Time    : 2017/12/21 19:00
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_01_wanConfig.py
# @Software: PyCharm Community Edition
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from msg.http200 import *
from urllib.request import urlopen
import random


class MSG(unittest.TestCase):
    '''--MSG-WR265-P6v3.0.0-171203--软件升级测试'''
    def setUp(self):
        print("start!----开始升级")

    def test_m_s_g(self):
        '''--页面升级300次'''
        file = open('count2.txt', 'w')
        # i = 1
        # for i in range(3500,3800):
        try:
            # self.driver = webdriver.PhantomJS()
            self.driver = webdriver.Chrome()
            self.base_url = "http://192.168.2.5/"
            # file = open('count.txt', 'w')
            self.driver.implicitly_wait(20)
            # print('第%s次升级' % i)
            # file.write("第%s次升级\n" % i)
            file.write("当前时间： " + time.ctime() + '\n')
            print("当前时间： " + time.ctime() + '\n')
            self.driver.get(self.base_url + "/noAuth/login.html")
            # self.driver.maximize_window()
            self.driver.find_element_by_name("username").clear()
            self.driver.find_element_by_name("username").send_keys("admin")
            self.driver.find_element_by_name("pwd").clear()
            self.driver.find_element_by_name("pwd").send_keys("cc329b")
            time.sleep(2)
            self.driver.find_element_by_id("login_btn").click()
            time.sleep(1)

            #当前时间
            str1 = time.strftime('%Y-%m-%d_', time.localtime(time.time()))
            hour = time.strftime('%H', time.localtime(time.time()))
            minute = time.strftime('%M', time.localtime(time.time()))
            second = time.strftime('%S', time.localtime(time.time()))
            nowdate = str1 + hour + 'h' + minute + 'min' + second + 's'
            self.driver.get_screenshot_as_file(r"C:\Users\utt\Desktop\update2\%s" % nowdate+'_%s'%i +'.png')
            # print("升级截图编号："+"%s"%nowdate+"_%s"%i+".png")
            # time.sleep(50)
        except Exception as E:
            print(E)
        # self.driver.quit()
        time.sleep(1)
        file.close()


    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.driver.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally:
            self.accept_next_alert = True

    def tearDown(self):
        print("end!----升级完成")
    #     # self.driver.quit()
    #     # self.assertEqual([], self.verificationErrors)
    #

if __name__ == "__main__":
    unittest.main()