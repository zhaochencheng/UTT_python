# -*- coding: utf-8 -*-
# @Time    : 2018/1/3 10:07
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_001_AP_offline.py
# @Software: PyCharm Community Edition
import unittest
from selenium import webdriver
import  time
from Utt.test_DPtech.Login_AC.login_ac import *

class AP_offline(unittest.TestCase):
    '''将在线ap踢下线'''
    @classmethod
    def setUpClass(cls):
        print("只打开一次浏览器")
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://192.168.2.252")
        #引入 公共类
        Login_DP_ac(cls.driver).login("admin","admin_default")

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("关闭浏览器")
    def setUp(self):

        print("\n再次打开浏览器")

    def tearDown(self):
        '''退出web 管理员登陆'''
        #切换到默认frame
        self.driver.switch_to.default_content()
        frame2 = self.driver.find_element_by_xpath("//*[@id='BODY']")
        #退出 按钮定位
        admin_exit = frame2.find_element_by_xpath(".//*[@id='test-top-right']/table/tbody/tr/td[6]/span/a/span")
        admin_exit.click()
        #接受弹窗
        a = self.driver.switch_to.alert
        print("弹窗内容：", a.text)
        a.accept()
        time.sleep(2)


    def test_ap_offline(self):
        '''将在线ap踢下线'''
        # AP管理
        AP_mangle = self.driver.find_element_by_css_selector("#menu_T_Wireless_Management > a > span")
        print("---" + AP_mangle.text + "---")
        AP_mangle.click()
        time.sleep(3)
        # 在线AP
        AP_online =self.driver.find_element_by_css_selector("#menu_S_INFORMATION_AP > a > span")
        print("---" + AP_online.text + "---")
        AP_online.click()
        # 切换到AP信息管理 iframe 标签中
        # self.driver.switch_to_default_content()
        iframe1 = self.driver.find_element_by_xpath(".//*[@id='mainframe_td']/div/div[2]/iframe[2]")
        self.driver.switch_to.frame(iframe1)
        while 1:
            # 当前在线ap个数
            ap_count = self.driver.find_elements_by_xpath("//*[@id='ap_info_manage']/tbody/tr")
            len_ap_count = len(ap_count)
            print("当前在线ap个数:", len_ap_count)
            for i in range(0, len_ap_count):
                i = 1
                # AP 型号
                model = self.driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[2]" % i)
                print("AP 型号", model.text)
                # 软件版本
                version = self.driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[6]" % i)
                print("软件版本:", version.text)
                # 状态信息
                status_messages = self.driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[7]" % i)
                print("状态信息:", status_messages.text)
                # #点击将ap踢下线
                ap_offline =self.driver.find_element_by_xpath(".//*[@id='ap_info_manage']/tbody/tr[%d]/td[10]/span[1]" % i)
                ap_offline.click()
                time.sleep(2)
                # 接收alert 弹窗； 确定将ap下线；
                a = self.driver.switch_to.alert
                print("弹窗内容：", a.text)
                a.accept()
                time.sleep(4)
            break

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(AP_offline("test_ap_offline"))
    runner = unittest.TextTestRunner()
    runner.run(suit)
#     # unittest.main()