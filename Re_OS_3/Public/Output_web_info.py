# -*- coding: utf-8 -*-
# @Time    : 2018/2/1 16:20
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Output_web_info.py
# @Software: PyCharm Community Edition
from selenium import webdriver
import time
import unittest

class Output_info():
    def __init__(self,driver):
        self.driver = driver
    def output_content(self,config_name):
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
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
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

    def output_all(self):
        u'''将展示页面信息 输出'''

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

        for i in range(1, len(tr) + 1):
            # tr中 td个数;若该条没有vlan 配置,td数为1;  如果不比较,会导致定位不到元素,,而报错
            td = self.driver.find_elements_by_xpath(".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td" % i)
            if len(td) > 1:
                try:
                    name_rule = self.driver.find_element_by_xpath(
                        ".//*[@id='1']/div/div/div[1]/table/tbody/tr[%d]/td[3]/span" % i).text
                except BaseException as E:
                    pass

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
                # print("该 ‘ %s ’ 信息已全部输出 " % name_rule)
                print("*" * 30, '\n')

            else:
                # print("页面无信息！")
                break




'''
实例化：
Output_info(self.driver).output_content(behavior_rulename)

按上面方式 进行实例化调用


'''