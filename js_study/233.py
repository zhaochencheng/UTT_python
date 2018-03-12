# -*- coding: utf-8 -*-
# @Time    : 2018/3/7 17:23
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : 233.py
# @Software: PyCharm Community Edition
import document as document
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://cmsdev.app-link.org/alucard263096/startupclub/login")
time.sleep(3)
driver.find_element_by_name("login_id").send_keys("admin")
driver.find_element_by_name("password").send_keys("admin")
driver.find_element_by_class_name("btn-primary").click()
time.sleep(3)


# 进入i生活界面
driver.find_element_by_xpath("/html/body/div[1]/aside/section/ul/li[3]/a/i").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='mainsiderbar']/section/ul/li[3]/ul/li[2]/a").click()
time.sleep(3)

iframe = driver.find_element_by_class_name("cke_wysiwyg_frame")
driver.switch_to.frame(iframe)
time.sleep(3)
# driver.find_element_by_class_name("cke_reset").send_keys('123465')
driver.find_element_by_xpath("/html/body/p/br").send_keys("121")
# js = 'document.getItems("/html/body/p").innerHTML= "q23"'
# driver.execute_script(js)
# driver.switch_to.default_content()
