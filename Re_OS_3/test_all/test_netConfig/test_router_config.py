# -*- coding: utf-8 -*-
# @Time    : 2018/1/26 17:44
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_router_config.py
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

class Router_config(unittest.TestCase):
    u'''**路由配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_05_001_staticRouter(self):
        u'''静态路由配置与删除'''

        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置:",netconfig.text)
        #路由配置 定位
        router_config = self.driver.find_element_by_link_text("路由配置")
        router_config.click()
        print("当前位置:",router_config.text)
        time.sleep(2)
        statice_route = self.driver.find_element_by_link_text("静态路由")
        print("当前位置:",statice_route.text)
        print("*" * 30, '\n')


        # # 静态路由配置  # #
        #页面显示个数
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        #选择  显示个数为50
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()

        # 判断页面是否存在与配置 相同的配置
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for j in range(len(router_static_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == router_static_name[j]:
                        # 删除按钮 定位
                        delete = self.driver.find_element_by_xpath(
                            ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[9]/span[2]" % i)
                        delete.click()
                        time.sleep(1)
                        # 确认删除 定位
                        ok = self.driver.find_element_by_id("u-cfm-ok")
                        ok.click()
                        time.sleep(4)
                        print("已有%s 规则，先将其删除" % name_rule)
                        print("*" * 30, '\n')
                    else:
                        pass
                else:
                    break

        #配置前 先ping 一下 要配置的IP 是否可以ping通

        for j in range(len(router_static_name)):
            try:
                ping = Ping().ping_IP(rou_static_destNet[j])
            except BaseException as E:
                print(E)

        time.sleep(2)
        #配置
        for j in range(len(router_static_name)):
            #新增 按钮
            add = self.driver.find_element_by_id("add")
            add.click()
            time.sleep(2)
            #状态  --- 定位 开启 radio框是否被选中
            # status = webwait.until(lambda x: x.find_element_by_xpath(".//input[@name='RouteEnables' and @value  = '1']"))
            status = self.driver.find_element_by_xpath(".//input[@name='RouteEnables' and @value  = '1']")
            if status.is_selected():
                # print("规则状态 已开启")
                pass
            else:
                status.click()
                print("点击 开启 该规则")
                time.sleep(2)
            #规则名称 定位
            rule_name = self.driver.find_element_by_xpath(".//input[@name='RouteNames']")
            rule_name.clear()
            rule_name.send_keys(router_static_name[j])
            #目的网络 定位
            desip = self.driver.find_element_by_xpath(".//input[@name='DesIPs']")
            desip.clear()
            desip.send_keys(rou_static_destNet[j])
            #子网掩码 定位
            desMasks = self.driver.find_element_by_xpath(".//input[@name='DesMasks']")
            desMasks.clear()
            desMasks.send_keys(rou_static_netmask[j])
            #网关地址 定位
            GWway = self.driver.find_element_by_xpath(".//input[@name='GateWays']")
            GWway.clear()
            GWway.send_keys(rou_static_GWay[j])
            #优先级 定位
            Metrics = self.driver.find_element_by_xpath(".//input[@name='Metrics']")
            Metrics.clear()
            Metrics.send_keys(rou_static_priority[j])

            #绑定接口  绑定wan1 口   -lan 口--
            #                     ---- 要考虑如何将所有接口都能绑定 进行测试
            interface = self.driver.find_element_by_xpath(".//select[@name='Profiles']")
            # Select(interface).select_by_value("WAN1")
            Select(interface).select_by_value("LAN")
            #点击保存
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(5)
        time.sleep(2)
        # 页面显示个数
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        # 选择  显示个数为50
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()

        # 将页面配置输出
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for j in range(len(router_static_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    web_name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if web_name_rule == router_static_name[j]:
                        web_rule_name = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span"%i).text
                        self.assertEqual(web_rule_name,router_static_name[j],"页面显示规则与配置规则不同！")
                        web_rule_status= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/input"%i)
                        web_desip = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span"%i).text
                        # self.assertEqual(web_desip,rou_static_destNet[j],"页面显示目的ip与配置目的ip不同！")
                        web_GWway = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span"%i).text
                        self.assertEqual(web_GWway,rou_static_GWay[j],"页面显示网关ip与配置网关ip不同！")
                        web_priority = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span"%i).text
                        self.assertEqual(web_priority,rou_static_priority[j],"页面显示优先级与配置优先级不同！")
                        web_interface = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span"%i).text
                        print("规则名为：",web_rule_name)
                        if web_rule_status.is_selected():
                            print("该规则为开启状态")
                        else:
                            print("该规则为关闭状态")
                        print("目的网络为：",web_desip,"  网关地址为：",web_GWway,"  优先级为：",web_priority,"  绑定接口为：",web_interface)

                        time.sleep(2)
                    else:
                        pass
                else:
                    break
        print("*" * 30, '\n')


        # # 配置后 ping 一下 要配置的IP 是否可以ping通
        # # 判断路由是否生效
        for j in range(len(router_static_name)):
            ping = Ping().ping_IP(rou_static_destNet[j])

        time.sleep(2)
        #删除配置 规则
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for j in range(len(router_static_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == router_static_name[j]:
                        # 删除按钮 定位
                        delete = self.driver.find_element_by_xpath(
                            ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[9]/span[2]" % i)
                        delete.click()
                        time.sleep(1)
                        # 确认删除 定位
                        ok = self.driver.find_element_by_id("u-cfm-ok")
                        ok.click()
                        time.sleep(5)
                        print("将%s 规则，删除" % name_rule)
                        # print("*" * 30, '\n')
                    else:
                        pass
                else:
                    break
        print("*" * 30, '\n')

    def test_05_strategyRouter(self):
        u'''策略路由 开启 、关闭与策略路由配置'''
        pass










if __name__ == '__main__':
    unittest.main()





