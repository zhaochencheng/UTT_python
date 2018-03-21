# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 13:38
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : DMZ主机.py
# @Software: PyCharm Community Edition
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from Autotest_2018.public_script.function_public import *

class DMZ_主机(unittest.TestCase):
    # class静态参数
    #
    # 配置参数获取
    #
    DMZ_globalHost = get_data("DMZ_config", "DMZ_globalHost")
    DMZ_wan1Host = get_data("DMZ_config", "DMZ_wan1Host")
    DMZ_wan2Host = get_data("DMZ_config", "DMZ_wan2Host")
    DMZ_wan3Host = get_data("DMZ_config", "DMZ_wan3Host")
    DMZ_wan4Host = get_data("DMZ_config", "DMZ_wan4Host")


    def setUp(self):
        pass
    def tearDown(self):
        pass

    def DMZ_config(self):
        u'''进行DMZ配置---全局配置'''

        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：", netconfig.text)
        # 端口映射 定位
        port_map = self.driver.find_element_by_link_text("端口映射")
        port_map.click()
        print("当前位置:", port_map.text)
        time.sleep(2)

        # DMZ主机 定位
        DMZ = self.driver.find_element_by_link_text("DMZ主机")
        print("当前定位：", DMZ.text)
        DMZ.click()
        time.sleep(2)
        # DMZ状态 定位
        open_DMZ = self.driver.find_element_by_xpath(".//input[@name = 'DMZEnable' and @value='on']")
        if open_DMZ.is_selected():
            print("已开启DMZ！")
        else:
            open_DMZ.click()
            print("现在开启DMZ！")
        time.sleep(3)
        # 全局DMZ主机 定位
        globalDMZ = self.driver.find_element_by_xpath(".//input[@name='GlobalDMZ']")
        globalDMZ.clear()
        globalDMZ.send_keys(self.DMZ_globalHost)
        # 保存 定位
        save = self.driver.find_element_by_id('save')
        save.click()
        time.sleep(2)
        # 判断全局DMZ主机 在页面 是否生效
        for i in range(1, 5):
            wan_DMZ = self.driver.find_element_by_xpath(".//input[@name='WAN%iDMZ']" % i)
            if wan_DMZ.is_displayed():
                print("wan%d口DMZ主机ip为：" % i, wan_DMZ.get_attribute("value"))
                self.assertEqual(wan_DMZ.get_attribute("value"), self.DMZ_globalHost, "全局DMZ主机ip和wan1口DMZ主机IP不一致")
        print("各wan口配置ip与全局DMZ主机ip相同")
    def test_01_DMZ主机配置(self):
        #  登陆web页面
        self.driver = Login_web()
        #
        self.DMZ_config()

    def test_02_DMZ主机验证(self):
        pass
if __name__ == '__main__':
    unittest.main()

