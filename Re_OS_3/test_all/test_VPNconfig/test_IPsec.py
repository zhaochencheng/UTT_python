# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 13:41
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_IPsec.py
# @Software: PyCharm Community Edition
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.Ping import Ping
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class IPSec(unittest.TestCase):
    u'''**IPSec配置与操作**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def enter_VPN(self):
        u'''进入VPN配置--IPsec页面'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # VPN配置 定位
        VPN = webwait.until(lambda x: x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
        VPN.click()
        print("当前位置：", VPN.text)
        # IPSec 定位
        IPSec = self.driver.find_element_by_link_text("IPSec")
        IPSec.click()
        print("当前位置：", IPSec.text)
    def IPsec_config_connected_local(self):
        add = self.driver.find_element_by_id("add")
        add.click()
        # 连接方式
        conntype = self.driver.find_element_by_xpath(".//select[@name = 'connType']")
        Select(conntype).select_by_visible_text("对方动态连接到本地")
        # 隧道名称
        ids = self.driver.find_element_by_xpath(".//input[@name='ids']")
        ids.clear()
        ids.send_keys(tunnelName[0])
        # 远端内网地址
        remoteAddr = self.driver.find_element_by_xpath(".//input[@name = 'remoteAddr']")
        remoteAddr.clear()
        remoteAddr.send_keys(remoteip[0])

        # 预共享密钥
        preshareKey = self.driver.find_element_by_xpath(".//input[@name = 'preshareKey']")
        preshareKey.clear()
        preshareKey.send_keys(shareKey[0])

        # 保存
        save = self.driver.find_element_by_id("save")
        save.click()
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("IPsec_config_connected_local_config")
    def Check_IPsec_config_connected_local(self,config_name):
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
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == config_name[j]:
                        # 标题栏 与 内容 同步输出！
                        print("*" * 30, '\n')
                        for k in range(1, len(head_all) + 1):
                            try:
                                headname = self.driver.find_element_by_xpath(
                                    "//*[@id='1']/div/div/div[1]/table/thead/tr/th[%d]/span" % k)
                                if headname.is_displayed():
                                    content = self.driver.find_element_by_xpath(
                                        '//*[@id="1"]/div/div/div[1]/table/tbody/tr[%d]/td[%d]/span' % (i, k)).text
                                    print(headname.text, ":", content)
                                else:
                                    pass
                            except BaseException as  E:
                                pass

                        time.sleep(2)
                        print("该 ‘ %s ’ 规则信息已全部输出 " % name_rule)
                        print("*" * 30, '\n')
                    else:
                        pass
                else:
                    # print("页面无信息！")
                    break
    def Delect_IPsec_config_connected_local(self,config_name):
        u'''将页面与配置信息 相同的配置删除'''
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
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == config_name[j]:
                        #
                        print("*" * 30, '\n')
                        for k in range(1, len(head_all) + 1):
                            try:
                                headname = self.driver.find_element_by_xpath(
                                    "//*[@id='1']/div/div/div[1]/table/thead/tr/th[%d]/span" % k)
                                if headname.text == '编辑':
                                    # 删除 页面与配置相同的 配置
                                    delete = self.driver.find_element_by_xpath(
                                        '//*[@id="1"]/div/div/div[1]/table/tbody/tr[%d]/td[%d]/span[2]' % (i, k))
                                    delete.click()
                                    time.sleep(3)
                                    # 确认删除
                                    ok = self.driver.find_element_by_id("u-cfm-ok")
                                    ok.click()
                                    time.sleep(3)
                                else:
                                    pass
                            except BaseException as  E:
                                pass
                        time.sleep(4)
                        print("先将‘ %s ’与配置文件相同规则删除！  " % name_rule)
                        print("*" * 30, '\n')
                    else:
                        pass
                else:
                    break


    # def test_26_001_IPsec(self):
    #     u'''IPsec配置--对方动态连接到本地'''
    #     # 显示等待
    #     webwait = WebDriverWait(self.driver, 10, 1)
    #     #VPN配置 定位
    #     VPN = webwait.until(lambda x:x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
    #     VPN.click()
    #     print("当前位置：",VPN.text)
    #     #IPSec 定位
    #     IPSec= self.driver.find_element_by_link_text("IPSec")
    #     IPSec.click()
    #     print("当前位置：",IPSec.text)
    #     # 配置前 先测试一下是否可以ping 同对端内网
    #     try:
    #         Ping().ping_IP(remoteip[0])
    #     except BaseException as E:
    #         if E:
    #             print("未配置VPN，无法ping同该ip")
    #         else:
    #             raise BaseException("功能生效不生效；")
    #
    #     # #　* 配置VPN * # #
    #     #新增 定位
    #     time.sleep(2)
    #     add = self.driver.find_element_by_id("add")
    #     add.click()
    #     #连接方式
    #     conntype= self.driver.find_element_by_xpath(".//select[@name = 'connType']")
    #     Select(conntype).select_by_visible_text("对方动态连接到本地")
    #     #隧道名称
    #     ids = self.driver.find_element_by_xpath(".//input[@name='ids']")
    #     ids.clear()
    #     ids.send_keys(tunnelName[0])
    #     #远端内网地址
    #     remoteAddr = self.driver.find_element_by_xpath(".//input[@name = 'remoteAddr']")
    #     remoteAddr.clear()
    #     remoteAddr.send_keys(remoteip[0])
    #
    #     #预共享密钥
    #     preshareKey = self.driver.find_element_by_xpath(".//input[@name = 'preshareKey']")
    #     preshareKey.clear()
    #     preshareKey.send_keys(shareKey[0])
    #
    #     # 保存
    #     save =self.driver.find_element_by_id("save")
    #     save.click()
    #     # #
    #
    #     #输出页面 隧道列表 信息
    #     Output_info(self.driver).output_all()
    #
    #     #判断配置VPN 后是否生效
    #     Ping().ping_IP(remoteip[0])
    #
    #     # 删除刚配置的 VPN
    #     # ----在这提出 前端页面 格式一会带id 一会不带id 套用随意  导致公共函数不能使用；

    def test_26_001_IPsec_dynamically_connected_local_config(self):
        u'''IPsec配置--对方动态连接到本地'''
        #进入VPN配置--IPsec页面
        self.enter_VPN()
        '''ipsec 对方动态连接到本地 配置'''
        self.IPsec_config_connected_local()
        print("IPsec配置--对方动态连接到本地---配置完成")

    def test_26_002_IPsec_dynamically_connected_local_show(self):
        u'''IPsec配置信息输出--对方动态连接到本地'''
        #进入VPN配置--IPsec页面
        self.enter_VPN()
        '''输出页面 隧道列表 信息'''
        # Output_info(self.driver).output_all()
        self.Check_IPsec_config_connected_local(tunnelName)
        '''#输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("IPsec_config_connected_local_show")

    def test_26_003_IPsec_dynamically_connected_local_validate(self):
        u'''IPsec功能验证--对方动态连接到本地'''
        '''判断配置VPN 后是否生效'''
        Ping().ping_IP(remoteip[0])

    def test_26_004_IPsec_dynamically_connected_local_delete(self):
        u'''IPsec配置删除--对方动态连接到本地'''
        ##进入VPN配置--IPsec页面
        self.enter_VPN()
        '''删除刚配置的 VPN'''
        self.Delect_IPsec_config_connected_local(tunnelName)
        '''#删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("IPsec_config_connected_local_delete")

    # def test_26_002_IPsec(self):
    #     u'''IPsec配置--动态连接到网关'''
    #     # 显示等待
    #     webwait = WebDriverWait(self.driver, 10, 1)
    #     # VPN配置 定位
    #     VPN = webwait.until(lambda x: x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
    #     VPN.click()
    #     print("当前位置：", VPN.text)
    #     # IPSec 定位
    #     IPSec = self.driver.find_element_by_link_text("IPSec")
    #     IPSec.click()
    #     print("当前位置：", IPSec.text)
    #     # 配置前 先测试一下是否可以ping 同对端内网
    #     # try:
    #     #     Ping().ping_IP(remoteip[0])
    #     # except BaseException as E:
    #     #     if E:
    #     #         print("未配置VPN，无法ping同该ip")
    #     #     else:
    #     #         raise BaseException("功能生效不生效；")
    #
    #     # #　* 配置VPN * # #
    #     # 新增 定位
    #     time.sleep(2)
    #     add = self.driver.find_element_by_id("add")
    #     add.click()
    #     # 连接方式
    #     conntype = self.driver.find_element_by_xpath(".//select[@name = 'connType']")
    #     Select(conntype).select_by_visible_text("动态连接到网关")
    #     # 隧道名称
    #     ids = self.driver.find_element_by_xpath(".//input[@name='ids']")
    #     ids.clear()
    #     ids.send_keys(tunnelName[1])
    #     #远端网关地址（域名）
    #     peer = self.driver.find_element_by_xpath(".//input[@name = 'peer']")
    #     peer.clear()
    #     peer.send_keys(peerip[1])
    #
    #     # 远端内网地址
    #     remoteAddr = self.driver.find_element_by_xpath(".//input[@name = 'remoteAddr']")
    #     remoteAddr.clear()
    #     remoteAddr.send_keys(remoteip[1])
    #
    #     # 预共享密钥
    #     preshareKey = self.driver.find_element_by_xpath(".//input[@name = 'preshareKey']")
    #     preshareKey.clear()
    #     preshareKey.send_keys(shareKey[1])
    #
    #     # 保存
    #     save = self.driver.find_element_by_id("save")
    #     save.click()
    #     # #
    #
    #     # 输出页面 隧道列表 信息
    #     Output_info(self.driver).output_all()
    #
    #     # 判断配置VPN 后是否生效
    #     # Ping().ping_IP(remoteip[1])
    #
    #     # 删除刚配置的 VPN
    #     # ----在这提出 前端页面 格式一会带id 一会不带id 套用随意  导致公共函数不能使用；
    #
    #
    #
    #     #

    def IPsec_dynamically_connected_gateway_config(self):
        u'''IPsec配置--动态连接到网关'''
        add = self.driver.find_element_by_id("add")
        add.click()
        # 连接方式
        conntype = self.driver.find_element_by_xpath(".//select[@name = 'connType']")
        Select(conntype).select_by_visible_text("动态连接到网关")
        # 隧道名称
        ids = self.driver.find_element_by_xpath(".//input[@name='ids']")
        ids.clear()
        ids.send_keys(tunnelName[1])
        # 远端网关地址（域名）
        peer = self.driver.find_element_by_xpath(".//input[@name = 'peer']")
        peer.clear()
        peer.send_keys(peerip[1])

        # 远端内网地址
        remoteAddr = self.driver.find_element_by_xpath(".//input[@name = 'remoteAddr']")
        remoteAddr.clear()
        remoteAddr.send_keys(remoteip[1])

        # 预共享密钥
        preshareKey = self.driver.find_element_by_xpath(".//input[@name = 'preshareKey']")
        preshareKey.clear()
        preshareKey.send_keys(shareKey[1])

        # 保存
        save = self.driver.find_element_by_id("save")
        save.click()
    def test_26_006_IPsec_dynamically_connected_gateway_config(self):
        u'''IPsec配置--动态连接到网关'''
        #进入VPN配置--IPsec页面
        self.enter_VPN()
        '''IPsec配置--动态连接到网关'''
        self.IPsec_dynamically_connected_gateway_config()
        print("IPsec配置--动态连接到网关---配置完成")
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("IPsec_dynamically_connected_gateway_config")
    def test_26_007_IPsec_dynamically_connected_gateway_show(self):
        u'''IPsec信息显示--动态连接到网关'''
        # 进入VPN配置--IPsec页面
        self.enter_VPN()
        '''IPsec信息显示--动态连接到网关'''
        self.Check_IPsec_config_connected_local(tunnelName)
        '''#输出后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("IPsec_dynamically_connected_gateway_show")
    def test_26_008_IPsec_dynamically_connected_gateway_validate(self):
        u'''IPsec功能验证--动态连接到网关'''

        '''判断配置VPN 后是否生效'''
        Ping().ping_IP(remoteip[1])
    def test_26_009_IPsec_dynamically_connected_gateway_delete(self):
        u'''IPsec配置删除--动态连接到网关'''
        # 进入VPN配置--IPsec页面
        self.enter_VPN()
        '''IPsec配置删除--动态连接到网关'''
        self.Delect_IPsec_config_connected_local(tunnelName)
        '''#删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("IPsec_dynamically_connected_gateway_delete")






if __name__ == '__main__':
    unittest.main()