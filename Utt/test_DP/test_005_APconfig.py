# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 21:00
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_005_APconfig.py
# @Software: PyCharm Community Edition
import unittest
from selenium import webdriver
import  time
import random

class APconfig(unittest.TestCase):
    '''从ac下发配置'''
    @classmethod
    def setUpClass(cls):
        print("只打开一次浏览器")
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://192.168.2.252")
        cls.driver.maximize_window()
        cls.driver.find_element_by_css_selector("#username").clear()
        cls.driver.find_element_by_css_selector("#username").send_keys('admin')
        cls.driver.find_element_by_css_selector("#login_password").clear()
        cls.driver.find_element_by_css_selector("#login_password").send_keys("admin_default")
        code = input("enter code:")  # 验证码
        cls.driver.find_element_by_css_selector("#code").send_keys(code)
        cls.driver.find_element_by_css_selector("#loginIn").click()
        time.sleep(3)
        print(cls.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("关闭浏览器")
    def setUp(self):
        print("\n再次打开浏览器")

    # def tearDown(self):
    #     '''退出web 管理员登陆'''
    #     #切换到默认frame
    #     self.driver.switch_to_default_content
    #     frame2 = self.driver.find_element_by_xpath("//*[@id='BODY']")
    #     #退出 按钮定位
    #     admin_exit = frame2.find_element_by_xpath(".//*[@id='test-top-right']/table/tbody/tr/td[6]/span/a/span")
    #     admin_exit.click()
    #     #接受弹窗
    #     a = self.driver.switch_to.alert
    #     print("退出管理员弹窗内容：", a.text)
    #     a.accept()
    #     time.sleep(2)
    def test_APconfig(self):
        f = open("ssid1.txt", "w+")
        # AP管理
        AP_mangle = self.driver.find_element_by_css_selector("#menu_T_Wireless_Management > a > span")
        print("---" + AP_mangle.text + "---")
        AP_mangle.click()
        time.sleep(3)
        # #在线AP
        # AP_online = driver.find_element_by_css_selector("#menu_S_INFORMATION_AP > a > span")
        # print("---"+AP_online.text+"---")
        # AP_online.click()
        # AP配置
        AP_set = self.driver.find_element_by_xpath(".//*[@id='menu_S_AC']/a/span")
        print("---" + AP_set.text + "---")
        AP_set.click()

        # 切换到AP信息管理 iframe 标签中
        iframe1 = self.driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/iframe[2]")
        self.driver.switch_to.frame(iframe1)
        for i in range(1, 300):
            # 进行ssid 名称配置
            try:
                ssid = self.driver.find_element_by_xpath(".//*[@id='template_cf_ssid']/tbody/tr[1]/td[3]")
                print("第%d次---" % i + "当前ssid为：", ssid.text)
                f.write("第%d次--" % i)
                f.write("当前ssid为：%s\n" % (ssid.text))
                ssid.click()
                # 输入 ssid名称
                ssid_input = self.driver.find_element_by_xpath(".//*[@id='ssid_input']")
                a = random.randint(1, 50)
                ssid_input.send_keys(str(a))
                self.driver.find_element_by_xpath(
                    ".//*[@id='INNER']/div[12]/div/div[2]/div/table/thead/tr/th[3]/div").click()
                time.sleep(1)
                # 确定
                submit = self.driver.find_element_by_xpath(".//*[@id='SUBMIT_BTN']")
                submit.click()
                # time.sleep(3)
                print("当前时间：", time.ctime())
                time.sleep(90)
            except Exception as E:
                print(E)
        f.close()
        time.sleep(5)
if __name__ == '__main__':
    unittest.main()