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
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.Ping import Ping

class BehaviorManage(unittest.TestCase):
    u'''**行为管理配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def check_imgopen(self,location):
        u'''检查行为管理总开关 是否开启'''
        if location.get_attribute("checktype") == "0" :
            print(location.get_attribute("checktype"))
            print("行为管理总开关 -- 未开启！")
            print("现在开启")
            location.click()
            time.sleep(3)
        else:
            print("行为管理总开关 -- 已开启！")

    def Output_web_info(self):
        one = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th[1]/input").text
        two = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th[2]/span").text
        three = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th[3]/span").text
# text        four = self.driver.find_element_by_xpath("//*[@id="1"]/div/div/div[1]/table/thead/tr/th[4]/span")
#         five = self.driver.find_element_by_xpath("//*[@id="1"]/div/div/div[1]/table/thead/tr/th[5]/span")
#         six = self.driver.find_element_by_xpath("//*[@id="1"]/div/div/div[1]/table/thead/tr/th[6]/span")
#         seven = self.driver.find_element_by_xpath("//*[@id="1"]/div/div/div[1]/table/thead/tr/th[7]/span")
#         eight = self.driver.find_element_by_xpath("//*[@id="1"]/div/div/div[1]/table/thead/tr/th[8]/span")

        head_all = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th")

        one = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th[1]/input").text
        headname  = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th[1]/input").text
        # 页面显示个数
        # shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        # shownumber.click()
        # time.sleep(1)
        # # 选择  显示个数为50
        # number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        # number_50.click()
        #
        # # 判断页面是否存在与配置 相同的配置
        # tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # # print("每页显示个数为:", len(tr))
        # time.sleep(2)
        # for j in range(len(behavior_rulename)):
        #     for i in range(1, len(tr) + 1):
        #         # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
        #         td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
        #         if len(td) > 1:
        #             name_rule = self.driver.find_element_by_xpath(
        #                 ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
        #             if name_rule == behavior_rulename[j]:
        #                 # 删除按钮 定位
        #                 delete = self.driver.find_element_by_xpath(
        #                     ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[9]/span[2]" % i)
        #                 delete.click()
        #                 time.sleep(1)
        #                 # 确认删除 定位
        #                 ok = self.driver.find_element_by_id("u-cfm-ok")
        #                 ok.click()
        #                 time.sleep(4)
        #                 print("已有%s 规则，先将其删除" % name_rule)
        #                 print("*" * 30, '\n')
        #             else:
        #                 pass
        #         else:
        #             break


    def test_17_001_behaviorMange(self):
        u'''行为管理配置与删除'''

        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #行为管理 菜单栏定位
        behaviorMange = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[6]/div/h4/span"))
        behaviorMange.click()
        print("当前位置：",behaviorMange.text)
        #行为管理  子栏定位
        time.sleep(2)
        behaviorMg = self.driver.find_element_by_link_text("行为管理")
        behaviorMg.click()
        print("当前位置：",behaviorMg.text)
        #行为管理按钮定位
        img = self.driver.find_element_by_xpath(".//*[@id='checkOpen']")
        #检查行为管理总开关 是否开启
        self.check_imgopen(img)
        check = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[1]/input")
        print("text:",check.text)
        check1 = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[2]/span")
        print("tests:",check1.text)

        # #
        #
        # #新增 定位
        # add = self.driver.find_element_by_id("add")
        # add.click()
        # time.sleep(2)
        # #规则名称 定位
        # rulename = self.driver.find_element_by_xpath(".//input[@name  = 'ruleName']")
        # rulename.clear()
        # rulename.send_keys(behavior_rulename[0])
        # #应用服务 定位
        # servers = self.driver.find_element_by_xpath(".//input[@name  = 'servers']")
        # servers.click()
        # time.sleep(2)
        # #搜索框 定位
        # searchbox = self.driver.find_element_by_xpath(".//input[@id  = 'search-text-box']")
        # searchbox.clear()
        # searchbox.send_keys(servername[0])
        # #搜索按钮 定位
        # searchbutton = self.driver.find_element_by_id("search")
        # searchbutton.click()
        # time.sleep(3)
        # #查询结果
        # search_result_all =self.driver.find_elements_by_xpath("//*[@id='appSearchRes']/ul/li")
        # for i in range(1,len(search_result_all)+1):
        #     #将搜索到的 点击 添加
        #     search_result = self.driver.find_element_by_xpath("//*[@id='appSearchRes']/ul/li[%d]"%i)
        #     search_result.click()
        #     time.sleep(1)
        # #应用服务中的 保存 定位
        # save_server = self.driver.find_elements_by_id("save")
        # # save_server = self.driver.find_element_by_xpath("//*[@id='save']")
        # save_server[1].click()
        # time.sleep(2)
        # #行为管理中 保存定位
        # save = self.driver.find_element_by_id("save")
        # save.click()
        # time.sleep(3)








if __name__ == '__main__':
    unittest.main()
