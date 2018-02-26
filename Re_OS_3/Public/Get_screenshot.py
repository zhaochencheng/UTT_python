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
        # 获取当前路径
        cwd = os.getcwd()
        # cd 到Re_OS_3 的位置   ------局限性
        parent_path = os.path.dirname(os.path.dirname(cwd))
        print("上级目录为：", parent_path)
        nowTime = time.strftime("%Y%m%d.%H_%M_%S")
        # cd 到截图保存文件夹
        ScreenShot = parent_path + "\Screenshot\%s.png" % (string+nowTime)
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