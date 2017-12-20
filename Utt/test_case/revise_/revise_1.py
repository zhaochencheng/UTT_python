# -*- coding: utf-8 -*-
# @Time    : 2017/12/12 19:36
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : revise_1.py
# @Software: PyCharm Community Edition
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re


class Test(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://192.168.2.1/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_(self):
        driver = self.driver
        driver.get(self.base_url + "/noAuth/login.html")
        driver.find_element_by_name("username").clear()
        driver.find_element_by_name("username").send_keys("admin")
        driver.find_element_by_name("pwd").clear()
        driver.find_element_by_name("pwd").send_keys("admin")
        driver.find_element_by_id("login_btn").click()
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
        driver.find_element_by_link_text(u"外网配置").click()
        driver.find_element_by_css_selector("span.glyphicon.glyphicon-edit").click()
        driver.find_element_by_id("save").click()
        driver.find_element_by_xpath("//ul[@id='otherBtns']/button").click()
        driver.find_element_by_id("sizzle-1513078668309").click()
        driver.find_element_by_link_text(u"已连接").click()

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
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


if __name__ == "__main__":
    unittest.main()
