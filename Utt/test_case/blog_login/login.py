# -*- coding: utf-8 -*-
# @Time    : 2017/12/1 16:18
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : login.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time
from Utt.Config.config import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


'''
路由器web管理页面
1·登陆
'''
class uttlogin():


    def login_web(self):
        '''
        路由器web管理页面
        1·登陆
        :return:
        '''
        self.driver = webdriver.Chrome()
        wait = WebDriverWait(self.driver, 10)
        self.driver.get(URL)
        print("web title:",self.driver.title)
        try:

            user = wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, '#wrap > form > div.row.first-line > input[type="text"]')))
            user.clear()
            user.send_keys(Username)
            time.sleep(1)
            self.driver.find_element_by_xpath('//*[@id="wrap"]/form/div[2]/input').clear()
            pwd = self.driver.find_element_by_xpath('//*[@id="wrap"]/form/div[2]/input').send_keys(Pwd)
            login = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#login_btn')))
            login.click()
            print("登陆web时间：", time.ctime())
            time.sleep(5)


        except TimeoutError as timeout:
            print(' setup is time out! %s ',timeout)
            return

if __name__ == '__main__':
     A = uttlogin()
     A.login_web()