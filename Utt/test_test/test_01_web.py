# -*- coding: utf-8 -*-
# @Time    : 2017/12/5 19:04
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : __init__.py.py
# @Software: PyCharm Community Edition
from Utt.Config.config import *
from Utt.tool.http200 import *
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
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
    #@unittest.skip(u'')
    def test_01_login(self):
        u'''web登陆'''

        try:
            # self.driver = webdriver.Chrome()
            # utt = self.driver
            # print(i)
            # self.driver.get(URL)
            f = open('test.txt', 'w')
            for i in range(1, 3):
                print('第%s次升级' % i)
                f.write("第%s次升级\n" % i)
                self.driver = webdriver.PhantomJS()
                self.driver.get(URL)
                # utt = webdriver.PhantomJS()
                # utt.get("http://192.168.2.1")
                self.driver.implicitly_wait(20)
                self.driver.maximize_window()
                time.sleep(1)
                self.driver.find_element_by_name('username').send_keys("admin")
                time.sleep(1)
                self.driver.find_element_by_name('pwd').send_keys("admin")
                time.sleep(3)
                self.driver.find_element_by_name("pwd").send_keys(Keys.ENTER)
                # i1 = random.randint(10, 20)
                time.sleep(3)
                str1 = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime(time.time()))
                self.driver.get_screenshot_as_file(r"C:\Users\utt\Desktop\update\%s" % i+'%s'%str1+".png")
                time.sleep(3)
                self.driver.quit()
                # utt.quit()
                try:
                    resp = urlopen(URL)
                    code = resp.getcode()
                    # file.write("请求http（lan口）时间： " + time.ctime() + '\n')
                    # file.write("http 状态码：%s" % code + ';可以访问web页面\n')
                    print('the result is :', code)
                    print("%s" % URL + "可以访问！")
                    print("当前时间： " + time.ctime() + '\n')
                except Exception as  e:
                    print(e)
        except TimeoutError as timeout:
            print(' setup is time out! %s ', timeout)
            return
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




if __name__ == '__main__':
    unittest.main()
# for i in range(2):
#     testunit = unittest.TestSuite()
#     testunit.addTests(Test_login('test_01_login'))
#     unittest.TextTestRunner(verbosity=2).run(testunit)

