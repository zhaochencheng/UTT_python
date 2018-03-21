# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 14:47
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : 用户状态.py
# @Software: PyCharm Community Edition
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from Autotest_2018.public_script.Get_screenshot import Get_Screenshot
from Autotest_2018.public_script.function_public import *
from Autotest_2018.public_script.Output_web_info import Output_info
class 用户_状态(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def enter_accStatu(self):
        # 进入用户管理---用户状态页面
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        # 用户状态 定位
        accStatus = self.driver.find_element_by_link_text("用户状态")
        accStatus.click()
        time.sleep(2)
    def Users_joingroups(self):
        u'''将临时用户全部加入分组'''
        # 进入用户管理---用户状态页面
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        # 用户状态 定位
        accStatus = self.driver.find_element_by_link_text("用户状态")
        accStatus.click()
        time.sleep(2)
        #表头
        all = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th[1]/input")
        all.click()
        # 移动到 定位
        move = self.driver.find_element_by_id("move")
        move.click()
        #分组 定位
        groupArr = self.driver.find_element_by_xpath(".//select[@name='groupArr']")
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
            print("将临时用户加入分组")

        # except BaseException as  E:
        #     print("当前无分组!")



    def test_01_用户状态查看(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        self.enter_accStatu()
        #输出页面信息
        Output_info(self.driver).output_all()

        time.sleep(2)
        self.driver.quit()

    def test_02_临时用户加入分组(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        self.Users_joingroups()

        time.sleep(2)
        self.driver.quit()

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(用户_状态("test_01_用户状态查看"))
    suit.addTest(用户_状态("test_02_临时用户加入分组"))
    runner = unittest.TextTestRunner()
    runner.run(suit)

