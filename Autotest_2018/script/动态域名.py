# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 17:47
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : 动态域名.py
# @Software: PyCharm Community Edition
import time
import unittest

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Autotest_2018.public_script.function_public import *
class 动态_域名(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def DDNS_config(self):
        u"动态域名配置"
        #"进入 网络配置--动态域名页面"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置:", netconfig.text)
        # 动态域名 定位
        ddns = self.driver.find_element_by_link_text("动态域名")
        ddns.click()
        print("当前位置：", ddns.text)
        time.sleep(2)
        # 新增 定位
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(3)
        provider = self.driver.find_element_by_xpath(".//select[@name='DDNSProvider']")
        uttcare = Select(provider).select_by_value("uttcare.com")
        time.sleep(1)
        # 主机名 地址获取
        hostname = self.driver.find_element_by_xpath(".//input[@name='DDNSUtt']").get_attribute("value")
        print("主机名 url为：", hostname)
        # 接口  这里选择wan1 口
        interface = self.driver.find_element_by_xpath(".//select[@name='Profile']")
        Select(interface).select_by_value("WAN1")
        # 保存 点击
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(3)
        # 刷新 点击
        refresh = self.driver.find_element_by_id("fresh")
        refresh.click()



    def test_动态域名配置(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        #配置动态域名
        self.DDNS_config()

        time.sleep(2)
        self.driver.quit()
if __name__ == '__main__':
    unittest.main()