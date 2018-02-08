# -*- coding: utf-8 -*-
# @Time    : 2018/1/5 13:08
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : test_003_AP_Poe.py
# @Software: PyCharm Community Edition
import unittest
from selenium import webdriver
import  time

class AP_Poe(unittest.TestCase):
    '''以太网供电口--开/关'''
    @classmethod
    def setUpClass(cls):
        print("只打开一次浏览器")
        cls.driver = webdriver.Chrome()
        cls.driver.get("http://192.168.2.252")
        cls.driver.maximize_window()
        cls.driver.find_element_by_css_selector("#username").clear()
        cls.driver.find_element_by_css_selector("#username").send_keys('admin')
        cls.driver.find_element_by_css_selector("#login_password").clear()
        cls.driver.find_element_by_css_selector("#login_password").send_keys("admin_default")
        code = input("enter code:")  # 验证码
        cls.driver.find_element_by_css_selector("#code").send_keys(code)
        cls.driver.find_element_by_css_selector("#loginIn").click()
        time.sleep(3)
        print(cls.driver.title)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        print("关闭浏览器")
    def setUp(self):
        print("\n再次打开浏览器")

    def tearDown(self):
        '''退出web 管理员登陆'''
        #切换到默认frame
        self.driver.switch_to_default_content()
        frame2 = self.driver.find_element_by_xpath("//*[@id='BODY']")
        #退出 按钮定位
        admin_exit = frame2.find_element_by_xpath(".//*[@id='test-top-right']/table/tbody/tr/td[6]/span/a/span")
        admin_exit.click()
        #接受弹窗
        a = self.driver.switch_to_alert()
        print("退出管理员弹窗内容：", a.text)
        a.accept()
        time.sleep(2)

    def test_AP_poe(self):
        '''对AC 系统管理---以太网供电口 进行开/关操作'''


        file = open("2.txt", "w")
        # 系统管理
        System_Managment = self.driver.find_element_by_xpath(".//*[@id='menu_M_System_Managment']/a/span")
        print("当前位置：", System_Managment.text)
        System_Managment.click()
        time.sleep(2)

        # 以太网供电
        Poe_port = self.driver.find_element_by_xpath(".//*[@id='menu_M_System_Managment']/ul/li[9]/a/span")
        print("当前位置：", Poe_port.text)
        Poe_port.click()
        time.sleep(5)
        frame1 = self.driver.find_element_by_xpath("//*[@id='contentarea']/iframe[2]")
        self.driver.switch_to_frame(frame1)
        # Poe配置
        Poe_config = self.driver.find_element_by_xpath(".//*[@id='T_Poe_Config2']")
        print("当前位置：", Poe_config.text)
        Poe_config.click()
        time.sleep(5)
        try:

            for i in range(200):

                # 接口poe状态
                Poe_statu = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[2]/div")
                print("------------**************---------------")
                print("第%d次" % i)
                print("开始前 接口poe状态：", Poe_statu.text)

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
                    poe_j = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[9]")
                    poe_j.click()
                    time.sleep(1)

                    POE_judge = self.driver.find_element_by_xpath(".//*[@id='judge_enable1']")
                    POE_judge.click()
                    Poe_close = self.driver.find_element_by_xpath(".//*[@id='judge_enable1']/option[2]")
                    Poe_close.click()
                    time.sleep(2)
                    # 修改poe状态的端口
                    Poe_name = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                    print(Poe_name.text)
                    Poe_name.click()
                    time.sleep(1)
                    # 确定按钮
                    Submit = self.driver.find_element_by_xpath(".//*[@id='SUBMIT_BTN']")
                    Submit.click()
                    time.sleep(3)
                    Poe_name_alter = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                    Poe_statu1 = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[2]/div")
                    print("处理后--接口%s" % (Poe_name_alter.text) + " poe状态：", Poe_statu1.text)
                    file.writelines("处理后--接口")
                    file.writelines(str(Poe_name_alter.text))
                    file.writelines("--poe状态：")
                    file.writelines(str(Poe_statu1.text))
                    file.writelines("\n")
                    # time.sleep(100)
                else:
                    # poe使能
                    poe_j1 = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[9]")
                    poe_j1.click()
                    time.sleep(1)

                    POE_judge1 = self.driver.find_element_by_xpath(".//*[@id='judge_enable1']")
                    POE_judge1.click()
                    Poe_open = self.driver.find_element_by_xpath(".//*[@id='judge_enable1']/option[1]")
                    Poe_open.click()
                    time.sleep(2)
                    # 修改poe状态的端口
                    Poe_name1 = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                    print(Poe_name1.text)
                    Poe_name1.click()
                    time.sleep(1)
                    # 确定按钮
                    Submit1 = self.driver.find_element_by_xpath(".//*[@id='SUBMIT_BTN']")
                    Submit1.click()
                    # 类似刷新页面
                    a = self.driver.find_element_by_xpath(".//*[@id='T_Poe_Info2']")
                    a.click()
                    time.sleep(2)
                    Poe_config1 = self.driver.find_element_by_xpath(".//*[@id='T_Poe_Config2']")
                    Poe_config1.click()
                    time.sleep(4)
                    Poe_name_alter1 = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[1]")
                    Poe_statu2 = self.driver.find_element_by_xpath(".//*[@id='poeconfig']/tbody/tr[1]/td[2]/div")
                    print("处理后 接口%s" % (Poe_name_alter1.text) + " poe状态：", Poe_statu2.text)
                    file.writelines("处理后--接口")
                    file.writelines(str(Poe_name_alter1.text))
                    file.writelines("--poe状态：")
                    file.writelines(str(Poe_statu2.text))
                    file.writelines("\n")
                    time.sleep(100)
        except Exception as  E:
            print(E)
        file.close()

        time.sleep(5)



if __name__ == '__main__':
    suit = unittest.TestSuite()
    suit.addTest(AP_Poe("test_AP_poe"))
    runner = unittest.TextTestRunner()
    runner.run(suit)