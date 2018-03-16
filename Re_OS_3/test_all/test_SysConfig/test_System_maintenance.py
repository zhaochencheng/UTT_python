# -*- coding: utf-8 -*-
# @Time    : 2018/2/6 21:54
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_System_maintenance.py
# @Software:PyCharm
from datetime import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time,random
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class System_maintenance(unittest.TestCase):
    u'''**系统维护**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def check_upgardesuccess(self):
        u'''检查升级是否成功'''
        #此时在上传版本
        time.sleep(30)
        #ping lan口 看是否重启
        # 是否重启，最好看设备的运行时间；
    def enter_system_maintenance(self):
        u'''进入系统配置---系统维护页面'''
        #显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：", Sysconfig.text)
        # 系统维护 定位
        system_maintenance = self.driver.find_element_by_link_text("系统维护")
        system_maintenance.click()
        print("当前位置：", system_maintenance.text)

    def System_upgrade(self):
        u'''进行系统升级配置'''
        # 系统升级页面定位
        system_upgrade = self.driver.find_element_by_link_text("系统升级")
        system_upgrade.click()
        print("当前位置：", system_upgrade.text)
        # 软件版本 定位
        softwareVersion = self.driver.find_element_by_xpath(".//input[@name = 'softwareVersion1']")
        version = softwareVersion.get_attribute("value")
        print("软件版本为：", version)
        time.sleep(4)
        self.driver.refresh()
        time.sleep(4)
        # 版本检测情况
        check_version = self.driver.find_element_by_xpath("//*[@id='iframe1']/table/tbody/tr[2]/td[3]/span")
        print("版本检查情况：", check_version.text)
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("System_upgrade")
        # 输入 软件
        time.sleep(2)  # 必加等待！！！
        # self.driver.find_element_by_name("updatesoftware").clear()#不能有clear
        sendsoftware = self.driver.find_element_by_name("updatesoftware")
        sendsoftware.send_keys(update_path)  # 考虑以下这个路径怎么写
        time.sleep(2)
        print("software:", sendsoftware.get_attribute("placeholder"))
        # 升级 button 定位
        upgarde = self.driver.find_element_by_id("update")
        upgarde.click()
        time.sleep(2)
        # 确认 定位
        # ok = self.driver.find_element_by_id("u-cfm-ok")
        # ok.click()



    def test_32_001_System_upgrade(self):
        u'''系统升级操作'''
        #进入系统配置---系统维护页面
        self.enter_system_maintenance()
        '''进行系统升级'''
        self.System_upgrade()
        '''升级成功检测'''


    def test_32_002_Application_feature_library(self):
        u'''应用特征库显示'''
        # 进入系统配置---系统维护页面
        self.enter_system_maintenance()
        #应用特征库 定位
        time.sleep(2)
        library = self.driver.find_element_by_link_text("应用特征库")
        library.click()
        print("当前位置:",library.text)
        time.sleep(3)
        print("*" * 30, '\n')
        #应用策略库版本 定位
        strategyname = self.driver.find_element_by_xpath("//b[@name = 'strategyName']")
        print("应用策略库版本:",strategyname.text)
        #应用优先模板版本
        priorityname = self.driver.find_element_by_xpath(".//*[@name= 'priorityName']")
        print("应用优先模板版本:",priorityname.text)
        #版本状态  定位
        showstate = self.driver.find_element_by_xpath(".//*[@id = 'showState']/span")
        print("版本状态:",showstate.text)
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("Application_feature_library")




    def test_32_003_Configuration_management(self):
        u'''配置管理'''
        pass
    def test_32_004_Reboot_DUT(self):
        u'''重启操作'''
        # 进入系统配置---系统维护页面
        self.enter_system_maintenance()
        #重启设备 定位
        time.sleep(2)
        rebootDUT = self.driver.find_element_by_link_text("重启设备")
        rebootDUT.click()
        print("当前位置:",rebootDUT.text)
        #重启按钮 定位
        reboot_button= self.driver.find_element_by_id("reboot")
        reboot_button.click()
        print("点击重启按钮!")
        # 确认 重启 定位
        time.sleep(2)
        # ok = self.driver.find_element_by_id("u-cfm-ok")
        # ok.click()
        print("确认重启....正在启动中...")

        '''此处加入 重启生效的判断方法'''


if __name__ == '__main__':
    unittest.main()



