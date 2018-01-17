# -*- coding: utf-8 -*-
# @Time    : 2018/1/12 18:10
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : AP_config.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time
from Utt.test_DP.Login_ac import *
import random

def Ap_Config():
    f = open("ssid1.txt","w+")
    '''AP配置下发'''
    #登陆AC
    driver = webdriver.Chrome()
    driver.get("http://192.168.2.252")
    driver.maximize_window()
    driver.find_element_by_css_selector("#username").clear()
    driver.find_element_by_css_selector("#username").send_keys('admin')
    driver.find_element_by_css_selector("#login_password").clear()
    driver.find_element_by_css_selector("#login_password").send_keys("admin_default")
    code = input("enter code:")  # 验证码
    driver.find_element_by_css_selector("#code").send_keys(code)
    driver.find_element_by_css_selector("#loginIn").click()
    time.sleep(3)
    print(driver.title+"\n")
    #AP管理
    AP_mangle= driver.find_element_by_css_selector("#menu_T_Wireless_Management > a > span")
    print("---"+AP_mangle.text+"---")
    AP_mangle.click()
    time.sleep(3)
    # #在线AP
    # AP_online = driver.find_element_by_css_selector("#menu_S_INFORMATION_AP > a > span")
    # print("---"+AP_online.text+"---")
    # AP_online.click()
    #AP配置
    AP_set = driver.find_element_by_xpath(".//*[@id='menu_S_AC']/a/span")
    print("---"+AP_set.text+"---")
    AP_set.click()

    # 切换到AP信息管理 iframe 标签中
    iframe1 = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div/div[2]/iframe[2]")
    driver.switch_to.frame(iframe1)
    for i in range(1,500):
        # 进行ssid 名称配置
        try:
            ssid = driver.find_element_by_xpath(".//*[@id='template_cf_ssid']/tbody/tr[1]/td[3]")
            print("第%d次---"%i+"当前ssid为：",ssid.text)
            f.write("第%d次--"%i)
            f.write("当前ssid为：%s\n" %(ssid.text))
            ssid.click()
            #输入 ssid名称
            ssid_input = driver.find_element_by_xpath(".//*[@id='ssid_input']")
            a = random.randint(1,50)
            ssid_input.send_keys(str(a))
            driver.find_element_by_xpath(".//*[@id='INNER']/div[12]/div/div[2]/div/table/thead/tr/th[3]/div").click()
            time.sleep(1)
            #确定
            submit = driver.find_element_by_xpath(".//*[@id='SUBMIT_BTN']")
            submit.click()
            # time.sleep(3)
            time.sleep(90)
        except Exception as E:
            print(E)
    f.close()
    time.sleep(5)
    driver.quit()
if __name__ == '__main__':
    Ap_Config()