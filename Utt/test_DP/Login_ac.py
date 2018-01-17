# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 16:07
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Login_ac.py
# @Software: PyCharm Community Edition

from selenium import webdriver
import time
def login_ac():
    url = "http://192.168.2.252"
    driver = webdriver.Chrome()
    driver.get(url)
    #cookies 输出
    # #[{'httpOnly': True, 'domain': '192.168.2.252', 'value': 'IOzjF3j2TBsA06z6nfvAPhokiUrKJ4IA',
    # 'path': '/', 'name': 'SID', 'secure': False}]
    cookies_before = driver.get_cookies()
    print(cookies_before)
    driver.delete_all_cookies()
    driver.add_cookie({'httpOnly': True, 'domain': '192.168.2.252', 'value': 'IOzjF3j2TBsA06z6nfvAPhokiUrKJ4IA',
    'path': '/', 'name': 'SID', 'secure': False})
    #[{'name': 'SID', 'httpOnly': True, 'secure': False, 'domain': '192.168.2.252', 'value': '3M5XGnd4FBNZC0k1e3LC8zqTa43MxQWZ', 'path': '/'}]
    driver.find_element_by_css_selector("#username").clear()
    driver.find_element_by_css_selector("#username").send_keys('admin')
    driver.find_element_by_css_selector("#login_password").clear()
    driver.find_element_by_css_selector("#login_password").send_keys("admin_default")
    # code = input("enter code:")#验证码
    # driver.find_element_by_css_selector("#code").send_keys(code)
    driver.find_element_by_css_selector("#loginIn").click()
    time.sleep(3)
    driver.get(url)
    # cookies 输出
    cookies_after = driver.get_cookies()
    print(cookies_after)
    print(driver.title)
    time.sleep(3)
    driver.quit()



if __name__ == '__main__':
    login_ac()