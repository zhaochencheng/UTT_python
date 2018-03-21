# coding=utf-8 
import unittest

from selenium.webdriver.support.ui import Select

from Autotest_2018.public_script.function_public import *


class 静态映射_TCP80(unittest.TestCase):
  
    #class静态参数
    #
    #配置参数获取
    #
    Wan_ip = get_data("wan_Config","static_ip")
    rule_name = get_data("nat_fwd","NAT_rule_name")
    bind_eth = get_data("nat_fwd","NAT_rule_ethbind")
    bind_ip = get_data("nat_fwd","NAT_rule_ip")        
    rule_protol = get_data("nat_fwd","NAT_rule_protol")
    rule_portfrom_in = get_data("nat_fwd","NAT_rule_portfrom_in")
    rule_portend_in = get_data("nat_fwd","NAT_rule_portend_in")
    rule_portfrom_out = get_data("nat_fwd","NAT_rule_portfrom_out")
    rule_portend_out = get_data("nat_fwd","NAT_rule_portend_out")

    def setUp(self):
        pass 

    def tearDown(self):
        pass

    def test_01_端口映射配置(self):
        #
        #vlan 配置
        #
        #vlan_config(2,"2",1,"2_3_4")
        #
        #登录web页面
        #
        driver = Login_web()
        driver.implicitly_wait(10)

        #
        #配置固定IP地址上网
        #
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
        driver.find_element_by_link_text(u"端口映射").click()
        driver.find_element_by_id("add").click()
        for i in range(1,10):
            flag = True
            try:
                driver.find_element_by_name("IDs")
            except:
                flag=False
            time.sleep (1)
            if i==9:
                self.fail()
                driver.quit()
                return
            if flag:
                driver.find_element_by_name("IDs").clear()
                driver.find_element_by_name("IDs").send_keys(self.rule_name)
                driver.find_element_by_name("IPs").clear()
                driver.find_element_by_name("IPs").send_keys(self.bind_ip)
                Select(driver.find_element_by_name("Protocols")).select_by_visible_text(self.rule_protol)
                driver.find_element_by_name("inS").clear()
                driver.find_element_by_name("inS").send_keys(self.rule_portfrom_in)
                driver.find_element_by_name("outS").clear()
                driver.find_element_by_name("outS").send_keys(self.rule_portfrom_out)
                driver.find_element_by_id("save").click()
                return

    def test_02_测试Lan方向http访问(self):
        #
        #测试打开网页
        #
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(10) 

        self.driver.get("http://" + self.bind_ip + "/baidu_test.html")  
        try:  
            assert '百度一下，你就知道' in self.driver.title
            print ('内网访问http服务器 pass！')  
        except Exception as e:  
            print ('内网访问http服务器 fail！')  
            self.fail()
        time.sleep(1)
        self.driver.quit()

    def test_03_测试NAT回环访问(self):
        #
        #测试打开网页
        #
        self.driver = webdriver.Chrome()
        self.driver.get("http://" + self.Wan_ip + ":" + self.rule_portfrom_out + "/baidu_test.html")  
        try:  
            assert '百度一下，你就知道' in self.driver.title
            print ('NAT回环访问http服务器 pass！')  
        except Exception as e:  
            print ('NAT回环访问http服务器 fail！')  
            self.fail()
        time.sleep(1)
        self.driver.quit()

    def test_04_测试WAN方向http访问(self):
        #
        #测试打开网页
        #
        self.driver = webdriver.Chrome()
        self.driver.get("http://" + self.Wan_ip + ":" + self.rule_portfrom_out + "/baidu_test.html")  
        try:  
            assert '百度一下，你就知道' in self.driver.title
            print ('外网访问http服务器 pass！')  
        except Exception as e:  
            print ('外网访问http服务器 fail！')  
            self.fail()
        time.sleep(1)
        self.driver.quit()


class 静态映射_UDP69(unittest.TestCase):  
  
    #class静态参数
    #
    #配置参数获取
    #
    Wan_ip = get_data("wan_Config","static_ip")
    rule_name = get_data("nat_fwd","NAT_rule_name2")
    bind_eth = get_data("nat_fwd","NAT_rule_ethbind")
    bind_ip = get_data("nat_fwd","NAT_rule_ip")        
    rule_protol = get_data("nat_fwd","NAT_rule_protol2")
    rule_portfrom_in = get_data("nat_fwd","NAT_rule_portfrom_in2")
    rule_portend_in = get_data("nat_fwd","NAT_rule_portend_in2")
    rule_portfrom_out = get_data("nat_fwd","NAT_rule_portfrom_out2")
    rule_portend_out = get_data("nat_fwd","NAT_rule_portend_out2")

    def setUp(self):
        pass 

    def tearDown(self):
        pass

    def test_01_端口映射配置(self):
        #
        #vlan 配置
        #
        #vlan_config(2,"2",1,"2_3_4")
        #
        #登录web页面
        #
        driver = Login_web()
        driver.implicitly_wait(10)

        #
        #配置固定IP地址上网
        #
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[3]/div/h4/span").click()
        driver.find_element_by_link_text(u"端口映射").click()
        driver.find_element_by_id("add").click()
        for i in range(1,10):
            flag = True
            try:
                driver.find_element_by_name("IDs")
            except:
                flag=False
            time.sleep (1)
            if i==9:
                self.fail()
                driver.quit()
                return
            if flag:
                driver.find_element_by_name("IDs").clear()
                driver.find_element_by_name("IDs").send_keys(self.rule_name)
                driver.find_element_by_name("IPs").clear()
                driver.find_element_by_name("IPs").send_keys(self.bind_ip)
                Select(driver.find_element_by_name("Protocols")).select_by_visible_text(self.rule_protol)
                driver.find_element_by_name("inS").clear()
                driver.find_element_by_name("inS").send_keys(self.rule_portfrom_in)
                driver.find_element_by_name("outS").clear()
                driver.find_element_by_name("outS").send_keys(self.rule_portfrom_out)
                driver.find_element_by_id("save").click()
                return

    def test_02_测试Lan方向tftp下载(self):
        #
        #测试tftp下载
        #
        flag = tftpdown_test(self.bind_ip)
        if flag == 1 :
            print("tftp下载文件测试 pass！")
        else:
            print("tftp下载文件测试 fail！")

    def test_03_测试NAT回环下载(self):
        #
        #测试tftp下载
        #
        flag = tftpdown_test(self.Wan_ip)
        if flag == 1 :
            print("tftp下载文件测试 pass！")
        else:
            print("tftp下载文件测试 fail！")

    def test_04_测试WAN方向tftp下载(self):
        #
        #测试tftp下载
        #
        flag = tftpdown_test(self.Wan_ip)
        if flag == 1 :
            print("tftp下载文件测试 pass！")
        else:
            print("tftp下载文件测试 fail！")


if __name__ == '__main__':  
    unittest.main()  