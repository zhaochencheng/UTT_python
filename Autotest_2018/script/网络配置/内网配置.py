# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 15:05
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : 内网配置.py
# @Software: PyCharm Community Edition
import time
import unittest

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Autotest_2018.public_script.function_public import *


class LAN口配置(unittest.TestCase):
    #class静态参数
    #
    #配置参数获取
    #
    default_ip = get_data("lan_config","default_ip")
    default_netMask= get_data("lan_config","default_netMask")

    lan_ip = get_data("lan_config","lan_ip")
    lan_ip_netMask = get_data("lan_config","lan_ip_netMask")

    vlan_name = get_data("lan_config","vlan_name")
    vlan_ip = get_data("lan_config","vlan_ip")
    vlan_netMask = get_data("lan_config","vlan_netMask")
    vlan_vid = get_data("lan_config","vlan_vid")
    error_style = ['操作失败，系统中存在相同VID的地址池','操作失败，虚接口地址网段重复','实例名称冲突']


    def setUp(self):
        pass
    def tearDown(self):
        pass
    def Lanconfig(self,lanip,lannetmask):
        u"进行lan口 配置"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        # print("当前位置：", netconfig.text)
        # 内网配置 定位
        lanconfig = self.driver.find_element_by_link_text("内网配置")
        lanconfig.click()
        # print("当前位置：", lanconfig.text)
        time.sleep(2)
        # 新增 按钮 定位
        # time.sleep()
        default_edit = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[7]/span[1]")
        default_edit.click()
        time.sleep(1)
        # 名称
        save1 = webwait.until(lambda x: x.find_element_by_id("save"))
        # IP 地址
        dhcpStart = self.driver.find_element_by_xpath(".//input[@name ='dhcpStart']")
        dhcpStart.clear()
        dhcpStart.send_keys(lanip)
        #子网掩码
        dhcpMask =self.driver.find_element_by_xpath(".//input[@name = 'dhcpMask']")
        dhcpMask.clear()
        dhcpMask.send_keys(lannetmask)
        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(22)
        print(self.driver.current_url)


    def test_01_LAN口配置(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        # 配置vlan
        #
        self.Lanconfig(self.lan_ip,self.lan_ip_netMask)
        time.sleep(2)
        self.driver.quit()

    def test_02_LAN口验证(self):
        # 登陆web页面
        self.driver = Login_web(URL="http://%s"%self.lan_ip)
        print('登陆URL为：',self.driver.current_url)
        #
        # 验证修改lan口是否生效
        #
        self.assertIn(self.lan_ip,self.driver.current_url,'lan口配置失败')
        #
        #将lan口该为默认配置 default ip
        #
        self.Lanconfig(self.default_ip,self.default_netMask)
        print("将lan口该为默认配置--Lan口为：",self.default_ip)
        time.sleep(2)
        self.driver.quit()

    def vlanconfig(self):
        u"进行vlan 配置"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        # print("当前位置：", netconfig.text)
        # 内网配置 定位
        lanconfig = self.driver.find_element_by_link_text("内网配置")
        lanconfig.click()
        # print("当前位置：", lanconfig.text)
        time.sleep(2)
        # 新增 按钮 定位
        # time.sleep()
        add = self.driver.find_element_by_id("add")
        add.click()
        # 名称
        lanipname = webwait.until(lambda x: x.find_element_by_xpath(".//input[@name ='lanIpName']"))
        lanipname.send_keys(self.vlan_name)
        time.sleep(1)
        # IP 地址
        lanIP = self.driver.find_element_by_xpath(".//input[@name ='lanIp']")
        lanIP.clear()
        lanIP.send_keys(self.vlan_ip)
        lanNetmask =self.driver.find_element_by_xpath(".//input[@name = 'lanNetmask']")
        lanNetmask.clear()
        lanNetmask.send_keys(self.vlan_netMask)
        # 生效 接口  --选择vlan id
        vlanID = self.driver.find_element_by_xpath(".//select[@name = 'sxjk']")
        Select(vlanID).select_by_value("vlanid")
        # vlan id 输入框定位
        DHCPvid = webwait.until(lambda x: x.find_element_by_xpath(".//input[@name ='dhcpVid']"))
        DHCPvid.send_keys(self.vlan_vid)
        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        try:
            pageTip_warn= self.driver.find_element_by_xpath("/html/body/div[4]")
            if pageTip_warn.is_displayed():
                time.sleep(1)
                pageTip_warn1 = self.driver.find_element_by_xpath("/html/body/div[4]/p")
                if pageTip_warn1.text in self.error_style:
                    print(pageTip_warn1.text)
                    # 点击关闭
                    time.sleep(3)
                    close = self.driver.find_element_by_id("modal-hide")
                    close.click()
                    time.sleep(2)
                else:
                    print("vlan配置完成;")
            else:
                print("vlan配置完成;")
                time.sleep(2)
        except BaseException as E:
            pass
        time.sleep(4)
    def config_check(self):
        head_all = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th")
        # print("标题子项：", len(head_all))
        #  #展开
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            # print('len(td):',len(td))
            if len(td) > 1:
                # 页面 名称
                name = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                # 页面 IP地址
                ip = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                # 页面 子网掩码
                netmask = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                #页面 VLAN ID
                VLAN_ID = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span"% i).text
                if name == self.vlan_name:
                    print("名称：",name)
                    print("IP地址：",ip)
                    print("子网掩码:",netmask)
                    print("VLAN ID:",VLAN_ID)
                    self.assertEqual(ip,self.vlan_ip,'ip 与配置文件不一致')
                    self.assertEqual(netmask,self.vlan_netMask,'netmask 与配置文件不一致')
                    self.assertEqual(VLAN_ID,self.vlan_vid,'VLAN_ID 与配置文件不一致')
                else:
                    pass
            else:
                # print("没有与配置文件%s一致的页面信息" % self.vlan_name)
                break
        return len(td)


    def test_03_LAN_VLAN配置(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        #配置vlan
        #
        self.vlanconfig()

        #
        # 判断页面信息是否与配置文件信息一致
        #
        self.config_check()

        time.sleep(2)
        self.driver.quit()

    def test_04_LAN_VLAN验证(self):
        pass

if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(LAN口配置("test_01_LAN口配置"))
    suit.addTest(LAN口配置("test_02_LAN口验证"))
    suit.addTest(LAN口配置("test_03_LAN_VLAN配置"))
    suit.addTest(LAN口配置("test_04_LAN_VLAN验证"))
    runner = unittest.TextTestRunner()
    runner.run(suit)