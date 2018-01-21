# -*- coding: utf-8 -*-
# @Time    : 2018/1/19 20:39
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_wan_config.py
# @Software: PyCharm Community Edition
import unittest
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
#导入Select 模块
from selenium.webdriver.support.select import Select
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Config_data.config import *
import os

class Wan_config(unittest.TestCase):
    u'''**wan口配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def test_1_001_wan_config_static(self):
        u'''--wan口固定ip配置与删除--'''

        #网络配置  定位
        netconfig = self.driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span")
        netconfig.click()
        print("当前位置：",netconfig.text)
        #外网配置 定位
        wan_config = self.driver.find_element_by_link_text("外网配置")
        wan_config.click()
        print("当前位置：",wan_config.text)
        #wan 口编辑按钮  定位
        edit = self.driver.find_element_by_class_name("glyphicon-edit")
        edit.click()

        #共有多少个wan口
        all_interface = self.driver.find_elements_by_xpath(".//select[@name ='PortName']/option")
        print("共有 ",len(all_interface)," wan口")
        #返回按钮
        back = self.driver.find_element_by_id("back")
        back.click()
        time.sleep(2)
        for i in range(len(all_interface)):
            edit_again = self.driver.find_element_by_class_name("glyphicon-edit")
            edit_again.click()
            # 接口
            interface = self.driver.find_element_by_xpath(".//select[@name ='PortName']")
            Select(interface).select_by_index(i)


            #连接类型定位  ----选择 固定接入
            connType = self.driver.find_element_by_xpath(".//select[@name ='connectionType']")
            Select(connType).select_by_value("STATIC")
            time.sleep(1)
            #连接类型总数
            # all_connType = self.driver.find_elements_by_xpath(".//select[@name ='connectionType']/option")
            # print("连接类型有：",len(all_connType),"种。")

            #ip 地址
            IP = self.driver.find_element_by_xpath(".//input[@name = 'staticIp']")
            IP.clear()
            IP.send_keys(wan_ip1[i])
            #子网掩码
            Static_netmark = self.driver.find_element_by_xpath(".//input[@name = 'staticNetmask']")
            Static_netmark.clear()
            Static_netmark.send_keys(netmask)
            #网关地址
            GateWay = self.driver.find_element_by_xpath(".//input[@name = 'staticGateway']")
            GateWay.clear()
            GateWay.send_keys(GWaddr1)
            # 主DNS
            DNS = self.driver.find_element_by_xpath(".//input[@name = 'staticPriDns']")
            DNS.clear()
            DNS.send_keys(DNSaddr)
            #保存
            Save_button = self.driver.find_element_by_xpath(".//button[@id='save']")
            Save_button.click()
            time.sleep(10)
            waiwangpeizhi = self.driver.find_element_by_xpath(".//*[@id='content']/nav/ul/li[1]/a")
            waiwangpeizhi.click()
            time.sleep(1)

            '''输出刚配置接口 在页面的显示信息'''
            #接口
            web_interface = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[1]/a"%(i+1)).text
            web_connType = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span"%(i+1)).text
            web_netmark = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span"%(i+1)).text
            web_GWway = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span"%(i+1)).text
            web_ip = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % (i + 1)).text
            web_connect_status = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1)).text
            print("*" * 30, '\n')
            print("当前接口为：",web_interface)
            print("连接状态：",web_connect_status)
            print("连接类型为：",web_connType)
            print("wan口ip为：",web_ip)
            print("子网掩码为：",web_netmark)
            print("网关地址为：",web_GWway)
            print("*" * 30, '\n')


            # 判断页面显示wan口ip 与 配置的wan口ip是否相同；
            self.assertEqual(web_ip, wan_ip1[i], "%s 配置IP与页面生效IP不一致"%web_interface)

            # 判断端口状态
            self.assertEqual(web_connect_status, "已连接", "%s 端口连接状态错误--可能网线未连接或该端口有问题"%web_interface)

            #ping 网关
            return1 = os.system('ping -n 2 -w 2 %s' % GWaddr)
            if return1:
                print('ping %s is fail' % GWaddr)
                raise Exception('ping %s is fail,ping网关不通！' % GWaddr)
                count_False = 1
            else:
                print('ping %s is ok' % GWaddr)
                count_True = 1
            #删除刚才的配置
            if i == 0 :
                #因为wan1口不可删除，在该处跳过，
                pass
            else:
                #删除 图标
                delete = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[13]/span[2]"%(i+1))
                delete.click()
                #确认删除
                delete_ok = self.driver.find_element_by_xpath(".//*[@id='u-cfm-ok']")
                delete_ok.click()
                time.sleep(10)
                #点击刷新
                shuaxin = self.driver.find_element_by_xpath(".//*[@id='otherBtns']/button")
                shuaxin.click()
                time.sleep(3)
                waiwangpeizhi = self.driver.find_element_by_xpath(".//*[@id='content']/nav/ul/li[1]/a")
                waiwangpeizhi.click()
                time.sleep(1)
                delet_web_interface = self.driver.find_element_by_xpath(
                    ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[1]/a" % (i + 1)).text
                delet_web_connType = self.driver.find_element_by_xpath(
                    ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % (i + 1)).text
                delet_web_netmark = self.driver.find_element_by_xpath(
                    ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % (i + 1)).text
                delet_web_GWway = self.driver.find_element_by_xpath(
                    ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % (i + 1)).text
                delet_web_ip = self.driver.find_element_by_xpath(
                    ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % (i + 1)).text
                delet_web_connect_status = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1)).text
                print("*" * 30, '\n','删除后接口信息为：','\n')
                print("当前接口为：", delet_web_interface)
                print("连接状态：", delet_web_connect_status)
                print("连接类型为：", delet_web_connType)
                print("wan口ip为：", delet_web_ip)
                print("子网掩码为：", delet_web_netmark)
                print("网关地址为：", delet_web_GWway)
                print("*" * 30, '\n')
                self.assertEqual(delet_web_connect_status,'未配置',"%s 端口配置未删除"%delet_web_interface)


    def test_1_002_wan_config_DHCP(self):
        u'''--wan口DHCP配置与释放--'''

        # 网络配置  定位
        netconfig = self.driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span")
        netconfig.click()
        print("当前位置：", netconfig.text)
        # 外网配置 定位
        wan_config = self.driver.find_element_by_link_text("外网配置")
        wan_config.click()
        print("当前位置：", wan_config.text)
        # wan 口编辑按钮  定位
        edit = self.driver.find_element_by_class_name("glyphicon-edit")
        edit.click()
        # 共有多少个wan口
        all_interface = self.driver.find_elements_by_xpath(".//select[@name ='PortName']/option")
        print("共有 ", len(all_interface), " wan口")
        # 返回按钮
        back = self.driver.find_element_by_id("back")
        back.click()
        time.sleep(2)
        for i in range(1,len(all_interface)): # 应从0开始，
            edit_again = self.driver.find_element_by_class_name("glyphicon-edit")
            edit_again.click()
            # 接口
            interface = self.driver.find_element_by_xpath(".//select[@name ='PortName']")
            Select(interface).select_by_index(i)

            # 连接类型定位  ----选择 DHCP
            connType = self.driver.find_element_by_xpath(".//select[@name ='connectionType']")
            Select(connType).select_by_value("DHCP")
            time.sleep(1)
            # 保存
            Save_button = self.driver.find_element_by_xpath(".//button[@id='save']")
            Save_button.click()
            time.sleep(10)
            #页面wan口的连接状态
            web_connect_status = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1))
            web_connect_status.click()
            #更新定位
            gengxin  = self.driver.find_element_by_xpath(".//*[@id='otherBtns']/button[1]")
            gengxin.click()
            time.sleep(3)
            #刷新定位
            shuaxin = self.driver.find_element_by_xpath(".//*[@id='otherBtns']/button[3]")
            shuaxin.click()
            time.sleep(10)
            waiwangpeizhi = self.driver.find_element_by_xpath(".//*[@id='content']/nav/ul/li[1]/a")
            waiwangpeizhi.click()
            time.sleep(1)

            '''输出刚配置接口 在页面的显示信息'''
            # 接口
            web_interface = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[1]/a" % (i + 1)).text
            web_connType = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % (i + 1)).text
            web_netmark = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % (i + 1)).text
            web_GWway = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % (i + 1)).text
            web_ip = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % (i + 1)).text
            web_connect_status = self.driver.find_element_by_xpath(
                "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1)).text
            print("*" * 30, '\n')
            print("当前接口为：", web_interface)
            print("连接状态：", web_connect_status)
            print("连接类型为：", web_connType)
            print("wan口ip为：", web_ip)
            print("子网掩码为：", web_netmark)
            print("网关地址为：", web_GWway)
            print("*" * 30, '\n')


            # 判断端口状态
            try:
                self.assertEqual(web_connect_status, "已连接", "%s 端口连接状态错误--可能网线未连接或该端口有问题" % web_interface)
            except Exception as  E:
                print(E)
                nowTime = time.strftime("%Y%m%d.%H_%M_%S")
                #截图存放路径  相对路径
                # png_path = os.path.dirname(os.getcwd()) + '\Screenshot'
                self.driver.get_screenshot_as_file(r'F:\untitled\Re_OS_3\Screenshot\%s.jpg' % (nowTime+'_wan_config_DHCP'))
                raise
            # ping 网关 ---判断网通？
            return1 = os.system('ping -n 2 -w 2 %s' % web_GWway)
            if return1:
                print('ping %s is fail' % web_GWway)
                raise Exception('ping %s is fail,ping网关不通！' % web_GWway)
                count_False = 1
            else:
                print('ping %s is ok' % web_GWway)
                count_True = 1

            # 释放wan口
            sf_web_connect_status = self.driver.find_element_by_xpath(
                "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1))
            sf_web_connect_status.click()
            #点击释放按钮
            shifang = self.driver.find_element_by_xpath(".//*[@id='otherBtns']/button[2]")
            shifang.click()
            time.sleep(3)
            #点击刷新按钮
            shuaxin = self.driver.find_element_by_xpath(".//*[@id='otherBtns']/button[3]")
            shuaxin.click()
            time.sleep(5)
            waiwangpeizhi = self.driver.find_element_by_xpath(".//*[@id='content']/nav/ul/li[1]/a")
            waiwangpeizhi.click()
            time.sleep(1)
            '''输出释放接口后 在页面的显示信息'''
            # 接口
            web_interface = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[1]/a" % (i + 1)).text
            web_connType = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % (i + 1)).text
            web_netmark = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % (i + 1)).text
            web_GWway = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % (i + 1)).text
            web_ip = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % (i + 1)).text
            web_connect_status = self.driver.find_element_by_xpath(
                "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1)).text
            print("*" * 30, '\n','释放后接口信息为：','\n')
            print("当前接口为：", web_interface)
            print("连接状态：", web_connect_status)
            print("连接类型为：", web_connType)
            print("wan口ip为：", web_ip)
            print("子网掩码为：", web_netmark)
            print("网关地址为：", web_GWway)
            print("*" * 30, '\n')

    def test_1_003_wan_config_PPPoE(self):
        u'''PPPoE的配置与挂断'''

        # 网络配置  定位
        netconfig = self.driver.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span")
        netconfig.click()
        print("当前位置：", netconfig.text)
        # 外网配置 定位
        wan_config = self.driver.find_element_by_link_text("外网配置")
        wan_config.click()
        print("当前位置：", wan_config.text)
        # wan 口编辑按钮  定位
        edit = self.driver.find_element_by_class_name("glyphicon-edit")
        edit.click()
        # 共有多少个wan口
        all_interface = self.driver.find_elements_by_xpath(".//select[@name ='PortName']/option")
        print("共有 ", len(all_interface), " wan口")
        # 返回按钮
        back = self.driver.find_element_by_id("back")
        back.click()
        time.sleep(2)
        for i in range(1, len(all_interface)):  # 应从0开始，
            edit_again = self.driver.find_element_by_class_name("glyphicon-edit")
            edit_again.click()
            # 接口
            interface = self.driver.find_element_by_xpath(".//select[@name ='PortName']")
            Select(interface).select_by_index(i)

            # 连接类型定位  ----选择 PPPOE
            connType = self.driver.find_element_by_xpath(".//select[@name ='connectionType']")
            Select(connType).select_by_value("PPPOE")
            time.sleep(1)
            #上网账号 输入
            loginname = self.driver.find_element_by_xpath(".//input[@name='pppoeUser']")
            loginname.clear()
            loginname.send_keys(pppoeuser[i])
            #上网密码 输入
            loginpwd = self.driver.find_element_by_xpath(".//input[@name='pppoePass']")
            loginpwd.clear()
            loginpwd.send_keys(pppoepwd[i])
            #点击保存
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(10)
            self.driver.refresh()
            # 页面wan口的连接状态
            web_connect_status = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1))
            # web_connect_status = WebDriverWait(self.driver,10,0.5).until(lambda x: x.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1)))
            web_connect_status.click()
            #拨号
            baohao = self.driver.find_element_by_xpath(".//*[@id='otherBtns']/button[2]")
            baohao.click()
            time.sleep(3)
            # 点击刷新按钮
            shuaxin = self.driver.find_element_by_xpath(".//*[@id='otherBtns']/button[3]")
            shuaxin.click()
            time.sleep(5)
            waiwangpeizhi = self.driver.find_element_by_xpath(".//*[@id='content']/nav/ul/li[1]/a")
            waiwangpeizhi.click()
            time.sleep(1)

            '''输出刚配置接口 在页面的显示信息'''
            # 接口
            web_interface = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[1]/a" % (i + 1)).text
            web_connType = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % (i + 1)).text
            web_netmark = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % (i + 1)).text
            web_GWway = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % (i + 1)).text
            web_ip = self.driver.find_element_by_xpath(
                ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % (i + 1)).text
            web_connect_status = self.driver.find_element_by_xpath(
                "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/a" % (i + 1)).text
            print("*" * 30, '\n')
            print("当前接口为：", web_interface)
            print("连接状态：", web_connect_status)
            print("连接类型为：", web_connType)
            print("wan口ip为：", web_ip)
            print("子网掩码为：", web_netmark)
            print("网关地址为：", web_GWway)
            print("*" * 30, '\n')











if __name__ == '__main__':
    suit = unittest.TestSuite()
    # suit.addTest(Wan_config("test_1_001_wan_config_static"))
    suit.addTest(Wan_config("test_1_002_wan_config_DHCP"))
    runner = unittest.TextTestRunner()
    runner.run(suit)






