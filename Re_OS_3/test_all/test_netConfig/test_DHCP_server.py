# -*- coding: utf-8 -*-
# @Time    : 2018/3/12 9:39
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_DHCP_server.py
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
from Re_OS_3.Public.Get_screenshot import Get_Screenshot
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_Config import Delect_config

class Lan_config(unittest.TestCase):
    u'''**Lan口配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def enter_DHCP(self):
        u"进行以下操作：点击网络配置---DHCP服务"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：", netconfig.text)
        # 内网配置 定位
        DHCPserver = self.driver.find_element_by_link_text("DHCP服务")
        DHCPserver.click()
        print("当前位置：", DHCPserver.text)
        time.sleep(2)
    def DHCP_config(self):
        u'''进行DHCP配置'''
        for i in range(len(vlan_lanipname)):
            #新增 定位
            add = self.driver.find_element_by_id("add")
            add.click()
            time.sleep(2)
            #地址池 定位
            poolname = self.driver.find_element_by_xpath(".//input[@name = 'poolName']")
            poolname.clear()
            poolname.send_keys(vlan_lanipname[i])
            # 新增 按钮
            littleAdd = self.driver.find_element_by_id("littleAdd")
            littleAdd.click()
            time.sleep(2)
            #vlan  名称
            lanIpName = self.driver.find_element_by_xpath(".//input[@name = 'lanIpName']")
            lanIpName.clear()
            lanIpName.send_keys(vlan_lanipname[i])
            #ip 地址
            lanIp = self.driver.find_element_by_xpath(".//input[@name = 'lanIp']")
            lanIp.clear()
            lanIp.send_keys(vlan_ip[i])
            #vlan id
            lanVid = self.driver.find_element_by_xpath(".//input[@name = 'lanVid']")
            lanVid.clear()
            lanVid.send_keys(vlan_id[i])
            #保存
            save_all = self.driver.find_elements_by_id("save")
            save = save_all[1]
            save.click()
            time.sleep(4)
            #起始地址 定位
            dhcpStart = self.driver.find_element_by_xpath(".//input[@name = 'dhcpStart']")
            dhcpStart.clear()
            dhcpStart.send_keys(dhcpStart_vlanip[i])
            #结束地址 定位
            dhcpEnd = self.driver.find_element_by_xpath(".//input[@name = 'dhcpEnd']")
            dhcpEnd.clear()
            dhcpEnd.send_keys(dhcpEnd_vlanip[i])
            #子网掩码 定位
            dhcpMask = self.driver.find_element_by_xpath(".//input[@name = 'dhcpMask']")
            dhcpMask.clear()
            dhcpMask.send_keys(dhcpMask_vlanip[i])
            #网关地址 定位
            dhcpGateway =self.driver.find_element_by_xpath(".//input[@name = 'dhcpGateway']")
            dhcpGateway.clear()
            dhcpGateway.send_keys(dhcpGateway_vlanip[i])
            #主DNS服务器 定位
            dhcpPriDns = self.driver.find_element_by_xpath(".//input[@name = 'dhcpPriDns']")
            dhcpPriDns.clear()
            dhcpPriDns.send_keys(dhcpPriDns_vlanip[i])
            #保存 定位
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(4)
            '''#配置后 截图#'''
            Get_Screenshot(self.driver).get_screenshot("Vlanvid_%s_DHCP_server_config" % (vlan_lanipname[i]))

    def DHCP_web_config_check_and_show(self,config_name):
        u'''将展示页面与配置相同的信息 输出'''

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
        for j in range(len(config_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                    if name_rule == config_name[j]:
                        interface_name =self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span"%i).text
                        beginIp = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span"%i).text
                        endIp = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span"%i).text
                        netmask= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span"%i).text
                        GwAddr_web= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[9]/span"%i).text
                        firstDNS= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[10]/span"%i).text
                        print("接口名称:",interface_name)
                        print("起始地址:",beginIp)
                        print("结束地址:",endIp)
                        print("子网掩码:",netmask)
                        print("网关地址:",GwAddr_web)
                        print("主DNS服务器:",firstDNS)
                        print()
                        self.assertEqual(interface_name, vlan_lanipname[j], "接口名称 与配置信息不一致")
                        self.assertEqual(beginIp, dhcpStart_vlanip[j], "起始地址 与配置信息不一致")
                        self.assertEqual(endIp, dhcpEnd_vlanip[j], "结束地址 与配置信息不一致")
                        self.assertEqual(netmask, dhcpMask_vlanip[j], "子网掩码 与配置信息不一致")
                        self.assertEqual(GwAddr_web, dhcpGateway_vlanip[j], "网关地址 与配置信息不一致")
                        self.assertEqual(firstDNS, dhcpPriDns_vlanip[j], "主DNS服务器 与配置信息不一致")
                    else:
                        pass
                else:
                    # print("页面无信息！")
                    break
        '''#页面信息输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("Vlan_DHCP_server_config_show")

    def DHCP_delect_vlanvid(self,config_name):
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：", netconfig.text)
        # 内网配置 定位
        lanconfig = self.driver.find_element_by_link_text("内网配置")
        lanconfig.click()
        print("当前位置：", lanconfig.text)
        time.sleep(2)
        # 每页显示  --显示50条
        shownumber = self.driver.find_element_by_xpath(".//button[@id='1']")
        shownumber.click()
        time.sleep(1)
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        time.sleep(1)
        # 在页面查看 配置的vlan id 是否生效
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        print("每页显示个数为:", len(tr))
        # #将配置的vlan 删除
        for j in range(len(config_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name == config_name[j]:
                        # 删除按钮 定位
                        delete = self.driver.find_element_by_xpath(
                            ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span[2]" % i)
                        delete.click()
                        # 确认删除 定位
                        ok = self.driver.find_element_by_id("u-cfm-ok")
                        ok.click()
                        time.sleep(4)
                        print("已将%s -vlan删除" % name)
                        '''#删除后 截图#'''
                        Get_Screenshot(self.driver).get_screenshot("Vlanvid%s_DHCP_server_delete" % (vlan_lanipname[j]))

                    else:
                        pass
                else:
                    break

    def test_03_001_DHCP_server_config(self):
        u'''DHCP服务配置'''
        #进入 DHCP服务配置页面
        self.enter_DHCP()
        #DHCP服务配置 定位
        DHCP_config= self.driver.find_element_by_link_text("DHCP服务配置")
        DHCP_config.click()
        print("当前位置：",DHCP_config.text)
        '''进行DHCP配置'''
        self.DHCP_config()
        print("配置DHCP完成")

    def test_03_002_DHCP_server_show(self):
        u'''将DHCP页面信息输出'''
        #进入 DHCP服务配置页面
        self.enter_DHCP()
        #将DHCP页面信息输出 -- 这个输出没有判断配置信息与页面信息是否一致
        # Output_info(self.driver).output_content(vlan_lanipname)
        '''如何匹配页面信息与配置信息相同--按之前的老方法吗？'''
        self.DHCP_web_config_check_and_show(vlan_lanipname)

    def test_03_003_DHCP_server_validate(self):
        u'''DHCP功能生效判断'''
        '''思路：查看DHCP客户端列表；看是否有主机'''
        #进入 DHCP服务配置页面
        self.enter_DHCP()
        #进入DHCP客户端列表
        DHCP_List = self.driver.find_element_by_link_text("DHCP客户端列表")
        DHCP_List.click()
        ''''''
        pass




    def test_03_004_DHCP_server_delete(self):
        u'''DHCP服务配置删除'''
        #进入 DHCP服务配置页面
        self.enter_DHCP()
        '''删除配置的DHCP'''
        Delect_config(self.driver).delect_sameconfig(vlan_lanipname)
        '''#删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("Vlan_DHCP_server_delete")
        '''删除vlan 接口'''
        self.DHCP_delect_vlanvid(vlan_lanipname)





if __name__ == '__main__':
    unittest.main()
