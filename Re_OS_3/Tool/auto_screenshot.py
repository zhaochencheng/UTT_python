# -*- coding: utf-8 -*-
# @Time    : 2018/1/21 16:18
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : auto_screenshot.py
# @Software: PyCharm Community Edition
from selenium import webdriver

class Screen(object):
    u'''这个应该截图功能的装饰器'''
    def __init__(self, driver):
        self.driver = driver

    def __call__(self, f):
        def inner(*args):
            try:
                return f(*args)
            except:
                import time
                nowTime = time.strftime("%Y_%m_%d_%H_%M_%S")
                self.driver.get_screenshot_as_file('%s.jpg' % nowTime)
                raise
        return inner


# 以下是装饰器与unittest结合的案例
import unittest
class Test(unittest.TestCase):

    driver = webdriver.Chrome()  # 全局参数driver

    def setUp(self):
        self.driver.get("https://www.baidu.com")

    @Screen(driver)
    def test01(self):
        u'''这个是失败的案例'''
        self.driver.find_element_by_id("11kw").send_keys("python")
        self.driver.find_element_by_id("su").click()

    @Screen(driver)
    def test_02(self):
        u'''这个是通过的案例'''
        self.driver.find_element_by_id("kw").send_keys("yoyo")
        self.driver.find_element_by_id("su").click()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()