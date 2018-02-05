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
from Re_OS_3.Public.Delect_sameConfig import Delect_config
from Re_OS_3.Config_data.config import *
from Re_OS_3.Tool.http200 import httpcode
from Re_OS_3.Tool.Ping import Ping

class NetManageStrate(unittest.TestCase):
    u'''**网管策略**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

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
                    time.sleep(2)
                    self.driver1.close()
                else:
                    pass
            except BaseException as  E:
                print("当前使用账户为：",admin_username[i])
                print("账号权限：读写！")
                print("*" * 30, '\n')
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



    def test_30_001_System_administrator(self):
        u'''系统管理员的配置'''
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        #系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：",Sysconfig.text)
        #网管策略 定位
        netmanageStrate =self.driver.find_element_by_link_text("网管策略")
        netmanageStrate.click()
        print("当前位置：",netmanageStrate.text)

        #输出系统管理员 信息
        Output_info(self.driver).output_all()

        # 配置系统管理员
        self.add_system_admin()
        #检查新增的管理员是否生效
        time.sleep(2)
        self.check_add_system_admin()
        #删除与配置文件相同的配置
        time.sleep(2)
        self.delect_add_system_admin(admin_username)






if __name__ == '__main__':
    unittest.main()