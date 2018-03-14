# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 10:55
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_organize_member.py
# @Software: PyCharm Community Edition
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

class Organization_member(unittest.TestCase):
    u'''**组织成员**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def add_newTree(self):
        u'''创建分组'''
        for i in range(len(newtree)):
            add = self.driver.find_element_by_id("addBtn_newTree_1")
            add.click()
            time.sleep(2)
            #组名称 定位
            name = self.driver.find_element_by_xpath(".//input[@name='name']")
            name.send_keys(newtree[i])
            #保存 定位
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(2)

    def output_member(self):
        u'''将展示页面信息 输出'''

        # #页面显示个数
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        #  #选择  显示个数为50
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        # 标题栏 中有多少个子项
        head_all = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/thead/tr/th")

        print("标题子项：", len(head_all))
        #  #展开
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)

        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                name_rule = self.driver.find_element_by_xpath(
                    ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                # 标题栏 与 内容 同步输出！
                print("*" * 30, '\n')
                for k in range(1, len(head_all) + 1):
                    try:
                        headname = self.driver.find_element_by_xpath(
                            "//*[@id='2']/div/div/div[1]/table/thead/tr/th[%d]/span" % k)
                        if headname.is_displayed():
                            content = self.driver.find_element_by_xpath(
                                '//*[@id="2"]/div/div/div[1]/table/tbody/tr[%d]/td[%d]/span' % (i, k)).text
                            print(headname.text, ":", content)
                        else:
                            pass
                    except BaseException as  E:
                        pass

                time.sleep(2)
                print("该 ‘ %s ’ 信息已全部输出 " % name_rule)
                print("*" * 30, '\n')

            else:
                # print("页面无信息！")
                break

    def delect_sameconfig(self,config_name):
        u'''将页面与配置信息 相同的配置删除'''
        # #页面显示个数
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        #  #选择  显示个数为50
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        # 标题栏 中有多少个子项
        head_all = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/thead/tr/th")
        print("标题子项：", len(head_all))
        #  #展开
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for j in range(len(config_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                    if name_rule == config_name[j]:
                        #
                        print("*" * 30, '\n')
                        for k in range(1, len(head_all) + 1):
                            try:
                                headname = self.driver.find_element_by_xpath(
                                    "//*[@id='2']/div/div/div[1]/table/thead/tr/th[%d]/span" % k)
                                if headname.text == '编辑':
                                    # 删除 页面与配置相同的 配置
                                    delete = self.driver.find_element_by_xpath(
                                        '//*[@id="2"]/div/div/div[1]/table/tbody/tr[%d]/td[%d]/span[2]' % (i, k))
                                    delete.click()
                                    time.sleep(3)
                                    # 确认删除
                                    ok = self.driver.find_element_by_id("u-cfm-ok")
                                    ok.click()
                                    time.sleep(3)
                                else:
                                    pass
                            except BaseException as  E:
                                pass
                        time.sleep(2)
                        print("先将‘ %s ’与配置文件相同规则删除！  " % name_rule)
                        print("*" * 30, '\n')
                    else:
                        pass
                else:
                    break
        # print("页面无相同信息！")

    def enter_Organization_member(self):
        '''进入用户管理---组织成员页面'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        print("当前位置：", usermanage.text)
        # 组织成员 定位
        organization_member = self.driver.find_element_by_link_text("组织成员")
        organization_member.click()
        print("当前位置：", organization_member.text)


    def test_13_001_Organization_member_config(self):
        u'''组织成员配置'''
        #进入用户管理---组织成员页面
        self.enter_Organization_member()
        '''组织成员配置'''
        self.add_newTree()
        print("组织成员配置-完成")
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("Organization_member_config")

    def test_13_002_Organization_member_show(self):
        u'''组织成员页面信息输出'''
        # 进入用户管理---组织成员页面
        self.enter_Organization_member()
        '''组织成员页面信息输出'''
        self.output_member()
        '''#输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("Organization_member_show")

if __name__ == '__main__':
    unittest.main()