# -*- coding: utf-8 -*-
# @Time    : 2018/2/26 10:24
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : Get_screenshot.py
# @Software: PyCharm Community Edition
import os
import time
from selenium import webdriver
class Get_Screenshot():

    # 截图 放在Screenshot 文件夹中
    def __init__(self,driver):
        self.driver = driver
    def get_screenshot(self,string):
        #设置 截图路径
        png = self.cd_screenshot_path(string)
        self.driver.get_screenshot_as_file(png)
    def cd_screenshot_path(self,string):
        # 当前脚本所在文件真实路径
        cur_path = os.path.realpath(__file__)
        # cur_path = r"G:\github\UTT_python\Re_OS_3\test_all\test_netConfig\test_DDNS.py"
        # print(cur_path)
        while 1:
            path = []
            if os.path.isdir(cur_path):
                list = os.listdir(cur_path)
                for i in list:
                    # print(i,"-",type(i))
                    if i != "Screenshot":
                        pass
                    else:
                        path = cur_path
                        # print("path:-----", path)
                        break
                if len(path) != 0:
                    break
                cur_path = os.path.dirname(cur_path)
                # print(cur_path)
            elif os.path.isfile(cur_path):
                print(cur_path,"is file")
                cur_path = os.path.dirname(cur_path)
        nowTime = time.strftime("%Y%m%d.%H_%M_%S")
        # cd 到截图保存文件夹
        ScreenShot = path + "\Screenshot\%s.png" % (nowTime+'_'+string)
        print('截图保存文件夹路径为:', ScreenShot)
        #返回 截图文件的路径
        return ScreenShot

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get("http://192.168.2.1")
    driver.implicitly_wait(10)
    Get_Screenshot(driver).get_screenshot("test")
    time.sleep(2)
    driver.quit()
    # 当前脚本所在文件真实路径
    # cur_path = os.path.dirname(os.path.realpath(__file__))
    # print(cur_path)
    # list = os.listdir(cur_path)
    # print(list)
    # cur_path = os.path.dirname(cur_path)
    # print(cur_path)
    # list1 = os.listdir(cur_path)
    # print(list1[7])
    # print(type(list1[7]))
    # print(type("Screenshot"))


    # # 获取当前路径
    # cwd = os.getcwd()
    # # cd 到Re_OS_3 的位置   ------局限性
    # parent_path = os.path.dirname(os.path.dirname(cur_path))
    # print("上级目录为：", parent_path)
    # nowTime = time.strftime("%Y%m%d.%H_%M_%S")
    # # cd 到截图保存文件夹
    # ScreenShot = parent_path + "\Screenshot\%s.png" % (nowTime+'_'+string)
    # print('截图保存文件夹路径为:', ScreenShot)