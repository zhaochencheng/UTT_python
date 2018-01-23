# -*- coding: utf-8 -*-
# @Time    : 2018/1/23 22:07
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_Port_mapping.py
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

class Port_mapping(unittest.TestCase):
    u'''**端口映射**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_04_001_static_port_mapping(self):
        u'''静态映射配置,修改与删除'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：",netconfig.text)
        #端口映射 定位
        port_map =self.driver.find_element_by_link_text("端口映射")
        port_map.click()
        print("当前位置:",port_map.text)

        # 新增 按钮 定位
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(1)
        #规则名称 定位
        rulename = webwait.until(lambda x: x.find_element_by_xpath(".//input[@name='IDs']"))
        rulename.send_keys(new_rulename[0])
        #绑定几口 定位
        bindinterface = self.driver.find_element_by_xpath(".//select[@name='NatBinds']")
        Select(bindinterface).select_by_value("WAN1") #选择wan1口
        # Select(bindinterface).select_by_index(0)
        #内网地址 定位
        inaddress = self.driver.find_element_by_xpath(".//input[@name='IPs']")
        inaddress.clear()
        inaddress.send_keys(inaddr[0])
        #内网端口 定位
        inport_left = self.driver.find_element_by_xpath(".//input[@name = 'inS']")
        inport_left.clear()
        inport_left.send_keys(inport[0])
        inport_right = self.driver.find_element_by_xpath(".//input[@name = 'inE']")
        inport_right.clear()
        inport_right.send_keys(inport[0])
        #外部端口 定位
        outport_left = self.driver.find_element_by_xpath(".//input[@name = 'outS']")
        outport_left.clear()
        outport_left.send_keys(outport[0])
        outport_right = self.driver.find_element_by_xpath(".//input[@name = 'outE']")
        outport_right.clear()
        outport_right.send_keys(outport[0])
        time.sleep(1)
        #保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(2)

        # 每页显示  --显示50条
        shownumber = self.driver.find_element_by_xpath(".//button[@id='1']")
        shownumber.click()
        time.sleep(1)
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        time.sleep(1)
        # 在页面查看 配置的 静态映射 是否生效
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        print("每页显示个数为:",len(tr))
        # # 判断配置的静态映射 是否生效 并将其输出;
        for j in range(len(new_rulename)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == new_rulename[j]:
                        ipaddr = self.driver.find_element_by_xpath(
                            ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                        self.assertEqual(ipaddr, inaddr[j], "配置IP与页面生效ip不一致")
                        port = self.driver.find_element_by_xpath(
                            ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % i).text
                        # self.assertEqual(vid, vlan_id[j], "配置vlan id 与页面生效vlan id不一致")
                        print("规则名称:", name_rule, "   内网IP地址:", ipaddr, "   端口映射关系:", port)
                    else:
                        pass
                else:
                    break
        #将配置好的页面截图
        nowTime = time.strftime("%Y%m%d.%H_%M_%S")
        # 截图存放路径  相对路径
        # png_path = os.path.dirname(os.getcwd()) + '\Screenshot'
        self.driver.get_screenshot_as_file(
            r'F:\untitled\Re_OS_3\Screenshot\net_config_png\port_mapping_png\%s.png' % (nowTime + '_static_port_mapping'))
        # #将配置的 静态映射 删除
        time.sleep(2)
        for j in range(len(new_rulename)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == new_rulename[j]:
                        # 删除按钮 定位
                        delete = self.driver.find_element_by_xpath(
                            ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]" % i)
                        delete.click()
                        # 确认删除 定位
                        ok = self.driver.find_element_by_id("u-cfm-ok")
                        ok.click()
                        time.sleep(4)
                        print("已将%s 规则删除"%name_rule)
                    else:
                        pass
                else:
                    break
                    # 将配置好的页面截图
        nowTime = time.strftime("%Y%m%d.%H_%M_%S")
        # 截图存放路径  相对路径
        # png_path = os.path.dirname(os.getcwd()) + '\Screenshot'
        self.driver.get_screenshot_as_file(
            r'F:\untitled\Re_OS_3\Screenshot\net_config_png\port_mapping_png\%s.png' % (
            nowTime + '_static_port_mapping'))



if __name__ == '__main__':
    unittest.main()