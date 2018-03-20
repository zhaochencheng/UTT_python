# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 9:39
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : DHCP服务器.py
# @Software: PyCharm Community Edition
import unittest
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

from Autotest_2018.public_script.Output_web_info import Output_info
from Autotest_2018.public_script.function_public import *


class DHCP_server_基本功能(unittest.TestCase):
    #class静态参数
    #
    #配置参数获取
    #
    web_poolname = get_data("DHCP_server","poolname")
    web_poolstartIP = get_data("DHCP_server","poolstartIP")
    web_poolendIP = get_data("DHCP_server","poolendIP")
    web_poolnetmask = get_data("DHCP_server","poolnetmask")
    web_poolgatemake = get_data("DHCP_server","poolgatemake")
    web_poolleasetime = get_data("DHCP_server","poolleasetime")
    web_poolfirstDns = get_data("DHCP_server","poolfirstDns")
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_DHCP_server配置(self):
        # 登陆web页面
        self.driver = Login_web()
        #配置DHCP服务器
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        DHCPserver = self.driver.find_element_by_link_text("DHCP服务")
        DHCPserver.click()
        time.sleep(2)
        edit_path ="//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[15]/span[1]"
        edit = webwait.until(lambda x: EC.visibility_of_all_elements_located(edit_path))
        if edit:
             self.driver.find_element_by_xpath(edit_path).click()
        time.sleep(2)
        WEB_save = webwait.until(lambda x: x.find_element_by_id("save"))
        # 地址池状态 定位
        DhcpEnable = self.driver.find_element_by_xpath(".//input[@name = 'DhcpEnable' and @value='on']")
        DhcpEnable.click()
        # 起始地址 定位
        dhcpStart = self.driver.find_element_by_xpath(".//input[@name = 'dhcpStart']")
        dhcpStart.clear()
        dhcpStart.send_keys(self.web_poolstartIP)
        # 结束地址 定位
        dhcpEnd = self.driver.find_element_by_xpath(".//input[@name = 'dhcpEnd']")
        dhcpEnd.clear()
        dhcpEnd.send_keys(self.web_poolendIP)
        # 子网掩码 定位
        dhcpMask = self.driver.find_element_by_xpath(".//input[@name = 'dhcpMask']")
        dhcpMask.clear()
        dhcpMask.send_keys(self.web_poolnetmask)
        # 网关地址 定位
        dhcpGateway = self.driver.find_element_by_xpath(".//input[@name = 'dhcpGateway']")
        dhcpGateway.clear()
        dhcpGateway.send_keys(self.web_poolgatemake)
        #租用时间
        dhcpLease = self.driver.find_element_by_xpath(".//input[@name = 'dhcpLease']")
        dhcpLease.clear()
        dhcpLease.send_keys(self.web_poolleasetime)
        # 主DNS服务器 定位
        dhcpPriDns = self.driver.find_element_by_xpath(".//input[@name = 'dhcpPriDns']")
        dhcpPriDns.clear()
        dhcpPriDns.send_keys(self.web_poolfirstDns)
        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(3)
        checkbox = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[4]/input"))
        #
        # 判断DHCP server 是否开启并输出web页面DHCP server信息
        #
        self.assertTrue(checkbox.is_selected())
        Output_info(self.driver).output_content(config_name=self.web_poolname)
        time.sleep(2)
        self.driver.quit()

    def test_DHCP_server验证(self):
        pass
