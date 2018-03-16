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
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class Port_mapping(unittest.TestCase):
    u'''**端口映射**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)
    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def enter_port_map(self):
        "页面操作：网络配置--端口映射"
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
    def del_static_port_sameconfig(self):
        u'先匹配页面是否与配置相同的配置文件，若有，则删除'
        # 每页显示  --显示50条
        shownumber = self.driver.find_element_by_xpath(".//button[@id='1']")
        shownumber.click()
        time.sleep(1)
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        time.sleep(1)
        # 判断页面是否存在与配置 相同的配置
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
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
                        print("有%s 规则，先将其删除\n" % name_rule,"*" * 30, '\n')
                    else:
                        pass
                else:
                    break
    def show_static_port_config(self):
        u'''将配置的信息输出'''
        # 每页显示  --显示50条
        shownumber = self.driver.find_element_by_xpath(".//button[@id='1']")
        shownumber.click()
        time.sleep(1)
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        time.sleep(1)
        # 在页面查看 配置的 静态映射 是否生效
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        print("每页显示个数为:", len(tr))
        print("*" * 30, '\n')
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

    def test_04_001_static_port_mapping_config(self):
        u'''静态映射配置'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #进入端口映射页面
        self.enter_port_map()
        time.sleep(1)
        #点击静态映射
        static_mapping = self.driver.find_element_by_link_text("静态映射")
        print("当前位置：",static_mapping.text)


        '''#先匹配页面是否与配置相同的配置文件，若有，则删除'''
        self.del_static_port_sameconfig()
        '''#配置 静态映射'''
        for j in  range(len(new_rulename)):
            '''#配置前先 截图#'''
            Get_Screenshot(self.driver).get_screenshot("%s_static_port_mapping_configure_before" % (new_rulename[j]))

            # 新增 按钮 定位
            add = self.driver.find_element_by_id("add")
            add.click()
            time.sleep(1)
            #规则名称 定位
            rulename = webwait.until(lambda x: x.find_element_by_xpath(".//input[@name='IDs']"))
            rulename.send_keys(new_rulename[j])
            #绑定几口 定位
            bindinterface = self.driver.find_element_by_xpath(".//select[@name='NatBinds']")
            Select(bindinterface).select_by_value("WAN1") #选择wan1口
            # Select(bindinterface).select_by_index(0)
            #内网地址 定位
            inaddress = self.driver.find_element_by_xpath(".//input[@name='IPs']")
            inaddress.clear()
            inaddress.send_keys(inaddr[j])
            #内网端口 定位
            inport_left = self.driver.find_element_by_xpath(".//input[@name = 'inS']")
            inport_left.clear()
            inport_left.send_keys(inport[j])
            inport_right = self.driver.find_element_by_xpath(".//input[@name = 'inE']")
            inport_right.clear()
            inport_right.send_keys(inport[j])
            #外部端口 定位
            outport_left = self.driver.find_element_by_xpath(".//input[@name = 'outS']")
            outport_left.clear()
            outport_left.send_keys(outport[j])
            outport_right = self.driver.find_element_by_xpath(".//input[@name = 'outE']")
            outport_right.clear()
            outport_right.send_keys(outport[j])
            time.sleep(1)
            #保存 定位
            save = self.driver.find_element_by_id("save")
            save.click()
            time.sleep(4)
            '''#配置完成 截图#'''
            Get_Screenshot(self.driver).get_screenshot("%s_static_port_mapping_configure_after" % (new_rulename[j]))
        #

        # # #将配置好的页面截图
        #
        #
        # #将配置的 静态映射 删除
        time.sleep(2)
        print("*" * 30, '\n')
    def test_04_002_static_port_mapping_show(self):
        u'''静态映射配置-页面信息正确 '''
        #进入端口映射页面
        self.enter_port_map()
        # 点击静态映射
        static_mapping = self.driver.find_element_by_link_text("静态映射")
        print("当前位置：", static_mapping.text)
        #输出 配置信息
        self.show_static_port_config()
        '''# 输出 截图#'''
        Get_Screenshot(self.driver).get_screenshot("_static_port_mapping_configure_show")
    def test_04_003_static_port_mapping_validate(self):
        u'''对配置静态端口映射 进行验证'''
        '''
        再此处实现对配置 静态映射 的验证方式
        '''
        pass
    def test_04_004_static_port_mapping_delect(self):
        u'''静态映射删除 '''

        # 进入端口映射页面
        self.enter_port_map()
        # 点击静态映射
        static_mapping = self.driver.find_element_by_link_text("静态映射")
        print("当前位置：", static_mapping.text)
        #删除配置
        self.del_static_port_sameconfig()
        '''# 删除配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("_static_port_mapping_configure_delect")

    def enter_nat_rule(self):
        u'''进入 nat规则 页面'''

        #进入 端口映射页面
        self.enter_port_map()
        #进入 nat规则 页面
        nat_rule = self.driver.find_element_by_link_text("NAT规则")
        print("当前位置:",nat_rule.text)
        nat_rule.click()
        time.sleep(3)
    def del_nat_rule_sameconfig(self):
        u'''删除相同配置'''
        webwait = WebDriverWait(self.driver, 10, 1)
        # 每页显示  --显示50条
        shownumbers = self.driver.find_elements_by_xpath(".//button[@id='1']")
        shownumber = shownumbers[1]
        shownumber.click()
        time.sleep(1)
        numbers_50 = self.driver.find_elements_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50 = numbers_50[1]
        number_50.click()
        time.sleep(1)
        # 在页面查看 配置的 静态映射 是否生效
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        print("每页显示个数为:", len(tr))
        print("*" * 30, '\n')
        time.sleep(2)
        # 判断是否已存在配置文件中的 配置 若有 则删除；
        for j in range(len(NAT_rulename)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == NAT_rulename[j]:
                        delete = self.driver.find_element_by_xpath(
                            ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]" % i)
                        delete.click()
                        # time.sleep(2)
                        ok = webwait.until(lambda x: x.find_element_by_id("u-cfm-ok"))
                        # ok = self.driver.find_element_by_id("u-cfm-ok")
                        ok.click()
                        time.sleep(4)
                        print("有%s 规则，先将其删除" % name_rule)

                    else:
                        pass
                else:
                    break
    def nat_rule_show(self):
        '''判断配置的静态映射 是否生效 并将其输出'''
        webwait = WebDriverWait(self.driver, 10, 1)
        # 每页显示  --显示50条
        shownumbers = self.driver.find_elements_by_xpath(".//button[@id='1']")
        shownumber = shownumbers[1]
        shownumber.click()
        time.sleep(1)
        numbers_50 = self.driver.find_elements_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50 = numbers_50[1]
        number_50.click()
        time.sleep(1)
        # 在页面查看 配置的 静态映射 是否生效
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        print("每页显示个数为:", len(tr))
        print("*" * 30, '\n')
        time.sleep(2)
        # 判断配置的静态映射 是否生效 并将其输出;
        for j in range(len(NAT_rulename)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver.find_elements_by_xpath(
                    ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == NAT_rulename[j]:
                        ipaddr = self.driver.find_element_by_xpath(
                            ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                        self.assertEqual(ipaddr, inaddr_begin[j], "配置 内网起始IP地址 与页面生效ip不一致")
                        nat_type = self.driver.find_element_by_xpath(
                            ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                        ipaddrend = self.driver.find_element_by_xpath(
                            ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                        self.assertEqual(ipaddrend, inaddr_end[j], "配置 内网结束IP地址 与页面生效ip不一致")
                        interface = self.driver.find_element_by_xpath(
                            ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % i).text

                        print("规则名称:", name_rule, " 	NAT类型:", nat_type, "  内网起始IP地址:", ipaddr,
                              " 内网结束IP地址:", ipaddrend, "   绑定接口:", interface)
                    else:
                        pass
                else:
                    break


    def test_04_006_nat_rule_config_EasyIP(self):
        u'''NAT规则EasyIP 配置'''
        #进入NAT规则页面
        self.enter_nat_rule()
        '''配置前 先核对 页面是否有配置文件相同的信息；若有则删除'''
        self.del_nat_rule_sameconfig()
        '''开始配置 NAT规则-EasyIP'''
        for j in range(len(NAT_rulename)):
            '''# 配置前 截图#'''
            Get_Screenshot(self.driver).get_screenshot("%s_nat_rule_configure_EasyIP_before"%(NAT_rulename[j]))
           # 新增 按钮 定位
            time.sleep(1)
            adds = self.driver.find_elements_by_id("add")
            add = adds[1]
            add.click()
            time.sleep(1)
            # 规则名称
            rule_name = self.driver.find_element_by_xpath(".//input[@name='RuleIDs']")
            rule_name.clear()
            rule_name.send_keys(NAT_rulename[j])
            # 绑定接口  --- 绑定wan口
            bindinterface = self.driver.find_element_by_xpath(".//select[@name='Binds']")
            Select(bindinterface).select_by_value("WAN1")
            # Select(bindinterface).select_by_index(0)
            # nat 类型
            # # Easy IP 定位
            Easyip = self.driver.find_element_by_xpath(".//input[@name='NatTypes' and @value='1']")
            Easyip.click()
            time.sleep(1)
            span = self.driver.find_element_by_xpath(
                "//*[@id='modal-add']/div/div/div[2]/table/tbody/tr[4]/td[2]/span[1]")
            if Easyip.is_selected():
                print("%s 定位成功！！" % (span.text))
            else:
                print("%s 定位失败！！" % (span.text))
            # # One2One 定位
            # One2One = self.driver.find_element_by_xpath(".//input[@name='NatTypes' and @value='2']")
            # One2One.click()
            # 内网起始IP地址 定位
            inaddrbegin = self.driver.find_element_by_xpath(".//input[@name='InFromIPs']")
            inaddrbegin.clear()
            inaddrbegin.send_keys(inaddr_begin[j])
            # 内网结束IP地址 定位
            inaddrend = self.driver.find_element_by_xpath(".//input[@name ='InEndIPs']")
            inaddrend.clear()
            inaddrend.send_keys(inaddr_end[j])
            # 外网IP地址
            out_addr = self.driver.find_element_by_xpath(".//input[@name = 'OutIPs']")
            out_addr.clear()
            out_addr.send_keys(outaddr[j])
            # 保存  定位
            save = self.driver.find_element_by_id("save")
            save.click()

            time.sleep(4)
            '''# 配置完成 截图#'''
            Get_Screenshot(self.driver).get_screenshot("%s_nat_rule_configure_EasyIP_after" % (NAT_rulename[j]))
        time.sleep(2)
        print("*" * 30, '\n')
    def test_04_007_nat_rule_show_EasyIP(self):
        u"EasyIP配置-页面信息正确"
        self.enter_nat_rule()
        #将信息输出
        self.nat_rule_show()
        '''# 输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("nat_rule_configure_show_EasyIP")
    def test_04_008_nat_rule_EasyIP_validate(self):
        u"验证EasyIP功能生效"
        pass
    def test_04_009_nat_rule_del_EasyIP(self):
        u"将配置的EasyIP 信息删除"
        self.enter_nat_rule()
        #删除EasyIP 信息
        self.del_nat_rule_sameconfig()
        '''# 删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("nat_rule_configure_delete_EasyIP")


    # def test_04_003_DMZ(self):
        #     u'''DMZ主机配置'''
        #
        #     # 显示等待
        #     webwait = WebDriverWait(self.driver, 10, 1)
        #     # 网络配置  定位
        #     netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        #     netconfig.click()
        #     print("当前位置：", netconfig.text)
        #     # 端口映射 定位
        #     port_map = self.driver.find_element_by_link_text("端口映射")
        #     port_map.click()
        #     print("当前位置:", port_map.text)
        #     time.sleep(2)
        #
        #     #DMZ主机 定位
        #     DMZ = self.driver.find_element_by_link_text("DMZ主机")
        #     print("当前定位：",DMZ.text)
        #     DMZ.click()
        #     time.sleep(2)
        #     #DMZ状态 定位
        #     open_DMZ = self.driver.find_element_by_xpath(".//input[@name = 'DMZEnable' and @value='on']")
        #     if open_DMZ.is_selected():
        #         print("已开启DMZ！")
        #     else:
        #         open_DMZ.click()
        #         print("现在开启DMZ！")
        #     time.sleep(3)
        #     # 全局DMZ主机 定位
        #     globalDMZ = self.driver.find_element_by_xpath(".//input[@name='GlobalDMZ']")
        #     globalDMZ.clear()
        #     globalDMZ.send_keys(globalDMZHost)
        #     #保存 定位
        #     save = self.driver.find_element_by_id('save')
        #     save.click()
        #     time.sleep(2)
        #     #判断全局DMZ主机 在页面 是否生效
        #     for i in range(1,5):
        #         wan_DMZ = self.driver.find_element_by_xpath(".//input[@name='WAN%iDMZ']"%i)
        #         if wan_DMZ.is_displayed():
        #             print("wan%d口DMZ主机ip为："%i,wan_DMZ.get_attribute("value"))
        #             self.assertEqual(wan_DMZ.get_attribute("value"), globalDMZHost, "全局DMZ主机ip和wan1口DMZ主机IP不一致")
        #     print("各wan口配置ip与全局DMZ主机ip相同")
        #
        #     #添加DMZ 生效 方法
        #
        #     #单个wan口DMZ 配置

    def test_04_011_nat_rule_config_One2One(self):
        u'''NAT规则 One2One配置'''
        # 进入NAT规则页面
        self.enter_nat_rule()
        '''配置前 先核对 页面是否有配置文件相同的信息；若有则删除'''
        self.del_nat_rule_sameconfig()
        '''开始配置 NAT规则-One2One'''

        for j in range(len(NAT_rulename)):
            '''# 配置前 截图#'''
            Get_Screenshot(self.driver).get_screenshot("%s_nat_rule_configure_One2One_before"%(NAT_rulename[j]))
           # 新增 按钮 定位
            time.sleep(1)
            adds = self.driver.find_elements_by_id("add")
            add = adds[1]
            add.click()
            time.sleep(1)
            # 规则名称
            rule_name = self.driver.find_element_by_xpath(".//input[@name='RuleIDs']")
            rule_name.clear()
            rule_name.send_keys(NAT_rulename[j])
            # 绑定接口  --- 绑定wan口
            bindinterface = self.driver.find_element_by_xpath(".//select[@name='Binds']")
            Select(bindinterface).select_by_value("WAN1")
            # Select(bindinterface).select_by_index(0)
            # nat 类型
            # One2One 定位
            One2One = self.driver.find_element_by_xpath(".//input[@name='NatTypes' and @value='2']")
            One2One.click()
            time.sleep(1)
            span = self.driver.find_element_by_xpath(
                "//*[@id='modal-add']/div/div/div[2]/table/tbody/tr[4]/td[2]/span[1]")
            if One2One.is_selected():
                print("%s 定位成功！！" % (span.text))
            else:
                print("%s 定位失败！！" % (span.text))
            # # One2One 定位
            # One2One = self.driver.find_element_by_xpath(".//input[@name='NatTypes' and @value='2']")
            # One2One.click()
            # 内网起始IP地址 定位
            inaddrbegin = self.driver.find_element_by_xpath(".//input[@name='InFromIPs']")
            inaddrbegin.clear()
            inaddrbegin.send_keys(inaddr_begin[j])
            # 内网结束IP地址 定位
            inaddrend = self.driver.find_element_by_xpath(".//input[@name ='InEndIPs']")
            inaddrend.clear()
            inaddrend.send_keys(inaddr_end[j])
            # 外网IP地址
            out_addr = self.driver.find_element_by_xpath(".//input[@name = 'OutIPs']")
            out_addr.clear()
            out_addr.send_keys(outaddr[j])
            # 保存  定位
            save = self.driver.find_element_by_id("save")
            save.click()

            time.sleep(4)
            '''# 配置完成 截图#'''
            Get_Screenshot(self.driver).get_screenshot("%s_nat_rule_configure_One2One_after" % (NAT_rulename[j]))
        time.sleep(2)
        print("*" * 30, '\n')
    def test_04_012_nat_rule_show_One2One(self):
        u"One2One配置-页面信息正确"
        self.enter_nat_rule()
        #将信息输出
        self.nat_rule_show()
        '''# 输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("nat_rule_configure_show_One2One")
    def test_04_013_nat_rule_One2One_validate(self):
        u"验证One2One配置功能生效"
        pass
    def test_04_014_nat_rule_del_One2One(self):
        u"将One2One配置 信息删除"
        self.enter_nat_rule()
        #删除One2One配置 信息
        self.del_nat_rule_sameconfig()
        '''# 删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("nat_rule_configure_delete_One2One")


    def test_04_016_DMZ(self):
            u'''DMZ主机配置'''

            # 显示等待
            webwait = WebDriverWait(self.driver, 10, 1)
            # 网络配置  定位
            netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
            netconfig.click()
            print("当前位置：", netconfig.text)
            # 端口映射 定位
            port_map = self.driver.find_element_by_link_text("端口映射")
            port_map.click()
            print("当前位置:", port_map.text)
            time.sleep(2)

            #DMZ主机 定位
            DMZ = self.driver.find_element_by_link_text("DMZ主机")
            print("当前定位：",DMZ.text)
            DMZ.click()
            time.sleep(2)
            #DMZ状态 定位
            open_DMZ = self.driver.find_element_by_xpath(".//input[@name = 'DMZEnable' and @value='on']")
            if open_DMZ.is_selected():
                print("已开启DMZ！")
            else:
                open_DMZ.click()
                print("现在开启DMZ！")
            time.sleep(3)
            # 全局DMZ主机 定位
            globalDMZ = self.driver.find_element_by_xpath(".//input[@name='GlobalDMZ']")
            globalDMZ.clear()
            globalDMZ.send_keys(globalDMZHost)
            #保存 定位
            save = self.driver.find_element_by_id('save')
            save.click()
            time.sleep(2)
            #判断全局DMZ主机 在页面 是否生效
            for i in range(1,5):
                wan_DMZ = self.driver.find_element_by_xpath(".//input[@name='WAN%iDMZ']"%i)
                if wan_DMZ.is_displayed():
                    print("wan%d口DMZ主机ip为："%i,wan_DMZ.get_attribute("value"))
                    self.assertEqual(wan_DMZ.get_attribute("value"), globalDMZHost, "全局DMZ主机ip和wan1口DMZ主机IP不一致")
            print("各wan口配置ip与全局DMZ主机ip相同")

            #添加DMZ 生效 方法

            #单个wan口DMZ 配置







if __name__ == '__main__':
    unittest.main()