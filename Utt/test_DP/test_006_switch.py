# -*- coding: utf-8 -*-
# @Time    : 2018/2/7 20:25
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_006_switch.py
# @Software: PyCharm Community Edition
import unittest
from selenium import webdriver
import  time
class Switch(unittest.TestCase):
    u'''对交换机端口进行控制'''
    @classmethod
    def setUpClass(cls):
        print("只打开一次浏览器")
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://192.168.2.254")
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(10)
        username = cls.driver.find_element_by_id("user")
        username.clear()
        username.send_keys("admin")
        pwd = cls.driver.find_element_by_id("pass")
        pwd.clear()
        pwd.send_keys("admin_default")
        login = cls.driver.find_element_by_id("btn_login")
        login.click()
        time.sleep(2)


    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("关闭浏览器")
    def setUp(self):
        print("\n再次打开浏览器")

    def tearDown(self):
        '''退出web 管理员登陆'''
        pass
    def test_switch(self):

        vlan = self.driver.find_element_by_xpath("//*[@id='introMainMenu']/div[2]")
        vlan.click()
        print("当前位置：",vlan.text)
        time.sleep(2)
        #管理vlan
        vlanmem = self.driver.find_element_by_link_text("管理VLAN")
        vlanmem.click()
        print("当前位置：",vlanmem.text)
        frame1 = self.driver.find_element_by_xpath("/html/body/table/tbody/tr/td[2]/iframe")
        # "/html/body/table/tbody/tr/td[2]/iframe"
        self.driver.switch_to.frame(frame1)
        time.sleep(2)
        frame2 = self.driver.find_element_by_xpath("/html/body/iframe")
        self.driver.switch_to.frame(frame2)
        time.sleep(2)

        # # 从这 加循环
        for i in range(1,240):
            #编辑  定位的第二栏
            editlist = self.driver.find_elements_by_xpath(".//button[@class='edit']")
            edit = editlist[8]
            # "/html/body/div[1]/div/table/tbody/tr[2]/td[6]/button[1]"
            edit.click()
            time.sleep(2)
            #选择port
            port = self.driver.find_element_by_xpath("//*[@id='div_ports']/div/div/table/tbody/tr[1]/td[2]/div")
            port.click()
            time.sleep(3)

            #点击保存
            save = self.driver.find_element_by_id("btnUpdate")
            save.click()
            time.sleep(2)
            #接受 浏览器 弹窗
            alert = self.driver.switch_to.alert
            alert.accept()
            time.sleep(2)
            #输出 刚才修改后 vlan下的接口
            portList = self.driver.find_element_by_xpath("//*[@id='vlan_table']/tr[9]/td[5]")
            print("第%d次修改"%i)
            print("端口列表为：",portList.text)
            print("当前时间：",time.ctime())
            time.sleep(150)






if __name__ == '__main__':
    unittest.main()