class DHCP_手工绑定(unittest.TestCase):
    # class静态参数
    #
    # 配置参数获取
    #
    web_static_username = get_data("DHCP_static", "static_username")
    web_static_ip = get_data("DHCP_static", "static_ip")
    web_static_mac = get_data("DHCP_static", "static_mac")
    error_style = ['该IP与MAC地址已做绑定，无法重复绑定!','该IP地址已做绑定，无法重复绑定!','该MAC地址已做绑定，无法重复绑定!','用户名已存在！']
    def setUp(self):
        pass
    def tearDown(self):
        time.sleep(3)
        pass
    def config_tree(self,config_name):
        u'''增加组织架构分组'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 用户管理 定位
        usermanage = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[5]/div/h4/span"))
        usermanage.click()
        # print("当前位置：", usermanage.text)
        # 组织成员 定位
        organization_member = self.driver.find_element_by_link_text("组织成员")
        organization_member.click()
        # print("当前位置：", organization_member.text)
        time.sleep(2)
        '''创建分组'''
        add = self.driver.find_element_by_id("addBtn_newTree_1")
        add.click()
        time.sleep(2)
        # 组名称 定位
        name = self.driver.find_element_by_xpath(".//input[@name='name']")
        name.send_keys(config_name)
        # 保存 定位
        save = self.driver.find_element_by_id("save")
        save.click()
        try:
            msg_grpExist = self.driver.find_element_by_xpath("/html/body/div[4]")
            if msg_grpExist.is_displayed():
                time.sleep(1)
                msg_grpExist1 = self.driver.find_element_by_xpath("/html/body/div[4]/p")
                if msg_grpExist1.text == '组名已存在':
                    print("组织架构中 %s 分组已存在"%config_name)
                    #点击关闭
                    time.sleep(3)
                    close = self.driver.find_element_by_id("modal-hide")
                    close.click()
                    time.sleep(2)
            else:
                time.sleep(2)
                print("新增组织分组:", config_name)
        except BaseException as E:
            pass
    def config_delete(self):
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
                # 页面 用户名
                dhcpUser = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                # 页面 IP地址
                dhcpIp = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                # 页面 MAC地址
                dhcpMac = self.driver.find_element_by_xpath(
                    "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                if dhcpUser == self.web_static_username and dhcpIp == self.web_static_ip and dhcpMac == self.web_static_mac:
                    delete = self.driver.find_element_by_xpath(
                        "//*[@id='2']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span[2]" % i)
                    delete.click()
                    time.sleep(2)
                    ok = self.driver.find_element_by_id("u-cfm-ok")
                    ok.click()
                    print("删除%s配置"% self.web_static_username)
                else:
                    print("页面无%s 该配置" % self.web_static_username)
            else:
                break
        return len(td)


    def test_DHCP_手工绑定_配置(self):
        # 登陆web页面
        self.driver = Login_web()
        #增加组织架构分组
        self.config_tree(get_data("organization_member","node_name"))
        #
        # 配置DHCP服务器
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        DHCPserver = self.driver.find_element_by_link_text("DHCP服务")
        DHCPserver.click()
        time.sleep(1)
        static_DHCP = self.driver.find_element_by_link_text("静态DHCP")
        static_DHCP.click()
        time.sleep(2)
        adds = self.driver.find_elements_by_id("add")
        add = adds[1]
        add.click()
        time.sleep(2)
        webwait.until(lambda x: x.find_element_by_id("save"))
        #地址池名称
        pools = self.driver.find_element_by_xpath('.//select[@name="pools"]')
        Select(pools).select_by_visible_text("default")
        #所属组
        pid = self.driver.find_element_by_xpath('.//select[@name="pid"]')
        Select(pid).select_by_index(0)
        #用户名
        UserName = self.driver.find_element_by_xpath(".//input[@name = 'UserName']")
        UserName.clear()
        UserName.send_keys(self.web_static_username)
        #IP 地址
        IP = self.driver.find_element_by_xpath(".//input[@name = 'IP']")
        IP.clear()
        IP.send_keys(self.web_static_ip)
        #MAC地址
        Mac = self.driver.find_element_by_xpath(".//input[@name = 'Mac']")
        Mac.clear()
        Mac.send_keys(self.web_static_mac)
        #保存定位
        save = self.driver.find_element_by_id("save")
        save.click()
        try:
            msg_grpExist = self.driver.find_element_by_xpath("/html/body/div[4]")
            if msg_grpExist.is_displayed():
                time.sleep(1)
                msg_grpExistp = self.driver.find_element_by_xpath("/html/body/div[4]/p")
                if msg_grpExistp.text in self.error_style:
                    print(msg_grpExistp.text)
                    #点击关闭
                    time.sleep(3)
                    close = self.driver.find_element_by_id("modal-hide")
                    close.click()
                    time.sleep(2)
                else:
                    print("静态DHCP配置完成;")
            else:
                time.sleep(2)
        except BaseException as E:
            pass
        #
        #等待配置返回页面
        #
        time.sleep(3)
        #页面 用户名
        dhcpUser = self.driver.find_element_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr[1]/td[2]/span").text
        #页面 IP地址
        dhcpIp = self.driver.find_element_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr[1]/td[4]/span").text
        #页面 MAC地址
        dhcpMac = self.driver.find_element_by_xpath("//*[@id='2']/div/div/div[1]/table/tbody/tr[1]/td[5]/span").text
        print("页面 用户名:",dhcpUser)
        print("页面 IP地址:",dhcpIp)
        print("页面 MAC地址:",dhcpMac)
        #
        # 判断页面显示信息与配置文件是否相同
        #
        self.assertEqual(dhcpUser,self.web_static_username,"页面 用户名与配置文件信息不一致")
        self.assertEqual(dhcpIp,self.web_static_ip,"页面 IP地址与配置文件信息不一致")
        self.assertEqual(dhcpMac,self.web_static_mac,"页面 MAC地址与配置文件信息不一致")
        self.driver.quit()
    def test_DHCP_手工帮定_验证(self):
        #
        #下层路由器 wan口设置动态获取ip；查看获取ip 是否是 配置文件中 mac --ip 对应一致
        #
        pass
    def test_DHCP_手工绑定_删除配置(self):
        # 登陆web页面
        self.driver = Login_web()
        # 配置DHCP服务器
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        DHCPserver = self.driver.find_element_by_link_text("DHCP服务")
        DHCPserver.click()
        time.sleep(1)
        static_DHCP = self.driver.find_element_by_link_text("静态DHCP")
        static_DHCP.click()
        time.sleep(2)
        #
        #将配置删除
        #
        self.config_delete()
        #
        #判断配置是否删除
        #
        if self.config_delete() == 1:
            print("配置已被删除！")

        self.driver.quit()
class DHCP全局配置(unittest.TestCase):
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def test_DNS代理配置(self):
        # 登陆web页面
        self.driver = Login_web()
        # 配置DHCP服务器
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        DHCPserver = self.driver.find_element_by_link_text("DHCP服务")
        DHCPserver.click()
        time.sleep(1)
        #全局配置
        Global_configuration = self.driver.find_element_by_link_text("全局配置")
        Global_configuration.click()
        #
        #开启DNS代理（默认是开启的）？？？
        #
        time.sleep(1)
        #开启状态 定位
        dnspEnblw = self.driver.find_element_by_xpath(".//input[@name = 'dnspEnblw' and @value = 'on']")
        if dnspEnblw.is_selected():
            print("默认开启DNS 代理")
        else:
            dnspEnblw1 = self.driver.find_element_by_xpath(".//input[@name = 'dnspEnblw' and @value = 'on']")
            dnspEnblw1.click()
            save = self.driver.find_element_by_id("save")
            save.click()
            print("现在开启DNS 代理")
        time.sleep(2)
        self.driver.quit()
    def test_DNS代理验证(self):
        pass


if __name__ == '__main__':
    # poolname = get_data("DHCP_server", "poolname")
    # poolstartIP = get_data("DHCP_server", "poolstartIP")
    # poolendIP = get_data("DHCP_server", "poolendIP")
    # poolnetmask = get_data("DHCP_server", "poolnetmask")
    # poolgatemake = get_data("DHCP_server", "poolgatemake")
    # poolleasetime = get_data("DHCP_server", "poolleasetime")
    # poolfirstDns = get_data("DHCP_server", "poolfirstDns")
    # print(poolname,poolstartIP,poolendIP,poolnetmask,poolgatemake,poolleasetime,poolfirstDns)
    # print(type(poolname))
    # unittest.main()
    # 手动添加单个用例
    suit = unittest.TestSuite()
    '''wan口配置'''
    # suit.addTest(DHCP_手工绑定("test_DHCP_手工绑定_配置"))
    # suit.addTest(DHCP_手工绑定("test_DHCP_手工绑定_删除配置"))
    suit.addTest(DHCP全局配置("test_DNS代理配置"))
    suit.addTest(DHCP全局配置("test_DNS代理验证"))
    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suit)
