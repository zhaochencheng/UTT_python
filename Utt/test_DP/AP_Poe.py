# -*- coding: utf-8 -*-
# @Time    : 2018/1/4 18:13
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : AP_Poe.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time
from Utt.test_DP.Login_ac import *
'''
对AC 系统管理---以太网供电口 进行开/关操作
'''

def AP_poe():
    '''将在线ap踢下线'''
    file = open("2.txt", "w")
    #登陆AC
    driver = webdriver.Chrome()
    driver.get("http://192.168.2.252")
    driver.maximize_window()
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
    #系统管理
    System_Managment = driver.find_element_by_xpath(".//*[@id='menu_M_System_Managment']/a/span")
    print("当前位置：",System_Managment.text)
    System_Managment.click()
    time.sleep(2)

    #以太网供电
    Poe_port = driver.find_element_by_xpath(".//*[@id='menu_M_System_Managment']/ul/li[9]/a/span")
    print("当前位置：",Poe_port.text)
    Poe_port.click()
    time.sleep(5)
    frame1 = driver.find_element_by_xpath("//*[@id='contentarea']/iframe[2]")
    driver.switch_to_frame(frame1)
    #Poe配置
    Poe_config = driver.find_element_by_xpath(".//*[@id='T_Poe_Config2']")
    print("当前位置：",Poe_config.text)
    Poe_config.click()
    time.sleep(5)
    try:


        for i in range(300):

            #接口poe状态
            Poe_statu =driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[2]/div")
            print("第%d次"%i)
            print("开始前 接口poe状态：",Poe_statu.text)

            file.writelines("-------------------\n")
            file.writelines(time.ctime())
            file.writelines("\n")
            file.writelines("第")
            file.writelines(str(i))
            file.writelines("次---")
            file.writelines("开始前--接口poe状态：")
            file.writelines(str(Poe_statu.text))
            file.writelines("\n")
            if Poe_statu.text == "on":
                # poe使能
                poe_j = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[9]")
                poe_j.click()
                time.sleep(1)

                POE_judge = driver.find_element_by_xpath(".//*[@id='judge_enable1']")
                POE_judge.click()
                Poe_close = driver.find_element_by_xpath(".//*[@id='judge_enable1']/option[2]")
                Poe_close.click()
                time.sleep(2)
                #修改poe状态的端口
                Poe_name = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                print(Poe_name.text)
                Poe_name.click()
                time.sleep(1)
                #确定按钮
                Submit = driver.find_element_by_xpath(".//*[@id='SUBMIT_BTN']")
                Submit.click()
                time.sleep(3)
                Poe_name_alter = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                Poe_statu1 = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[2]/div")
                print("处理后--接口%s"%(Poe_name_alter.text)+" poe状态：", Poe_statu1.text)
                file.writelines("处理后--接口")
                file.writelines(str(Poe_name_alter.text))
                file.writelines("--poe状态：")
                file.writelines(str(Poe_statu1.text))
                file.writelines("\n")
                # time.sleep(100)
            else:
                # poe使能
                poe_j1 = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[9]")
                poe_j1.click()
                time.sleep(1)

                POE_judge1 = driver.find_element_by_xpath(".//*[@id='judge_enable1']")
                POE_judge1.click()
                Poe_open = driver.find_element_by_xpath(".//*[@id='judge_enable1']/option[1]")
                Poe_open.click()
                time.sleep(2)
                # 修改poe状态的端口
                Poe_name1 = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                print(Poe_name1.text)
                Poe_name1.click()
                time.sleep(1)
                # 确定按钮
                Submit1 = driver.find_element_by_xpath(".//*[@id='SUBMIT_BTN']")
                Submit1.click()
                #类似刷新页面
                a = driver.find_element_by_xpath(".//*[@id='T_Poe_Info2']")
                a.click()
                time.sleep(2)
                Poe_config1 = driver.find_element_by_xpath(".//*[@id='T_Poe_Config2']")
                Poe_config1.click()
                time.sleep(4)
                Poe_name_alter1 = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                Poe_statu2 = driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[2]/div")
                print("处理后 接口%s"%(Poe_name_alter1.text)+" poe状态：", Poe_statu2.text)
                file.writelines("处理后--接口")
                file.writelines(str(Poe_name_alter1.text))
                file.writelines("--poe状态：")
                file.writelines(str(Poe_statu2.text))
                file.writelines("\n")
                time.sleep(100)
    except Exception as  E:
        print(E)

    time.sleep(5)
    driver.quit()



if __name__ == '__main__':
    AP_poe()