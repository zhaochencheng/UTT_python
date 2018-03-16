# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 13:55
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_PPTP.py
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

class PPTP(unittest.TestCase):
    u'''**PPTP配置与操作**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def enter_pptp(self):
        u'''进入VPN配置--PPTP/L2TP页面'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # VPN配置 定位
        VPN = webwait.until(lambda x: x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
        VPN.click()
        print("当前位置：", VPN.text)
        # PPTP/L2TP页面 定位
        pptp = self.driver.find_element_by_link_text("PPTP/L2TP")
        pptp.click()
        print("当前位置：",pptp.text)

    def open_pptp_server(self):
        u'''开启pptp服务器'''
        self.enter_pptp()
        #pptp服务器全局配置
        time.sleep(2)
        PPTP_server_global_configuration= self.driver.find_element_by_link_text("PPTP服务器全局配置")
        PPTP_server_global_configuration.click()
        print("当前位置：",PPTP_server_global_configuration.text)
        time.sleep(2)
        #判断 服务器状态是否开启
        state_open = self.driver.find_element_by_xpath(".//input[@name = 'enable' and @value = 'ENABLE']")
        if state_open.is_selected():
            print("目前状态为开启状态")
        else:
            state_open.click()
            print("现在开启PPTP服务器")
        #地址池起始地址
        poolStart = self.driver.find_element_by_xpath(".//input[@name = 'poolStart']")
        print("地址池起始地址:",poolStart.get_attribute("value"))
        #最大连接数
        poolCount = self.driver.find_element_by_xpath(".//input[@name = 'poolCount']")
        print("最大连接数 :",poolCount.get_attribute("value"))
        #服务器端IP地址
        localIp = self.driver.find_element_by_xpath(".//input[@name = 'localIp']")
        print("服务器端IP地址:",localIp.get_attribute("value"))
        #主DNS服务器
        priDns = self.driver.find_element_by_xpath(".//input[@name = 'priDns']")
        priDns.clear()
        priDns.send_keys("114.114.114.114")
        #保存定位
        save = self.driver.find_element_by_id("save")
        save.click()

    def PPTP_config(self):
        u'''PPTP配置---做服务端'''
        #新增 定位
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(2)
        #工作模式
        workMode = self.driver.find_element_by_xpath(".//input[@name='workMode' and @value='1']")
        if workMode.is_selected():
            print("已选择服务端（拨入）")
        else:
            workMode.click()
            print("现在选择服务端（拨入）")
        #协议类型
        protoType = self.driver.find_element_by_xpath(".//input[@name='protoType' and @value='PPTP']")
        protoType.click()
        #隧道名称
        TunNames = self.driver.find_element_by_xpath(".//input[@name = 'TunNames']")
        TunNames.clear()
        TunNames.send_keys(PPTP_tunnelname[0])
        #用户类型
        userType = self.driver.find_element_by_xpath(".//select[@name = 'userType']")
        Select(userType).select_by_visible_text("LAN到LAN")
        #用户名
        userNames = self.driver.find_element_by_xpath(".//input[@name = 'userNames']")
        userNames.clear()
        userNames.send_keys(PPTP_username[0])
        #密码
        password = self.driver.find_element_by_xpath(".//input[@name = 'password']")
        password.clear()
        password.send_keys(PPTP_password[0])
        #远端内网地址
        remoteInIp = self.driver.find_element_by_xpath(".//input[@name = 'remoteInIp']")
        remoteInIp.clear()
        remoteInIp.send_keys(PPTP_remoteInIp[0])
        #远端内网子网掩码
        remoteInIPMask =self.driver.find_element_by_xpath(".//input[@name = 'remoteInIPMask']")
        remoteInIPMask.clear()
        remoteInIPMask.send_keys(PPTP_remoteInIPMask[0])
        #保存
        save =self.driver.find_element_by_id("save")
        save.click()
    def PPTP_check(self,config_name):
        u'''PPTP功能验证----做服务端'''
        self.driver1 = webdriver.Chrome()
        Login(self.driver1).login_router(End_to_end_wanip_url[0],End_to_end_wan_username,End_to_end_wan_password)
        # 显示等待
        webwait = WebDriverWait(self.driver1, 10, 1)
        # VPN配置 定位
        VPN = webwait.until(lambda x: x.find_element_by_xpath('//*[@id="sidebar"]/ul/li[9]/div/h4/span'))
        VPN.click()
        print("当前位置：", VPN.text)
        # PPTP/L2TP页面 定位
        pptp = self.driver1.find_element_by_link_text("PPTP/L2TP")
        pptp.click()
        print("当前位置：", pptp.text)
        # #页面显示个数
        shownumber = self.driver1.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        #  #选择  显示个数为50
        number_50 = self.driver1.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        # 标题栏 中有多少个子项
        head_all = self.driver1.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/thead/tr/th")
        print("标题子项：", len(head_all))
        #  #展开
        tr = self.driver1.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for j in range(len(config_name)):
            for i in range(1, len(tr) + 1):
                # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
                td = self.driver1.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
                if len(td) > 1:
                    name_rule = self.driver1.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    if name_rule == config_name[j]:
                        #
                        print("*" * 30, '\n')
                        for k in range(1, len(head_all) + 1):
                            try:
                                headname = self.driver1.find_element_by_xpath(
                                    "//*[@id='1']/div/div/div[1]/table/thead/tr/th[%d]/span" % k)
                                if headname.text == '操作':
                                    # 删除 页面与配置相同的 配置
                                    call = self.driver1.find_element_by_xpath(
                                        '//*[@id="1"]/div/div/div[1]/table/tbody/tr[%d]/td[%d]/a[1]' % (i, k))
                                    call.click()
                                    time.sleep(3)
                                else:
                                    pass
                            except BaseException as  E:
                                pass
                        time.sleep(2)
                        print("%s拨号完成  " % name_rule)
                        print("*" * 30, '\n')
                    else:
                        pass
                else:
                    break
        self.driver1.close()
    def PPTP_delete(self,config_name):
        u'''PPTP 配置删除'''
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
                        time.sleep(2)
                        print("将‘ %s ’与配置文件相同规则删除！  " % name_rule)
                        print("*" * 30, '\n')
                    else:
                        pass
                else:
                    break


    def PPTP_config_as_client(self):
        u'''PPTP配置---做客户端(拨出)'''
        #新增 定位
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(2)
        #工作模式
        workMode = self.driver.find_element_by_xpath(".//input[@name='workMode' and @value='2']")
        if workMode.is_selected():
            print("已选择客户端(拨出)")
        else:
            workMode.click()
            print("现在选择客户端(拨出)")
        #协议类型
        protoType = self.driver.find_element_by_xpath(".//input[@name='protoType' and @value='PPTP']")
        protoType.click()
        #隧道名称
        TunNames = self.driver.find_element_by_xpath(".//input[@name = 'TunNames']")
        TunNames.clear()
        TunNames.send_keys(PPTP_tunnelname[1])
        #隧道服务器地址
        TunNamesIP = self.driver.find_element_by_xpath(".//input[@name = 'TunNamesIP']")
        TunNamesIP.clear()
        TunNamesIP.send_keys(PPTP_asclient_tunSrvAddr[0])
        #用户名
        userNames = self.driver.find_element_by_xpath(".//input[@name = 'userNames']")
        userNames.clear()
        userNames.send_keys(PPTP_username[1])
        #密码
        password = self.driver.find_element_by_xpath(".//input[@name = 'password']")
        password.clear()
        password.send_keys(PPTP_password[1])
        #远端内网地址
        remoteInIp = self.driver.find_element_by_xpath(".//input[@name = 'remoteInIp']")
        remoteInIp.clear()
        remoteInIp.send_keys(PPTP_remoteInIp[1])
        #远端内网子网掩码
        remoteInIPMask =self.driver.find_element_by_xpath(".//input[@name = 'remoteInIPMask']")
        remoteInIPMask.clear()
        remoteInIPMask.send_keys(PPTP_remoteInIPMask[1])
        #保存
        save =self.driver.find_element_by_id("save")
        save.click()

    def test_27_001_PPTP_server_config(self):
        u'''PPTP服务器配置'''
        #开启PPTP服务器
        self.open_pptp_server()
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_server_config")
    def test_27_002_PPTP_as_server_config(self):
        u'''PPTP配置--做服务端'''
        #进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        '''进行PPTP配置'''
        time.sleep(2)
        self.PPTP_config()
        print("PPTP配置---做服务器端  配置完成！")
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_server_config")
    def test_27_003_PPTP_as_server_show(self):
        u'''PPTP信息显示--做服务端'''
        # 进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        #PPTP web页面信息输出
        Output_info(self.driver).output_all()
        '''#输出信息后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_server_show")
    def test_27_004_PPTP_as_server_validate(self):
        u'''PPTP功能验证--做服务端'''
        # 进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        '''做服务端 怎么验证，配置好，需要到客户端页面去拨号；'''
        '''内网可以通过进 对端设备的映射地址 去拨号'''
        self.PPTP_check(PPTP_tunnelname)
        time.sleep(3)
        #会话状态
        connectStatus = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[4]/span")
        print('页面显示会话状态:',connectStatus.text)
        self.assertEqual(connectStatus.text,"正常","当前会话状态错误")
        '''#验证后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_server_validate")
        '''工具判断vpn是否生效'''
        Ping().ping_IP(PPTP_remoteInIp[0])
    def test_27_005_PPTP_as_server_delete(self):
        u'''PPTP配置删除--做服务端'''
        #进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        '''删除PPTP配置'''
        self.PPTP_delete(PPTP_tunnelname)
        '''#删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_server_delete")

    def test_27_007_PPTP_as_Client_config(self):
        u''''PPTP配置--做客户端'''
        # 进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        '''进行PPTP配置---做客户端'''
        time.sleep(2)
        self.PPTP_config_as_client()
        print("PPTP配置---做客户端  配置完成！")
        '''#配置后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_Client_config")
    def test_27_008_PPTP_as_Client_show(self):
        u'''PPTP信息显示--做客户端'''
        # 进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        # PPTP web页面信息输出
        Output_info(self.driver).output_all()
        '''#输出信息后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_Client_show")
    def test_27_009_PPTP_as_Client_validate(self):
        u'''PPTP功能验证--做服务端'''
        # 进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        '''做客户端 要拨号 到服务端'''
        # 会话状态
        connectStatus = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[4]/span")
        print('页面显示会话状态:', connectStatus.text)
        self.assertEqual(connectStatus.text, "正常", "当前会话状态错误")
        '''#验证后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_Client_validate")
        '''工具判断vpn是否生效'''
        Ping().ping_IP(PPTP_remoteInIp[1])
    def test_27_010_PPTP_as_Client_delete(self):
        u'''PPTP配置删除--做客户端'''
        # 进入VPN配置--PPTP/L2TP页面
        self.enter_pptp()
        '''删除PPTP配置'''
        self.PPTP_delete(PPTP_tunnelname)
        '''#删除后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("PPTP_as_Client_delete")












if __name__ == '__main__':
    unittest.main()