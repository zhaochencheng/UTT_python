# -*- coding: utf-8 -*-
# @Time    : 2018/2/4 15:44
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_accStatu.py
# @Software: PyCharm
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

class AccStatu(unittest.TestCase):
    u'''**用户状态**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def Users_joingroups(self):
        u'''将临时用户全部加入分组'''
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

        # except BaseException as  E:
        #     print("当前无分组!")


    def blackList(self):
        u'''将用户拉黑并删除'''

        # #**将用户拉黑 **# #

        # #页面显示个数
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        #  #选择  显示个数为50
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        # 标题栏 中有多少个子项
        head_all = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th")
        print("标题子项：", len(head_all))
        #  #展开
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)

        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                name_rule = self.driver.find_element_by_xpath(
                    ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                #
                print("*" * 30, '\n')
                for k in range(1, len(head_all) + 1):
                    try:
                        headname = self.driver.find_element_by_xpath(
                            "//*[@id='1']/div/div/div[1]/table/thead/tr/th[%d]/span" % k)
                        if headname.text == '编辑':
                            # 拉黑 用户
                            calldown_list = self.driver.find_elements_by_id("calldown")
                            calldown = calldown_list[i]
                            calldown.click()
                            time.sleep(3)
                            # 确认 拉黑
                            ok = self.driver.find_element_by_id("u-cfm-ok")
                            ok.click()
                            time.sleep(3)
                        else:
                            pass
                    except BaseException as  E:
                        pass
                time.sleep(2)
                print("先将‘ %s ’用户拉黑  " % name_rule)
                print("*" * 30, '\n')

            else:
                break

        # 测试用户 能否 访问外网
        # try:
        #     ping = Ping().ping_IP("www.baidu.com")
        # except BaseException as E:
        #     # print("ping 不通配置中的ip")
        #     print("error", E)
        #     print(type(E))
        #     if E:
        #         print("功能生效")
        #     else:
        #         raise BaseException("功能生效不生效；未禁ping")
        time.sleep(3)
        self.driver.refresh()
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        # 进入黑名单页面 查看黑名单；
        blacklist = self.driver.find_element_by_link_text("黑名单")
        blacklist.click()
        print("当前位置：",blacklist.text)
        #输出黑名单页面信息
        Output_info(self.driver).output_all()

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


    def test_14_001_accStatu(self):
        u'''用户状态显示与操作'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        #用户状态 定位
        accStatus = self.driver.find_element_by_link_text("用户状态")
        accStatus.click()
        #将页面 用户状态列表 信息输出
        Output_info(self.driver).output_all()

        #将临时用户加入分组中
        self.Users_joingroups()

        #将页面 用户状态列表 信息输出
        time.sleep(5)
        self.driver.refresh()
        time.sleep(3)
        Output_info(self.driver).output_all()

        '''黑名单生效
        #将本机ip拉黑导致无法再进入web页面。拉黑别的ip如何测试？？？？
        '''

        # self.blackList()

    def test_14_001_accStatu_Users_joingroups(self):
        u'''将临时用户加入分组中'''
        #进入用户管理---用户状态页面
        self.enter_accStatu()
        #将临时用户加入分组中
        self.Users_joingroups()





if __name__ == '__main__':
    unittest.main()