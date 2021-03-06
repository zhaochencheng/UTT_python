# -*- coding: utf-8 -*-
# @Time    : 2018/1/31 16:36
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_BehaviorManage.py
# @Software: PyCharm Community Edition
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.Ping import Ping
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class BehaviorManage(unittest.TestCase):
    u'''**行为管理配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    # def check_imgopen(self,location):
    #     u'''检查行为管理总开关 是否开启'''
    #     if location.get_attribute("checktype") == "0" :
    #         print(location.get_attribute("checktype"))
    #         print("行为管理总开关 -- 未开启！")
    #         print("现在开启")
    #         location.click()
    #         time.sleep(3)
    #     else:
    #         print("行为管理总开关 -- 已开启！")

    def enter_behaviorMg(self):
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 行为管理 菜单栏定位
        behaviorMange = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[6]/div/h4/span"))
        behaviorMange.click()
        print("当前位置：", behaviorMange.text)
        # 行为管理  子栏定位
        time.sleep(2)
        behaviorMg = self.driver.find_element_by_link_text("行为管理")
        behaviorMg.click()
        print("当前位置：", behaviorMg.text)

    def switch_check_open(self,state):
        u"0代表关闭,1代表开启"
        # 策略路由开关按钮 定位
        checkopen = self.driver.find_element_by_id("checkOpen")
        checkopen_status = int(checkopen.get_attribute("checktype"))
        # print("checkopen_status:",checkopen_status,type(checkopen_status))
        # print("state:",state,type(state))
        if checkopen_status == state:
            print("no operation")
            pass
        else:
            checkopen = self.driver.find_element_by_id("checkOpen")
            checkopen.click()
            print("操作按钮")
        time.sleep(2)

    def behaviorMange_config(self,behavior_rulename):
        for i in range(len(behavior_rulename)):
            #新增 定位
            add = self.driver.find_element_by_id("add")
            add.click()
            time.sleep(2)
            #规则名称 定位
            rulename = self.driver.find_element_by_xpath(".//input[@name  = 'ruleName']")
            rulename.clear()
            rulename.send_keys(behavior_rulename[i])
            #应用服务 定位
            servers = self.driver.find_element_by_xpath(".//input[@name  = 'servers']")
            servers.click()
            time.sleep(2)
            #搜索框 定位
            searchbox = self.driver.find_element_by_xpath(".//input[@id  = 'search-text-box']")
            searchbox.clear()
            searchbox.send_keys(servername[i])
            #搜索按钮 定位
            searchbutton = self.driver.find_element_by_id("search")
            searchbutton.click()
            time.sleep(3)
            #查询结果
            search_result_all =self.driver.find_elements_by_xpath("//*[@id='appSearchRes']/ul/li")
            for k in range(1,len(search_result_all)+1):
                #将搜索到的 点击 添加
                search_result = self.driver.find_element_by_xpath("//*[@id='appSearchRes']/ul/li[%d]"%k)
                search_result.click()
                time.sleep(1)
            #应用服务中的 保存 定位
            save_server = self.driver.find_elements_by_id("save")
            # save_server = self.driver.find_element_by_xpath("//*[@id='save']")
            save_server[1].click()
            time.sleep(2)
            #行为管理中 保存定位
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(4)
    def behaviorMange_show(self):
        Output_info(self.driver).output_content(behavior_rulename)
    def behaviorMange_delect(self):
        Delect_config(self.driver).delect_sameconfig(behavior_rulename)
    def behaviorMange_validate(self):
        '''
        在此处加入判断条件
        '''
        # 判断
        try:
            Ping().ping_IP("www.baidu.com")
        except BaseException as E:
            # print("ping 不通配置中的ip")
            print("error", E)
            # print(type(E))
            if E:
                print("功能生效")
            else:
                raise BaseException("功能生效不生效；未禁ping")


    # def test_17_001_behaviorMange(self):
    #     u'''行为管理配置与删除'''
    #
    #     self.enter_behaviorMg()
    #
    #     #行为管理按钮定位
    #     img = self.driver.find_element_by_xpath(".//*[@id='checkOpen']")
    #     #检查行为管理总开关 是否开启
    #     self.check_imgopen(img)
    #     # 检查页面是否有与配置文件相同的配置 有则删除
    #     Delect_config(self.driver).delect_sameconfig(behavior_rulename)
    #
    #     #配置前 先ping 一下
    #     Ping().ping_IP("www.baidu.com")
    #     print("未配置行为管理，可ping通外网")
    #     time.sleep(1)
    #
    #     # #
    #     #
    #     for i in range(len(behavior_rulename)):
    #         #新增 定位
    #         add = self.driver.find_element_by_id("add")
    #         add.click()
    #         time.sleep(2)
    #         #规则名称 定位
    #         rulename = self.driver.find_element_by_xpath(".//input[@name  = 'ruleName']")
    #         rulename.clear()
    #         rulename.send_keys(behavior_rulename[i])
    #         #应用服务 定位
    #         servers = self.driver.find_element_by_xpath(".//input[@name  = 'servers']")
    #         servers.click()
    #         time.sleep(2)
    #         #搜索框 定位
    #         searchbox = self.driver.find_element_by_xpath(".//input[@id  = 'search-text-box']")
    #         searchbox.clear()
    #         searchbox.send_keys(servername[i])
    #         #搜索按钮 定位
    #         searchbutton = self.driver.find_element_by_id("search")
    #         searchbutton.click()
    #         time.sleep(3)
    #         #查询结果
    #         search_result_all =self.driver.find_elements_by_xpath("//*[@id='appSearchRes']/ul/li")
    #         for k in range(1,len(search_result_all)+1):
    #             #将搜索到的 点击 添加
    #             search_result = self.driver.find_element_by_xpath("//*[@id='appSearchRes']/ul/li[%d]"%k)
    #             search_result.click()
    #             time.sleep(1)
    #         #应用服务中的 保存 定位
    #         save_server = self.driver.find_elements_by_id("save")
    #         # save_server = self.driver.find_element_by_xpath("//*[@id='save']")
    #         save_server[1].click()
    #         time.sleep(2)
    #         #行为管理中 保存定位
    #         save = self.driver.find_element_by_id("save")
    #         save.click()
    #         time.sleep(4)
    #
    #     # 输出：
    #     Output_info(self.driver).output_content(behavior_rulename)
    #
    #     '''
    #     在此处加入判断条件
    #
    #     '''
    #     #判断
    #     try:
    #         Ping().ping_IP("www.baidu.com")
    #     except BaseException as E:
    #         # print("ping 不通配置中的ip")
    #         print("error", E)
    #         # print(type(E))
    #         if E:
    #             print("功能生效")
    #         else:
    #             raise BaseException("功能生效不生效；未禁ping")
    #
    #
    #     #删除配置
    #     Delect_config(self.driver).delect_sameconfig(behavior_rulename)
    #     time.sleep(2)
    #
    #     # 删除配置后 再ping 一下
    #     Ping().ping_IP("www.baidu.com")
    #     print("删除 ping （行为管理），可ping通外网")

    def test_17_001_behaviorMange_config(self):
        u"行为管理开启与配置"
        #进入行为管理页面
        self.enter_behaviorMg()
        '''开启行为管理按钮'''
        #0代表关闭,1代表开启
        self.switch_check_open(1)
        '''配置前先查看页面中是否有与配置文件相同的配置，若有则删除'''
        self.behaviorMange_delect()
        '''配置行为管理---'''
        self.behaviorMange_config(behavior_rulename)
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("behaviorMange_config")
    def test_17_002_behaviorMange_show(self):
        u"行为管理页面信息核对"
        # 进入行为管理页面
        self.enter_behaviorMg()
        '''行为管理页面信息核对'''
        self.behaviorMange_show()
        '''#信息输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("behaviorMange_show")

    def test_17_003_behaviorMange_validate(self):
        u"行为管理页面功能生效判断"
        self.behaviorMange_validate()
    def test_17_004_behaviorMange_delete(self):
        u"行为管理信息删除"
        # 进入行为管理页面
        self.enter_behaviorMg()
        '''行为管理信息删除'''
        self.behaviorMange_delect()
        '''#配置删除 截图#'''
        Get_Screenshot(self.driver).get_screenshot("behaviorMange_delete")












if __name__ == '__main__':
    unittest.main()
