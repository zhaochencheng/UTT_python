# -*- coding: utf-8 -*-
# @Time    : 2017/12/28 16:04
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : AP_offline.py
# @Software: PyCharm Community Edition

from selenium import webdriver
import time
from Utt.test_DP.Login_ac import *

def Ap_offline():
    '''将在线ap踢下线'''
    #登陆AC
    driver = webdriver.Chrome()
    driver.get("http://192.168.2.252")
    # cookies 输出
    # cookies_before = driver.get_cookies()
    # print(cookies_before)
    driver.find_element_by_css_selector("#username").clear()
    driver.find_element_by_css_selector("#username").send_keys('admin')
    driver.find_element_by_css_selector("#login_password").clear()
    driver.find_element_by_css_selector("#login_password").send_keys("admin_default")
    code = input("enter code:")  # 验证码
    driver.find_element_by_css_selector("#code").send_keys(code)
    driver.find_element_by_css_selector("#loginIn").click()
    time.sleep(3)
    # cookies 输出
    # cookies_after = driver.get_cookies()
    # print(cookies_after)
    print(driver.title+"\n")
    #AP管理
    AP_mangle= driver.find_element_by_css_selector("#menu_T_Wireless_Management > a > span")
    print("---"+AP_mangle.text+"---")
    AP_mangle.click()
    time.sleep(3)
    #在线AP
    AP_online = driver.find_element_by_css_selector("#menu_S_INFORMATION_AP > a > span")
    print("---"+AP_online.text+"---")
    AP_online.click()
    # 切换到AP信息管理 iframe 标签中
    iframe1 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]").find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/iframe[2]")
    driver.switch_to.frame(iframe1)
    while 1:
        #当前在线ap个数
        ap_count = driver.find_elements_by_xpath("//*[@id='ap_info_manage']/tbody/tr")
        len_ap_count = len(ap_count)
        print("\n当前在线ap个数:",len_ap_count)
        for i in range(0,len_ap_count):
            i = 1
            # AP 型号
            model = driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[2]"%i)
            print("AP 型号",model.text)
            #软件版本
            version = driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[6]"%i)
            print("软件版本:",version.text)
            #状态信息
            status_messages=driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[7]"%i)
            print("状态信息:",status_messages.text)
        # #点击将ap踢下线
            ap_offline = driver.find_element_by_xpath(".//*[@id='ap_info_manage']/tbody/tr[%d]/td[10]/span[1]"%i)
            ap_offline.click()
            time.sleep(2)
            # 接收alert 弹窗； 确定将ap下线；
            a = driver.switch_to_alert()
            print("弹窗内容：", a.text)
            a.accept()
            time.sleep(4)
        break
    driver.quit()

def test_ap_reboot():
        '''将在线ap重启'''
        driver = webdriver.Chrome()
        driver.get("http://192.168.2.252")
        # cookies 输出
        # cookies_before = driver.get_cookies()
        # print(cookies_before)
        driver.find_element_by_css_selector("#username").clear()
        driver.find_element_by_css_selector("#username").send_keys('admin')
        driver.find_element_by_css_selector("#login_password").clear()
        driver.find_element_by_css_selector("#login_password").send_keys("admin_default")
        code = input("enter code:")  # 验证码
        driver.find_element_by_css_selector("#code").send_keys(code)
        driver.find_element_by_css_selector("#loginIn").click()
        time.sleep(3)
        # AP管理
        AP_mangle = driver.find_element_by_css_selector("#menu_T_Wireless_Management > a > span")
        print("---" + AP_mangle.text + "---")
        AP_mangle.click()
        time.sleep(3)
        # 在线AP
        AP_online = driver.find_element_by_css_selector("#menu_S_INFORMATION_AP > a > span")
        print("---" + AP_online.text + "---")
        AP_online.click()

        # 切换到AP信息管理 iframe 标签中
        iframe1 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]").find_element_by_xpath(
            "/html/body/div[2]/div[3]/div/div[2]/iframe[2]")
        driver.switch_to.frame(iframe1)
        while 1:
            # 当前在线ap个数
            ap_count = driver.find_elements_by_xpath("//*[@id='ap_info_manage']/tbody/tr")
            len_ap_count = len(ap_count)
            if len_ap_count == 0:
                print("当前在线ap个数:", len_ap_count)
                break
                # time.sleep(120)
            else:
                print("当前在线ap个数:", len_ap_count)
                for i in range(0, len_ap_count):
                    i = 1
                    # AP 型号
                    model = driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[2]" % i)
                    print("AP 型号", model.text)
                    # 软件版本
                    version = driver.find_element_by_xpath("//*[@id='ap_info_manage']/tbody/tr[%d]/td[6]" % i)
                    print("软件版本:", version.text)
                    # 状态信息
                    status_messages = driver.find_element_by_xpath(
                        "//*[@id='ap_info_manage']/tbody/tr[%d]/td[7]" % i)
                    print("状态信息:", status_messages.text)
                    # #点击将ap踢下线
                    ap_reboot = driver.find_element_by_xpath(
                        ".//*[@id='ap_info_manage']/tbody/tr[%d]/td[10]/span[2]" % i)
                    ap_reboot.click()
                    time.sleep(2)
                    # 接收alert 弹窗； 确定将ap下线；
                    a = driver.switch_to_alert()
                    print("弹窗内容：", a.text)
                    a.accept()
                    time.sleep(4)
                break
        driver.switch_to_default_content()
        frame2 = driver.find_element_by_xpath("//*[@id='BODY']")
        admin_exit = frame2.find_element_by_xpath(".//*[@id='test-top-right']/table/tbody/tr/td[6]/span/a/span")
        admin_exit.click()
        a = driver.switch_to_alert()
        print("弹窗内容：", a.text)
        a.accept()
        time.sleep(2)

        driver.quit()


if __name__ == '__main__':
    # Ap_offline()
    test_ap_reboot()

