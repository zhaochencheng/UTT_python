# -*- coding: utf-8 -*-
# @Time    : 2018/1/30 17:05
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_DDNS.py
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
from Re_OS_3.Config_data.config import *
from Re_OS_3.Public.Get_screenshot import Get_Screenshot

class DDNS_config(unittest.TestCase):
    u'''**动态域名配置**'''
    def setUp(self):
        self.driver = webdriver.Chrome()
        Login(self.driver).login_router(url,username,pwd)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()
    def openhostname(self,hostname):
        u'''判断ddns是否生效'''
        #
        self.driver1 = webdriver.Chrome()
        url = "http://"+hostname+":8081"
        Login(self.driver1).login_router(url, username, pwd)
        print("title:",self.driver1.title)
        print("current_url:",self.driver1.current_url)
        print("self.driver1.title",self.driver1.title)
        if self.driver1.title == "艾泰科技":
            print("DDNS配置主机可以访问")
            '''#验证功能生效 截图#'''
            Get_Screenshot(self.driver).get_screenshot("DDNS_uttcare_config_validate")
        else:
            raise BaseException("DDNS配置主机无法访问")

    def enter_DDNS(self):
        u"进入 网络配置--动态域名页面"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        print("当前位置:", netconfig.text)
        # 动态域名 定位
        ddns = self.driver.find_element_by_link_text("动态域名")
        ddns.click()
        print("当前位置：", ddns.text)
        time.sleep(2)
        print("*" * 30, '\n')
    def DDNS_uttcare_config(self):
        u"DDNS 配置-uttcare.com"
        '''#配置前先 截图#'''
        Get_Screenshot(self.driver).get_screenshot("DDNS_uttcare_config_before")
        # 新增 定位
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(3)
        provider = self.driver.find_element_by_xpath(".//select[@name='DDNSProvider']")
        uttcare = Select(provider).select_by_value("uttcare.com")
        time.sleep(1)
        # 主机名 地址获取
        hostname = self.driver.find_element_by_xpath(".//input[@name='DDNSUtt']").get_attribute("value")
        print("主机名 url为：", hostname)
        # 接口  这里选择wan1 口
        interface = self.driver.find_element_by_xpath(".//select[@name='Profile']")
        Select(interface).select_by_value("WAN1")
        # 保存 点击
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(3)
        # 刷新 点击
        refresh = self.driver.find_element_by_id("fresh")
        refresh.click()
        '''#配置完成后 截图#'''
        Get_Screenshot(self.driver).get_screenshot("DDNS_uttcare_config_after")
    def DDNS_uttcare_show(self):
        u"将页面配置的uttcare  信息输出"
        # #将页面信息输出
        # 页面显示个数
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        # 选择  显示个数为50
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        #
        # 将页面信息输出
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                web_provider = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                if web_provider == "uttcare.com":
                    web_interface = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                    web_connect_status = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                    web_provider = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                    web_hostname = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                    web_ip = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % i).text
                    web_freshtime = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % i).text
                    print("绑定接口为：", web_interface, " 连接状态：", web_connect_status, " 服务商：", web_provider, " 主机名：",
                          web_hostname, " ip地址：", web_ip, " 更新时间：", web_freshtime)
                    print("*" * 30, '\n')
                else:
                    pass
            else:
                break
        time.sleep(2)
        '''#输出信息 截图#'''
        Get_Screenshot(self.driver).get_screenshot("DDNS_uttcare_config_show")
    def DDNS_uttcare_delete(self):
        u"将配置的uttcare信息 删除"
        # 页面显示个数
        shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
        shownumber.click()
        time.sleep(1)
        # 选择  显示个数为50
        number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
        number_50.click()
        #
        # 判断页面是否存在与配置 相同的配置
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                web_provider = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                if web_provider == "uttcare.com":
                    # 点击删除
                    web_hostname = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                    delete = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]" % i)
                    delete.click()
                    time.sleep(2)
                    # 确认删除
                    ok = self.driver.find_element_by_id("u-cfm-ok")
                    ok.click()
                    time.sleep(3)
                    print("将%s删除"%web_hostname)
                    '''#删除完成 截图#'''
                    Get_Screenshot(self.driver).get_screenshot("DDNS_uttcare_config_delect")
                else:
                    pass
            else:
                break

        time.sleep(4)
    def DDNS_uttcare_validate(self):
        u"DDNS-uttcare功能生效验证"
        # 将页面信息输出
        tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
        # print("每页显示个数为:", len(tr))
        time.sleep(2)
        web_hostname = []
        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                web_provider = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                if web_provider == "uttcare.com":
                    web_hostName = self.driver.find_element_by_xpath(
                        "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i)
                    web_hostname.append(web_hostName.text)
                    # print(web_hostName)
                    # print(type(web_hostName))
                else:
                    pass
            else:
                break
        time.sleep(2)

        if len(web_hostname) != 0:
            # #判断 ddns功能是否生效；-----如果打不开怎么办？
            self.openhostname(web_hostname[0])
        else:
            print("页面没有配置DDNS-uttcare")
            '''#没有配置成功 截图#'''
            Get_Screenshot(self.driver).get_screenshot("DDNS_uttcare_config_noDDNS_error")
            raise BaseException("页面没有配置DDNS-uttcare")


    # def test_06_001_ddns(self):
    #     u'''动态域名的新增与删除，'''
    #     #进入 网络配置--动态域名页面
    #     self.enter_DDNS()
    #
    #     # # 配置动态域名
    #     # #使用uttcare.com 服务商---- 默认主机名---绑定wan1口
    #
    #     # 页面显示个数
    #     shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
    #     shownumber.click()
    #     time.sleep(1)
    #     # 选择  显示个数为50
    #     number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
    #     number_50.click()
    #     #
    #     # 判断页面是否存在与配置 相同的配置
    #     tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
    #     # print("每页显示个数为:", len(tr))
    #     time.sleep(2)
    #     for i in range(1, len(tr) + 1):
    #         # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
    #         td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
    #         if len(td) > 1:
    #             web_provider = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span"%i).text
    #             if web_provider == "uttcare.com":
    #                 #点击删除
    #                 delete  = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]"%i)
    #                 delete.click()
    #                 time.sleep(2)
    #                 #确认删除
    #                 ok = self.driver.find_element_by_id("u-cfm-ok")
    #                 ok.click()
    #                 time.sleep(3)
    #             else:
    #                 pass
    #         else:
    #             break
    #
    #     time.sleep(4)
    #     #新增 定位
    #     add = self.driver.find_element_by_id("add")
    #     add.click()
    #     time.sleep(3)
    #     provider = self.driver.find_element_by_xpath(".//select[@name='DDNSProvider']")
    #     uttcare = Select(provider).select_by_value("uttcare.com")
    #     time.sleep(1)
    #     #主机名 地址获取
    #     hostname = self.driver.find_element_by_xpath(".//input[@name='DDNSUtt']").get_attribute("value")
    #     print("主机名 url为：",hostname)
    #     #接口  这里选择wan1 口
    #     interface = self.driver.find_element_by_xpath(".//select[@name='Profile']")
    #     Select(interface).select_by_value("WAN1")
    #     #保存 点击
    #     save = self.driver.find_element_by_id("save")
    #     save.click()
    #     time.sleep(3)
    #     #刷新 点击
    #     refresh = self.driver.find_element_by_id("fresh")
    #     refresh.click()
    #
    #     # #将页面信息输出
    #     # 页面显示个数
    #     shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
    #     shownumber.click()
    #     time.sleep(1)
    #     # 选择  显示个数为50
    #     number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
    #     number_50.click()
    #     #
    #     # 将页面信息输出
    #     tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
    #     # print("每页显示个数为:", len(tr))
    #     time.sleep(2)
    #     for i in range(1, len(tr) + 1):
    #         # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
    #         td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
    #         if len(td) > 1:
    #             web_provider = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span"%i).text
    #             if web_provider == "uttcare.com":
    #                 web_interface = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span"%i).text
    #                 web_connect_status = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span"%i).text
    #                 web_provider = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
    #                 web_hostname = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span"%i).text
    #                 web_ip = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span"%i).text
    #                 web_freshtime = self.driver.find_element_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span"%i).text
    #                 print("绑定接口为：",web_interface," 连接状态：",web_connect_status," 服务商：",web_provider," 主机名：",web_hostname," ip地址：",web_ip," 更新时间：",web_freshtime)
    #                 print("*" * 30, '\n')
    #
    #                 self.assertEqual(web_hostname,hostname ,"页面主机名和配置时主机名不一致！")
    #             else:
    #                 pass
    #         else:
    #             break
    #     time.sleep(2)
    #
    #     # #判断 ddns功能是否生效；-----如果打不开怎么办？
    #     self.openhostname(web_hostname)
    #
    #
    #
    #     time.sleep(2)
    #     # 页面显示个数
    #     shownumber = self.driver.find_element_by_xpath(".//button[@id = '1']")
    #     shownumber.click()
    #     time.sleep(1)
    #     # 选择  显示个数为50
    #     number_50 = self.driver.find_element_by_xpath("//*[@id='page-count-control']/div[1]/ul/li[3]/a")
    #     number_50.click()
    #     #
    #     # 删除配置
    #     tr = self.driver.find_elements_by_xpath("//*[@id='1']/div/div/div[1]/table/tbody/tr")
    #     # print("每页显示个数为:", len(tr))
    #     time.sleep(2)
    #     for i in range(1, len(tr) + 1):
    #         # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
    #         td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
    #         if len(td) > 1:
    #             web_provider = self.driver.find_element_by_xpath(
    #                 "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
    #             if web_provider == "uttcare.com":
    #                 # 点击删除
    #                 delete = self.driver.find_element_by_xpath(
    #                     "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[8]/span[2]" % i)
    #                 delete.click()
    #                 time.sleep(2)
    #                 # 确认删除
    #                 ok = self.driver.find_element_by_id("u-cfm-ok")
    #                 ok.click()
    #                 print("*" * 30, '\n')
    #                 print("将%s 该条ddns删除！"%("uttcare.com"))
    #                 time.sleep(3)
    #             else:
    #                 pass
    #         else:
    #             break

    def test_06_001_DDNS_uttcare_config(self):
        u"配置DDNS-uttcare"
        #进入动态域名页面
        self.enter_DDNS()
        '''配置DDNS uttcare'''
        self.DDNS_uttcare_config()

    def test_06_002_DDNS_uttcare_show(self):
        u"DDNS-uttcare信息输出"
        # 进入动态域名页面
        self.enter_DDNS()
        '''将配置的DDNS uttcare信息输出'''
        self.DDNS_uttcare_show()

    def test_06_003_DDNS_uttcare_validate(self):
        u"DDNS-uttcare功能生效验证"
        # 进入动态域名页面
        self.enter_DDNS()
        '''DDNS-uttcare功能生效验证'''
        self.DDNS_uttcare_validate()

    def test_06_004_DDNS_uttcare_del(self):
        u"将配置的DDNS-uttcare信息删除"
        # 进入动态域名页面
        self.enter_DDNS()
        '''将配置的DDNS-uttcare信息删除'''
        self.DDNS_uttcare_delete()




if __name__ == '__main__':
    unittest.main()