# -*- coding: utf-8 -*-
# @Time    : 2018/1/22 19:06
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_Lan_config.py
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

class Lan_config(unittest.TestCase):
    u'''**Lan口配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def enter_Lanconfig(self):
        u"进行以下操作：点击网络配置---内网配置"
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

    # def test_02_001_lanconfig(self):
    #     u'''lan口默认配置'''
    #     #显示等待
    #     webwait = WebDriverWait(self.driver,10,1)
    #     # 网络配置  定位
    #     netconfig = webwait.until(lambda x :x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
    #     netconfig.click()
    #     print("当前位置：", netconfig.text)
    #     #内网配置 定位
    #     lanconfig = self.driver.find_element_by_link_text("内网配置")
    #     lanconfig.click()
    #     print("当前位置：",lanconfig.text)

    def test_02_002_vlan_Lan_configure(self):
        u'''vlan配置'''
        # 进入内网配置页面
        self.enter_Lanconfig()
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)

        for i in range(len(vlan_lanipname)):
            '''#配置前先 截图#'''
            Get_Screenshot(self.driver).get_screenshot("Vlan%s_Lan_configure_before" % (vlan_lanipname[i]))

            #新增 按钮 定位
            # time.sleep()
            add = self.driver.find_element_by_id("add")
            add.click()
            # add = webwait.until(lambda x : x.find_element_by_id("add"))
            # add.click()
            # time.sleep(2)
            #名称
            lanipname = webwait.until(lambda x: x.find_element_by_xpath(".//input[@name ='lanIpName']"))
            lanipname.send_keys(vlan_lanipname[i])
            time.sleep(1)
            #IP 地址
            lanIP = self.driver.find_element_by_xpath(".//input[@name ='lanIp']")
            lanIP.clear()
            lanIP.send_keys(vlan_ip[i])
            #生效 接口  --选择vlan id
            vlanID = self.driver.find_element_by_xpath(".//select[@name = 'sxjk']")
            Select(vlanID).select_by_value("vlanid")
            #vlan id 输入框定位
            DHCPvid = webwait.until(lambda x: x.find_element_by_xpath(".//input[@name ='dhcpVid']"))
            DHCPvid.send_keys(vlan_id[i])
            #保存 定位
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(4)
            '''#配置前先 截图#'''
            Get_Screenshot(self.driver).get_screenshot("Vlan%s_Lan_configure_after" % (vlan_lanipname[i]))
        time.sleep(1)
        # # '''显示配置的vlan Lan'''
        # #每页显示  --显示50条
        # shownumber = self.driver.find_element_by_xpath(".//button[@id='1']")
        # shownumber.click()
        # time.sleep(1)
        # number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        # number_50.click()
        # time.sleep(1)
        # #在页面查看 配置的vlan id 是否生效
        # tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:",len(tr))
        # # # 判断配置的vlan 是否生效 并将其输出;
        # for j in range(len(vlan_lanipname)):
        #     for i in range(1,len(tr)+1):
        #         #tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
        #         td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td"%i)
        #         if len(td)>1:
        #             name = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span"%i).text
        #             if name == vlan_lanipname[j]:
        #                 ipaddr = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span"%i).text
        #                 self.assertEqual(ipaddr,vlan_ip[j],"配置IP与页面生效ip不一致")
        #                 vid = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span"%i).text
        #                 self.assertEqual(vid,vlan_id[j],"配置vlan id 与页面生效vlan id不一致")
        #                 print("名称:",name,"   IP地址:",ipaddr,"   vlan id:",vid)
        #             else:
        #                 pass
        #         else:
        #             break
        # #将配置的vlan 删除
        # for j in range(len(vlan_lanipname)):
        #     for i in range(1,len(tr)+1):
        #         #tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
        #         td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td"%i)
        #         if len(td)>1:
        #             name = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span"%i).text
        #             if name == vlan_lanipname[j]:
        #                 #删除按钮 定位
        #                 delete = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span[2]"%i)
        #                 delete.click()
        #                 # 确认删除 定位
        #                 ok = self.driver.find_element_by_id("u-cfm-ok")
        #                 ok.click()
        #                 time.sleep(4)
        #                 print("已将%s -vlan删除"%name)
        #
        #             else:
        #                 pass
        #         else:
        #             break

    def test_02_003_vlan_Lan_web_show(self):
        u"将页面配置的vlan lan输出 并比较页面显示与配置是否一致 "
        #进入内网配置页面
        self.enter_Lanconfig()
        '''显示配置的vlan Lan'''
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
        # # 判断配置的vlan 页面是否生效 并将其输出;
        for j in range(len(vlan_lanipname)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name == vlan_lanipname[j]:
                        ipaddr = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text

                        '''断言判断 页面信息与配置信息是否相同'''
                        try:
                            self.assertEqual(ipaddr, vlan_ip[j], "配置IP与页面生效ip不一致")
                        except BaseException as E:
                            '''#错误截图 截图#'''
                            Get_Screenshot(self.driver).get_screenshot("Vlan%s_Lan_configure_error_%s" % (vlan_lanipname[j],"配置IP与页面生效ip不一致"))
                            raise
                        '''断言判断 页面信息与配置信息是否相同'''
                        vid = self.driver.find_element_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                        try:
                            self.assertEqual(vid, vlan_id[j], "配置vlan id 与页面生效vlan id不一致")
                        except BaseException as E:
                            Get_Screenshot(self.driver).get_screenshot("Vlan%s_Lan_configure_error_%s" % (vlan_lanipname[j],"配置vlan id 与页面生效vlan id不一致"))

                        print("名称:", name, "   IP地址:", ipaddr, "   vlan id:", vid)
                    else:
                        pass
                else:
                    break

    def test_02_004_vlan_Lan_dele_config(self):
        u"将配置的vlan lan 删除"
        # 进入内网配置页面
        self.enter_Lanconfig()

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
        for j in range(len(vlan_lanipname)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name == vlan_lanipname[j]:
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
                        Get_Screenshot(self.driver).get_screenshot("Vlan%s_Lan_configure_delete" % (vlan_lanipname[j]))

                    else:
                        pass
                else:
                    break


if __name__ == '__main__':
    unittest.main()