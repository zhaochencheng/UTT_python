# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 16:32
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : 路由配置.py
# @Software: PyCharm Community Edition
import time
import unittest

from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Autotest_2018.public_script.Get_screenshot import Get_Screenshot
from Autotest_2018.public_script.function_public import *
class 静态路由(unittest.TestCase):
    # class静态参数
    #
    # 配置参数获取
    #
    static_router_rulename = get_data("router_config", "static_router_rulename")
    static_router_destNet = get_data("router_config", "static_router_destNet")
    static_router_netmask = get_data("router_config", "static_router_netmask")
    static_router_Gatewayip = get_data("router_config", "static_router_Gatewayip")
    static_router_com_priority = get_data("router_config", "static_router_com_priority")
    static_router_interface_LAN = get_data("router_config", "static_router_interface_LAN")
    error_style =['路由名称输入重复!']

    def setUp(self):
        pass
    def tearDown(self):
        pass
    def static_route_config(self):
        u"静态路由配置"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        # print("当前位置:", netconfig.text)
        # 路由配置 定位
        router_config = self.driver.find_element_by_link_text("路由配置")
        router_config.click()
        # print("当前位置:", router_config.text)
        time.sleep(2)
        # 新增 按钮
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(2)
        # 状态  --- 定位 开启 radio框是否被选中
        save1 = webwait.until(lambda x: x.find_element_by_id("save"))
        status = self.driver.find_element_by_xpath(".//input[@name='RouteEnables' and @value  = '1']")
        if status.is_selected():
            # print("规则状态 已开启")
            pass
        else:
            status.click()
            print("点击 开启 该规则")
            time.sleep(2)
        # 规则名称 定位
        rule_name = self.driver.find_element_by_xpath(".//input[@name='RouteNames']")
        rule_name.clear()
        rule_name.send_keys(self.static_router_rulename)
        # 目的网络 定位
        desip = self.driver.find_element_by_xpath(".//input[@name='DesIPs']")
        desip.clear()
        desip.send_keys(self.static_router_destNet)
        # 子网掩码 定位
        desMasks = self.driver.find_element_by_xpath(".//input[@name='DesMasks']")
        desMasks.clear()
        desMasks.send_keys(self.static_router_netmask)
        # 网关地址 定位
        GWway = self.driver.find_element_by_xpath(".//input[@name='GateWays']")
        GWway.clear()
        GWway.send_keys(self.static_router_Gatewayip)
        # 优先级 定位
        Metrics = self.driver.find_element_by_xpath(".//input[@name='Metrics']")
        Metrics.clear()
        Metrics.send_keys(self.static_router_com_priority)

        # 绑定接口  绑定wan1 口   -lan 口--
        #                     ---- 要考虑如何将所有接口都能绑定 进行测试
        interface = self.driver.find_element_by_xpath(".//select[@name='Profiles']")
        # Select(interface).select_by_value("WAN1")
        # Select(interface).select_by_value("LAN")
        Select(interface).select_by_visible_text(self.static_router_interface_LAN)
        # 点击保存
        save = self.driver.find_element_by_id("save")
        save.click()
        try:
            pageTip_warn= self.driver.find_element_by_xpath("/html/body/div[4]")
            if pageTip_warn.is_displayed():
                time.sleep(1)
                ROUTE_NAME_REPEAT = self.driver.find_element_by_xpath("/html/body/div[4]/p")
                if ROUTE_NAME_REPEAT.text in self.error_style:
                    print(ROUTE_NAME_REPEAT.text)
                    # 点击关闭
                    time.sleep(3)
                    close = self.driver.find_element_by_id("modal-hide")
                    close.click()
                    time.sleep(2)
                else:
                    print("静态路由配置完成;")
            else:
                print("静态路由配置完成;")
                time.sleep(2)
        except BaseException as E:
            pass
        time.sleep(5)
        print("静态路由配置完成")
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
                # 页面 规则名称
                routeName = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                # 页面 目的网络
                rou_destNet = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                # 页面 子网掩码
                netmask = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                #页面 网关地址
                GwAddr= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span"% i).text
                #页面 优先级
                com_priority= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span"% i).text
                #页面 绑定接口
                bind_if= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span"% i).text
                if routeName == self.static_router_rulename:
                    print("规则名称：",routeName)
                    print("目的网络：",rou_destNet)
                    print("子网掩码:",netmask)
                    print("网关地址:",GwAddr)
                    print("优先级:",com_priority)
                    print("绑定接口:",bind_if)
                    self.assertEqual(routeName,self.static_router_rulename,'规则名称 与配置文件不一致')
                    self.assertEqual(rou_destNet,self.static_router_destNet,'目的网络 与配置文件不一致')
                    self.assertEqual(netmask,self.static_router_netmask,'子网掩码 与配置文件不一致')
                    self.assertEqual(GwAddr,self.static_router_Gatewayip,'网关地址 与配置文件不一致')
                    self.assertEqual(com_priority,self.static_router_com_priority,'优先级 与配置文件不一致')
                    self.assertEqual(bind_if,self.static_router_interface_LAN,'绑定接口 与配置文件不一致')
                else:
                    pass
            else:
                # print("没有与配置文件%s一致的页面信息" % self.vlan_name)
                break
        return len(td)

    def static_router_delete(self):
        u"静态路由配置删除"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        # print("当前位置:", netconfig.text)
        # 路由配置 定位
        router_config = self.driver.find_element_by_link_text("路由配置")
        router_config.click()
        # print("当前位置:", router_config.text)
        time.sleep(2)
        # 删除配置 规则
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)

        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                name_rule = self.driver.find_element_by_xpath(
                    ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                if name_rule == self.static_router_rulename:
                    '''#删除配置前 截图#'''
                    Get_Screenshot(self.driver).get_screenshot(
                        "%s_static_router_delete_before" % (self.static_router_rulename))
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
                    '''#删除配置后 截图#'''
                    Get_Screenshot(self.driver).get_screenshot(
                        "%s_static_router_delete_after" % (self.static_router_rulename))
                    # print("*" * 30, '\n')
                else:
                    pass
            else:
                break
        print("*" * 30, '\n')

    def test_静态路由配置(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        # 进行静态路由配置
        #
        self.static_route_config()
        time.sleep(2)
        #
        #页面信息 与配置文件 进行比较
        #
        self.config_check()
        time.sleep(2)
        self.driver.quit()

    def test_静态路由验证(self):
        #
        #判断静态路由生效--- ping 目的网络？
        #
        pass

    def test_静态路由删除(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        self.static_router_delete()

class 策略路由(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass


if __name__ == '__main__':
    unittest.main()