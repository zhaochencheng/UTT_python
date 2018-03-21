# -*- coding: utf-8 -*-
# @Time    : 2018/3/21 11:24
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : NAT规则.py
# @Software: PyCharm Community Edition
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Autotest_2018.public_script.Get_screenshot import Get_Screenshot
from Autotest_2018.public_script.function_public import *

class NAT规则_EasyIP(unittest.TestCase):
    # class静态参数
    #
    # 配置参数获取
    #
    EasyIP_name = get_data("nat_EasyIP", "EasyIP_name")
    EasyIP_interface = get_data("nat_EasyIP", "EasyIP_interface")
    EasyIP_beginip = get_data("nat_EasyIP", "EasyIP_beginip")
    EasyIP_endip = get_data("nat_EasyIP", "EasyIP_endip")
    EasyIP_outIP = get_data("nat_EasyIP", "EasyIP_outIP")
    EasyIP_type = get_data("nat_EasyIP", "EasyIP_type")
    error_style = ['规则名重复','外部IP地址段重叠']

    def setUp(self):
        pass
    def tearDown(self):
        pass

    def NAT_rule_config_EasyIP(self):
        # 配置nat规则----EasyIP
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
        time.sleep(1)
        # 进入 nat规则 页面
        nat_rule = self.driver.find_element_by_link_text("NAT规则")
        print("当前位置:", nat_rule.text)
        nat_rule.click()
        time.sleep(3)
        # 新增 按钮 定位
        adds = self.driver.find_elements_by_id("add")
        add = adds[1]
        add.click()
        time.sleep(1)
        # 规则名称
        rule_name = self.driver.find_element_by_xpath(".//input[@name='RuleIDs']")
        rule_name.clear()
        rule_name.send_keys(self.EasyIP_name)
        # 绑定接口  --- 绑定wan口
        bindinterface = self.driver.find_element_by_xpath(".//select[@name='Binds']")
        Select(bindinterface).select_by_visible_text(self.EasyIP_interface)
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
        inaddrbegin.send_keys(self.EasyIP_beginip)
        # 内网结束IP地址 定位
        inaddrend = self.driver.find_element_by_xpath(".//input[@name ='InEndIPs']")
        inaddrend.clear()
        inaddrend.send_keys(self.EasyIP_endip)
        # 外网IP地址
        out_addr = self.driver.find_element_by_xpath(".//input[@name = 'OutIPs']")
        out_addr.clear()
        out_addr.send_keys(self.EasyIP_outIP)
        # 保存  定位
        save = self.driver.find_element_by_id("save")
        save.click()
        try:
            msg_grpExist = self.driver.find_element_by_xpath("/html/body/div[4]")
            if msg_grpExist.is_displayed():
                time.sleep(1)
                msg_grpExistp = self.driver.find_element_by_xpath("/html/body/div[4]/p")
                if msg_grpExistp.text in self.error_style:
                    print(msg_grpExistp.text)
                    # 点击关闭
                    time.sleep(3)
                    close = self.driver.find_element_by_id("modal-hide")
                    close.click()
                    time.sleep(2)
                else:
                    print("动态域名配置完成;")
            else:
                time.sleep(2)
        except BaseException as E:
            pass
        time.sleep(2)
        print("EasyIP配置完成！")
    def check_web_NAT_rule_EasyIP(self,config_name):
        head_all = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/thead/tr/th")
        # print("标题子项：", len(head_all))
        #  #展开
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            # print('len(td):',len(td))
            if len(td) > 1:
                # 页面 	规则名称
                rulename = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                # 页面 NAT类型
                NATType = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                # 页面 内网起始IP地址
                IPinFRROM= self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                # 页面 内网结束IP地址
                IPoutTo = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                # 页面 外网起始IP地址
                outStartIP = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % i).text
                # 页面 	绑定接口
                bindInterface = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % i).text
                if rulename == config_name:
                    print("规则名称：", rulename)
                    print("NAT类型：", NATType)
                    print("内网起始IP地址:", IPinFRROM)
                    print("内网结束IP地址:", IPoutTo)
                    print("外网起始IP地址:", outStartIP)
                    print("绑定接口:", bindInterface)
                    print("NAT规则---EasyIP 页面信息输出完成！")
                    self.assertEqual(rulename, self.EasyIP_name, '规则名称 与配置文件不一致')
                    self.assertEqual(NATType, self.EasyIP_type, 'NAT类型 与配置文件不一致')
                    self.assertEqual(IPinFRROM, self.EasyIP_beginip, '内网起始IP地址 与配置文件不一致')
                    self.assertEqual(IPoutTo, self.EasyIP_endip, '内网结束IP地址 与配置文件不一致')
                    self.assertEqual(outStartIP, self.EasyIP_outIP, '外网起始IP地址 与配置文件不一致')
                    self.assertEqual(bindInterface, self.EasyIP_interface, '绑定接口 与配置文件不一致')
                else:
                    pass
            else:
                # print("没有与配置文件%s一致的页面信息" % self.vlan_name)
                break
        return len(td)

    def del_nat_rule_sameconfig(self):
        u'''删除相同配置'''
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：", netconfig.text)
        # 端口映射 定位
        port_map = self.driver.find_element_by_link_text("端口映射")
        port_map.click()
        print("当前位置:", port_map.text)
        time.sleep(1)
        # 进入 nat规则 页面
        nat_rule = self.driver.find_element_by_link_text("NAT规则")
        print("当前位置:", nat_rule.text)
        nat_rule.click()
        time.sleep(3)
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        print("每页显示个数为:", len(tr))
        print("*" * 30, '\n')
        time.sleep(2)
        # 判断是否已存在配置文件中的 配置 若有 则删除；
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                name_rule = self.driver.find_element_by_xpath(
                    ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                if name_rule == self.EasyIP_name:
                    delete = self.driver.find_element_by_xpath(
                        ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]" % i)
                    delete.click()
                    # time.sleep(2)
                    ok = webwait.until(lambda x: x.find_element_by_id("u-cfm-ok"))
                    # ok = self.driver.find_element_by_id("u-cfm-ok")
                    ok.click()
                    time.sleep(4)
                    print("有%s 规则，将其删除" % name_rule)

                else:
                    # print("页面无%s 规则删除" % self.EasyIP_name)
                    pass
            else:
                # print("页面无%s 规则删除" % self.EasyIP_name)
                break



    def test_NAT_EasyIP规则配置(self):
        #  登陆web页面
        self.driver = Login_web()
        #
        #NAT规则---EasyIP配置
        #
        self.NAT_rule_config_EasyIP()
        #
        #判断页面显示信息 与 配置信息 是否一致
        #
        self.check_web_NAT_rule_EasyIP(self.EasyIP_name)
        time.sleep(2)
        self.driver.quit()

    def test_NAT_EasyIP规则验证(self):
        pass

    def test_NAT_EasyIP规则删除(self):
        #  登陆web页面
        self.driver = Login_web()
        # 删除配置
        self.del_nat_rule_sameconfig()

class NAT规则_One2One(unittest.TestCase):
    # class静态参数
    #
    # 配置参数获取
    #
    One2One_name = get_data("nat_One2One", "One2One_name")
    One2One_interface = get_data("nat_One2One", "One2One_interface")
    One2One_beginip = get_data("nat_One2One", "One2One_beginip")
    One2One_endip= get_data("nat_One2One", "One2One_endip")
    One2One_outIP = get_data("nat_One2One", "One2One_outIP")
    One2One_type = get_data("nat_One2One", "One2One_type")
    error_style = ['规则名重复', '外部IP地址段重叠']


    def setUp(self):
        pass
    def tearDown(self):
        pass
    def NAT_rule_config_One2One(self):
        # 配置nat规则----One2One
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
        time.sleep(1)
        # 进入 nat规则 页面
        nat_rule = self.driver.find_element_by_link_text("NAT规则")
        print("当前位置:", nat_rule.text)
        nat_rule.click()
        time.sleep(3)
        # 新增 按钮 定位
        adds = self.driver.find_elements_by_id("add")
        add = adds[1]
        add.click()
        time.sleep(1)
        # 规则名称
        rule_name = self.driver.find_element_by_xpath(".//input[@name='RuleIDs']")
        rule_name.clear()
        rule_name.send_keys(self.One2One_name)
        # 绑定接口  --- 绑定wan口
        bindinterface = self.driver.find_element_by_xpath(".//select[@name='Binds']")
        Select(bindinterface).select_by_visible_text(self.One2One_interface)
        # Select(bindinterface).select_by_index(0)
        # nat 类型
        # # Easy IP 定位
        # # One2One 定位
        One2One = self.driver.find_element_by_xpath(".//input[@name='NatTypes' and @value='2']")
        One2One.click()
        time.sleep(1)
        span = self.driver.find_element_by_xpath(
            "//*[@id='modal-add']/div/div/div[2]/table/tbody/tr[4]/td[2]/span[2]")
        if One2One.is_selected():
            print("%s 定位成功！！" % (span.text))
        else:
            print("%s 定位失败！！" % (span.text))
        # 内网起始IP地址 定位
        inaddrbegin = self.driver.find_element_by_xpath(".//input[@name='InFromIPs']")
        inaddrbegin.clear()
        inaddrbegin.send_keys(self.One2One_beginip)
        # 内网结束IP地址 定位
        inaddrend = self.driver.find_element_by_xpath(".//input[@name ='InEndIPs']")
        inaddrend.clear()
        inaddrend.send_keys(self.One2One_endip)
        # 外网IP地址
        out_addr = self.driver.find_element_by_xpath(".//input[@name = 'OutIPs']")
        out_addr.clear()
        out_addr.send_keys(self.One2One_outIP)
        # 保存  定位
        save = self.driver.find_element_by_id("save")
        save.click()
        try:
            msg_grpExist = self.driver.find_element_by_xpath("/html/body/div[4]")
            if msg_grpExist.is_displayed():
                time.sleep(1)
                msg_grpExistp = self.driver.find_element_by_xpath("/html/body/div[4]/p")
                if msg_grpExistp.text in self.error_style:
                    print(msg_grpExistp.text)
                    # 点击关闭
                    time.sleep(3)
                    close = self.driver.find_element_by_id("modal-hide")
                    close.click()
                    time.sleep(2)
                else:
                    print("动态域名配置完成;")
            else:
                time.sleep(2)
        except BaseException as E:
            pass
        time.sleep(2)
        print("One2One配置完成！")
    def check_web_NAT_rule_One2One(self,config_name):
        head_all = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/thead/tr/th")
        # print("标题子项：", len(head_all))
        #  #展开
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            # print('len(td):',len(td))
            if len(td) > 1:
                # 页面 	规则名称
                rulename = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                # 页面 NAT类型
                NATType = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                # 页面 内网起始IP地址
                IPinFRROM= self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                # 页面 内网结束IP地址
                IPoutTo = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                # 页面 外网起始IP地址
                outStartIP = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % i).text
                # 页面 	绑定接口
                bindInterface = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % i).text
                if rulename == config_name:
                    print("规则名称：", rulename)
                    print("NAT类型：", NATType)
                    print("内网起始IP地址:", IPinFRROM)
                    print("内网结束IP地址:", IPoutTo)
                    print("外网起始IP地址:", outStartIP)
                    print("绑定接口:", bindInterface)
                    print("NAT规则---One2One 页面信息输出完成！")
                    self.assertEqual(rulename, self.One2One_name, '规则名称 与配置文件不一致')
                    self.assertEqual(NATType, self.One2One_type, 'NAT类型 与配置文件不一致')
                    self.assertEqual(IPinFRROM, self.One2One_beginip, '内网起始IP地址 与配置文件不一致')
                    self.assertEqual(IPoutTo, self.One2One_endip, '内网结束IP地址 与配置文件不一致')
                    self.assertEqual(outStartIP, self.One2One_outIP, '外网起始IP地址 与配置文件不一致')
                    self.assertEqual(bindInterface, self.One2One_interface, '绑定接口 与配置文件不一致')
                else:
                    pass
            else:
                # print("没有与配置文件%s一致的页面信息" % self.vlan_name)
                break
        return len(td)
    def del_nat_rule_sameconfig(self):
        u'''删除相同配置'''
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：", netconfig.text)
        # 端口映射 定位
        port_map = self.driver.find_element_by_link_text("端口映射")
        port_map.click()
        print("当前位置:", port_map.text)
        time.sleep(1)
        # 进入 nat规则 页面
        nat_rule = self.driver.find_element_by_link_text("NAT规则")
        print("当前位置:", nat_rule.text)
        nat_rule.click()
        time.sleep(3)
        tr = self.driver.find_elements_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr")
        print("每页显示个数为:", len(tr))
        print("*" * 30, '\n')
        time.sleep(2)
        # 判断是否已存在配置文件中的 配置 若有 则删除；
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                name_rule = self.driver.find_element_by_xpath(
                    ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                if name_rule == self.One2One_name:
                    delete = self.driver.find_element_by_xpath(
                        ".//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]" % i)
                    delete.click()
                    # time.sleep(2)
                    ok = webwait.until(lambda x: x.find_element_by_id("u-cfm-ok"))
                    # ok = self.driver.find_element_by_id("u-cfm-ok")
                    ok.click()
                    time.sleep(4)
                    print("有%s 规则，将其删除" % name_rule)
                else:
                    # print("页面无%s 规则删除" % self.EasyIP_name)
                    pass
            else:
                # print("页面无%s 规则删除" % self.One2One_name)
                break

    def test_Nat规则One2One配置(self):
        #  登陆web页面
        self.driver = Login_web()
        #
        #配置 One2One
        self.NAT_rule_config_One2One()
        #
        #判断页面信息 与 配置信息是否一致
        #
        self.check_web_NAT_rule_One2One(self.One2One_name)
        time.sleep(2)
        self.driver.quit()

    def test_Nat规则One2One验证(self):
        pass
    def test_NAT_规则One2One删除(self):
        #  登陆web页面
        self.driver = Login_web()
        # 删除配置
        self.del_nat_rule_sameconfig()
        '''# 删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("nat_rule_configure_delete_One2One")


if __name__ == '__main__':
    unittest.main()