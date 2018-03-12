# -*- coding: utf-8 -*-
# @Time    : 2018/2/5 21:55
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_NetManageStrate.py
# @Software: PyCharm
from datetime import time
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import unittest
import time,random
from selenium import webdriver
from Re_OS_3.Public.Login_Router import Login
from Re_OS_3.Public.Output_web_info import Output_info
from Re_OS_3.Public.Delect_Config import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class NetManageStrate(unittest.TestCase):
    u'''**网管策略**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def enter_netmanageStrate(self):
        u"进入系统配置---网管策略页面"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：", Sysconfig.text)
        # 网管策略 定位
        netmanageStrate = self.driver.find_element_by_link_text("网管策略")
        netmanageStrate.click()
        print("当前位置：", netmanageStrate.text)

    def add_system_admin(self):
        u'''新增 系统管理员'''
        for i in range(len(admin_username)):
            add = self.driver.find_element_by_id("add")
            add.click()
            time.sleep(2)
            #用户名 定位
            admin_name = self.driver.find_element_by_xpath(".//input[@name='username']")
            admin_name.clear()
            admin_name.send_keys(admin_username[i])
            #密码 定位
            admin_pwd = self.driver.find_element_by_xpath(".//input[@name='passwd1']")
            admin_pwd.clear()
            admin_pwd.send_keys(admin_password[i])
            #确认密码 定位
            admin_pwd_again = self.driver.find_element_by_xpath(".//input[@name='passwd2']")
            admin_pwd_again.clear()
            admin_pwd_again.send_keys(admin_password[i])
            #权限 定位
            role = self.driver.find_element_by_xpath(".//select[@name = 'role']")
            # Select(role).select_by_visible_text("读写")
            Select(role).select_by_index(i)
            #保存 定位
            save =self.driver.find_element_by_id("save")
            save.click()
            time.sleep(3)
            '''#配置 截图#'''
            Get_Screenshot(self.driver).get_screenshot("System_administrator_configure_%s" % (admin_username[i]))
    def check_add_system_admin(self):
        u'''检查新增的管理员是否生效'''
        for i in range(len(admin_username)):
            self.driver1 = webdriver.Chrome()
            Login(self.driver1).login_router(url,admin_username[i],admin_password[i])
            try:
                role = self.driver1.find_element_by_xpath("//*[@id='header']/header/ul/li[1]/span[1]")
                if role.is_displayed():
                    rolestatus = self.driver1.find_element_by_id("header_account_access")
                    print("当前使用账户为：",admin_username[i])
                    print("账号权限：",rolestatus.text)
                    print("*" * 30, '\n')
                    # 验证 截图#'''
                    Get_Screenshot(self.driver1).get_screenshot("System_administrator_configure_%s_validate"%(admin_username[i]))
                    time.sleep(2)
                    self.driver1.close()
                else:
                    pass
            except BaseException as  E:
                print("当前使用账户为：",admin_username[i])
                print("账号权限:读写",)
                print("*" * 30, '\n')
                # 验证 截图#'''
                Get_Screenshot(self.driver1).get_screenshot(
                    "System_administrator_configure_%s_validate" % (admin_username[i]))
                self.driver1.close()
                print(E)
    def delect_add_system_admin(self,config_name):
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
                        time.sleep(2)
                        print("将‘ %s ’与配置文件相同规则删除！  " % name_rule)
                        print("*" * 30, '\n')
                    else:
                        pass
                else:
                    break
        # 验证 截图#'''
        Get_Screenshot(self.driver).get_screenshot("System_administrator_configure_delect")
    def show_add_system_admin(self,config_name):
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
                        #标题栏 与 内容 同步输出！
                        print("*" * 30, '\n')
                        for k in range(1, len(head_all) + 1):
                            try:
                                headname = self.driver.find_element_by_xpath(
                                    "//*[@id='1']/div/div/div[1]/table/thead/tr/th[%d]/span" % k)
                                if headname.is_displayed():
                                    content = self.driver.find_element_by_xpath(
                                        '//*[@id="1"]/div/div/div[1]/table/tbody/tr[%d]/td[%d]/span' % (i, k)).text
                                    print(headname.text, ":", content)
                                    self.assertEqual(content,config_name[j],"用户名-页面显示与配置文件不一致！")
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
        # 配置前先 截图#'''
        Get_Screenshot(self.driver).get_screenshot("System_administrator_configure_show")

    def test_30_001_System_administrator_config(self):
        u"系统管理员的配置"
        #进入系统配置--网管配置--系统管理员页面
        self.enter_netmanageStrate()
        #系统管理员配置
        self.add_system_admin()
    def test_30_002_System_administrator_show(self):
        u'''系统管理员页面信息输出'''
        # 进入系统配置--网管配置--系统管理员页面
        self.enter_netmanageStrate()
        #系统管理员页面信息输出
        self.show_add_system_admin(admin_username)
    def test_30_003_System_administrator_validate(self):
        u'''系统管理员功能生效验证'''
        self.check_add_system_admin()
    def test_30_004_System_administrator_delect(self):
        u'''系统管理员配置删除'''
        # 进入系统配置--网管配置--系统管理员页面
        self.enter_netmanageStrate()
        #系统管理员配置删除
        self.delect_add_system_admin(admin_username)

    def test_30_006_Intranet_access_control(self):
        u'''内网访问控制配置与操作'''
        pass

    def check_remote_effective(self):
        u'''开启远程管理并检查其是否生效'''

        # 状态 关闭定位
        status_off = self.driver.find_element_by_xpath(".//input[@name='HttpEnable' and @ value='0']")
        if status_off.is_selected():
            print("*" * 30, '\n')
            print("远程管理 已关闭！")

        else:
            status_off.click()
            print("*" * 30, '\n')
            print("现在关闭 远程管理！")

            # 保存定位
            save = self.driver.find_element_by_id("save")
            save.click()
        time.sleep(2)
        remote_Outport1 = self.driver.find_element_by_xpath(".//input[@name='OutPort']")
        port = remote_Outport1.get_attribute("value")
        print("端口为：", port)
        print("*" * 30, '\n')
        time.sleep(3)
        # 开启远程管理  ---判断 能否 远程登陆 远程管理 ip
        httpcode().http200("http://" + "192.168.30.115" + ":" + port)


        #状态 开启定位
        status_open = self.driver.find_element_by_xpath(".//input[@name='HttpEnable' and @ value='1']")
        if status_open.is_selected():
            print("*" * 30, '\n')
            print("远程管理 已开启！")

        else:
            print("*" * 30, '\n')
            status_open.click()
            print("现在开启 远程管理！")

            #保存定位
            save =self.driver.find_element_by_id("save")
            save.click()
        time.sleep(2)
        remote_Outport = self.driver.find_element_by_xpath(".//input[@name='OutPort']")
        port = remote_Outport.get_attribute("value")
        print("端口为：",port)
        print("*" * 30, '\n')
        time.sleep(3)
        #开启远程管理  ---判断 能否 远程登陆 远程管理 ip
        httpcode().http200("http://"+"192.168.30.115"+":"+port)

    def check_status(self,location):
        u'''检查radio 标签是否被选中'''
        if location.is_selected():
            print("*" * 30, '\n')
            print("已选中该操作！")

        else:
            location.click()
            print("*" * 30, '\n')
            print("现该操作未被选中，现在选中")
            time.sleep(1)
            # 保存定位
            save = self.driver.find_element_by_id("save")
            save.click()

    def test_30_008_Remote_management_open(self):
        u'''远程管理-开启'''
        #进入系统配置--网管配置 页面
        self.enter_netmanageStrate()
        # 远程管理 定位
        remote_management = self.driver.find_element_by_link_text("远程管理")
        remote_management.click()
        print("当前位置：", remote_management.text)
        time.sleep(2)
        # # **开启远程管理** # #
        # 状态 开启定位
        status_open = self.driver.find_element_by_xpath(".//input[@name='HttpEnable' and @ value='1']")
        self.check_status(status_open)
        time.sleep(2)
        # 端口 定位
        remote_Outport = self.driver.find_element_by_xpath(".//input[@name='OutPort']")
        port = remote_Outport.get_attribute("value")
        print("端口为：", port)
        '''判断状态是否开启'''
        stat_open = self.driver.find_element_by_xpath(".//input[@name='HttpEnable' and @ value='1']")
        self.assertTrue(stat_open.is_selected(),"远程管理未开启成功！")
        # 配置开启 截图#'''
        Get_Screenshot(self.driver).get_screenshot("Remote_management_config_open")

    def test_30_009_Remote_management_validate(self):
        u'''远程管理功能生效判断'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x:x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置：",netconfig.text)
        #外网配置 定位
        wan_config = self.driver.find_element_by_link_text("外网配置")
        wan_config.click()
        time.sleep(2)
        # self.driver.refresh()
        wan1_ip= self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[1]/td[3]/span").text
        print(wan1_ip)
        # 开启远程管理  ---判断 能否 远程登陆 远程管理 ip
        httpcode().http200("http://" + wan1_ip + ":" + "8081")
    def test_30_010_Remote_managment_close(self):
        u"远程管理-关闭"
        # 进入系统配置--网管配置 页面
        self.enter_netmanageStrate()
        # 远程管理 定位
        remote_management = self.driver.find_element_by_link_text("远程管理")
        remote_management.click()
        print("当前位置：", remote_management.text)
        time.sleep(2)
        status_off = self.driver.find_element_by_xpath(".//input[@name='HttpEnable' and @ value='0']")
        self.check_status(status_off)
        # 端口定位
        remote_Outport1 = self.driver.find_element_by_xpath(".//input[@name='OutPort']")
        port = remote_Outport1.get_attribute("value")
        print("端口为：", port)
        print("*" * 30, '\n')
        time.sleep(3)
        '''判断状态是否开启'''
        stat_off = self.driver.find_element_by_xpath(".//input[@name='HttpEnable' and @ value='0']")
        self.assertTrue(stat_off.is_selected(),"远程管理未关闭成功！")
        # 配置关闭 截图#'''
        Get_Screenshot(self.driver).get_screenshot("Remote_management_config_close")

    def test_30_012_Net_management_access_strategy(self):
        u'''网管访问策略配置与操作'''
         # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：", Sysconfig.text)
        # 网管策略 定位
        netmanageStrate = self.driver.find_element_by_link_text("网管策略")
        netmanageStrate.click()
        print("当前位置：", netmanageStrate.text)
        #网管访问策略 定位
        access_strategy = self.driver.find_element_by_link_text("网管访问策略")
        access_strategy.click()

    def test_30_013_language_select(self):
        u'''语言选择'''
         # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：", Sysconfig.text)
        # 网管策略 定位
        netmanageStrate = self.driver.find_element_by_link_text("网管策略")
        netmanageStrate.click()
        print("当前位置：", netmanageStrate.text)
        #语言选择 定位
        language = self.driver.find_element_by_link_text("语言选择")
        language.click()
        print("当前位置：",language.text)
        #中文定位
        chinese = self.driver.find_element_by_xpath(".//input[@name='langSelection']")
        self.check_status(chinese)
        time.sleep(3)
        chinese_name =self.driver.find_element_by_xpath("//*[@id='5']/table/tbody/tr/td[2]/span")
        print("当前语言为：",chinese_name.text)






if __name__ == '__main__':
    unittest.main()