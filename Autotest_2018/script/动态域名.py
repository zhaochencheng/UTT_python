# -*- coding: utf-8 -*-
# @Time    : 2018/3/20 17:47
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : 动态域名.py
# @Software: PyCharm Community Edition
import time
import unittest
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait
from Autotest_2018.public_script.function_public import *

class 动态_域名(unittest.TestCase):
    # class静态参数
    #
    # 配置参数获取
    #
    DDNS_Server = get_data("DDNS_config", "DDNS_server")
    error_style = ['接口名称绑定重复']
    def setUp(self):
        pass
    def tearDown(self):
        pass
    def DDNS_Config(self):
        u"动态域名配置"
        #"进入 网络配置--动态域名页面"
        # 显示等待
        webwait = WebDriverWait(self.driver, 10, 1)
        # 网络配置  定位
        netconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[3]/div/h4/span"))
        netconfig.click()
        # print("当前位置:", netconfig.text)
        # 动态域名 定位
        ddns = self.driver.find_element_by_link_text("动态域名")
        ddns.click()
        # print("当前位置：", ddns.text)
        time.sleep(2)
        # 新增 定位
        add = self.driver.find_element_by_id("add")
        add.click()
        time.sleep(3)
        provider = self.driver.find_element_by_xpath(".//select[@name='DDNSProvider']")
        uttcare = Select(provider).select_by_value(self.DDNS_Server)
        time.sleep(1)
        # 接口  这里选择wan1 口
        interface = self.driver.find_element_by_xpath(".//select[@name='Profile']")
        Select(interface).select_by_value("WAN1")
        # 保存 点击
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
                    print("动态域名配置完成;")
            else:
                time.sleep(2)
        except BaseException as E:
            pass
        time.sleep(3)
        # 刷新 点击
        refresh = self.driver.find_element_by_id("fresh")
        refresh.click()

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
                # 页面 	接口
                interface = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[2]/span" % i).text
                # 页面 状态
                status = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                # 页面 服务商
                provider = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[4]/span" % i).text
                # 页面 主机名
                hostName = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[5]/span" % i).text
                # 页面 IP 地址
                ip = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[6]/span" % i).text
                # 页面 	更新时间
                freshTime = self.driver.find_element_by_xpath(
                    "//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[7]/span" % i).text
                if provider == self.DDNS_Server:
                    print("接口：", interface)
                    print("状态：", status)
                    print("服务商:", provider)
                    print("主机名:", hostName)
                    print("IP 地址:", ip)
                    print("更新时间:", freshTime)
                    print("动态域名页面信息输出完成！")
                    #往配置文件中写入 配置
                    set_date("DDNS_config", "ddns_address",hostName)
                    self.assertEqual(provider, self.DDNS_Server, '服务商 与配置文件不一致')
                else:
                    pass
            else:
                # print("没有与配置文件%s一致的页面信息" % self.vlan_name)
                break
        return len(td)
    def open_port8081(self):
        #开启远程管理 8081端口
        # 显示等待
        print("*" * 30, '\n')
        webwait = WebDriverWait(self.driver, 10, 1)
        # 系统配置 定位
        Sysconfig = webwait.until(lambda x: x.find_element_by_xpath("//*[@id='sidebar']/ul/li[11]/div/h4/span"))
        Sysconfig.click()
        print("当前位置：", Sysconfig.text)
        time.sleep(2)
        # 网管策略 定位
        netmanageStrate = self.driver.find_element_by_link_text("网管策略")
        netmanageStrate.click()
        print("当前位置：", netmanageStrate.text)
        # 远程管理 定位
        remote_management = self.driver.find_element_by_link_text("远程管理")
        remote_management.click()
        print("当前位置：", remote_management.text)
        time.sleep(2)
        # # **开启远程管理** # #
        # 状态 开启定位
        status_open = self.driver.find_element_by_xpath(".//input[@name='HttpEnable' and @ value='1']")
        u'''检查radio 标签是否被选中'''
        if status_open.is_selected():
            print("*" * 30, '\n')
            print("远程管理已开启！")
        else:
            status_open.click()
            print("*" * 30, '\n')
            print("远程管理现在开启")
            time.sleep(1)
        # 保存定位
        save = self.driver.find_element_by_id("save")
        save.click()
        time.sleep(3)



    def test_动态域名配置(self):
        # 登陆web页面
        self.driver = Login_web()
        #
        #配置动态域名
        #
        self.DDNS_Config()
        #
        #判断页面显示信息 与 配置文件是否相同
        #
        self.config_check()
        time.sleep(2)
        self.open_port8081()
        time.sleep(2)
        self.driver.quit()

    def test_动态域名验证(self):
        DDNS_hostname = get_data("DDNS_config", "ddns_address")
        print("当前主机名:", DDNS_hostname)
        #
        #通过域名 可以访问路由器
        #
        try:
            self.driver = Login_web(URL="http://%s:8081"%DDNS_hostname)
            print(self.driver.title)
            print(self.driver.current_url)
            self.assertEqual(self.driver.title,"艾泰科技","DDNS功能不生效")
            print("DDNS功能生效！")
            time.sleep(2)
            self.driver.quit()
        except BaseException as e:
            print(e)
            raise BaseException("无法打开该动态域名，功能未生效")

if __name__ == '__main__':
    # DDNS_Server = get_data("DDNS_config", "DDNS_server")
    # DDNS_addr = get_data("DDNS_config", "DDNS_address")
    # print(DDNS_addr)
    unittest.main()