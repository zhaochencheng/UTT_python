# -*- coding:utf-8 -*-
import configparser
import os.path



#
#函数作用：从参数文件中获取参数值
#参数说明：config_fdir 需要获取参数的目录名称
#          config_data 需要获取参数的名称
#          config_file 参数文件的名称
#
from selenium import webdriver


def get_data(config_fdir,config_data,config_file="/Config/config.ini"):

    config = configparser.ConfigParser()
    file_path = os.path.abspath(os.path.join(os.path.realpath(__file__), "../.."))   + config_file
    config.read(file_path)
    data = config.get(config_fdir, config_data)
    #print(config_data + ": %s" % data)
    return data

def set_date(config_fdir,config_data,value_data,config_file="/Config/config.ini"):
    config = configparser.ConfigParser()
    file_path = os.path.abspath(os.path.join(os.path.realpath(__file__), "../..")) + config_file
    config.read(file_path)
    config.set(config_fdir,config_data,value_data)
    with open(file_path, 'w+') as f:
        config.write(f)
    # print(config_data + ": %s" % data)

#
#函数作用：登录被测设备的UI
#参数说明：     URL 被测设备UI登录IP地址
#          username 被测设备UI登录的用户名
#            passwd 被测设备UI登录的密码
#
web_URL = get_data("server_para","Server_url")
web_username = get_data("server_para","Login_user")
web_passwd = get_data("server_para","Login_passwd")

def Login_web(URL=web_URL,username=web_username,passwd=web_passwd):

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)    
    driver.get(URL)
    driver.find_element_by_name("username").clear()
    driver.find_element_by_name("username").send_keys(username)
    driver.find_element_by_name("pwd").clear()
    driver.find_element_by_name("pwd").send_keys(passwd)
    driver.find_element_by_id("login_btn").click()
    # 最大化浏览器窗口 方便截图完整
    driver.maximize_window()
    return driver


#
#函数作用：配置交换机的vlan
#参数说明：source_vlan 操作的vlan编号
#            vlan_port 操作端口号，多个端口号用“_”连接
#            switch_ip 交换机UI的IP地址
#
def vlan_config(source_vlan,vlan_port,source_vlan2,vlan_port2,switch_ip="192.168.1.254"):

    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    port_id = vlan_port.split("_")
    driver.get("http://admin:admin@" + switch_ip)

    driver.switch_to.frame("leftMenu")

    driver.find_element_by_xpath("//span[@onclick='markActive(3,this)']").click()
    driver.find_element_by_link_text("VLAN").click()

    driver.switch_to.parent_frame()
    driver.switch_to.frame("main")
    driver.switch_to.frame("frame12")
    driver.find_element_by_link_text(str(source_vlan)).click()

    driver.switch_to.parent_frame()
    for i in range(0,len(port_id)):
        driver.find_element_by_id("chkPort" + str(eval(port_id[i]) - 1)).click()
    driver.find_element_by_xpath(u"(//input[@value='保存'])[2]").click()
    
    if source_vlan2 == 0 and vlan_port2 == "0":
        pass
    else:
        #driver.switch_to.parent_frame()
        #driver.switch_to.frame("main")
        driver.switch_to.frame("frame12")
        port_id2 = vlan_port2.split("_")
        driver.find_element_by_link_text(str(source_vlan2)).click()
        driver.switch_to.parent_frame()
        for i in range(0,len(port_id2)):
            driver.find_element_by_id("chkPort" + str(eval(port_id2[i]) - 1)).click()
        driver.find_element_by_xpath(u"(//input[@value='保存'])[2]").click()

    driver.quit()

#
#函数作用：创建结果文件目录，返回html格式的结果文件名
#参数说明：log_dir log文件的相对目录
#
def mklog_file(log_dir="../../log/run_report/"): 

    day=time.strftime("%Y-%m-%d")
    log_path = os.path.abspath(os.path.join(os.path.realpath(__file__), log_dir)) + "\\" + day 
    
    if not os.path.exists(log_path):
        os.makedirs(log_path)
        
    second = time.strftime("%H_%M_%S")
    log_file = log_path + "\\" + day + " " + second + ".html" 
    return log_file


#
#函数作用：telnet进入设备，返回输出信息
#参数说明：command 输入的命令
#           strand 查找的内容
#               ip 被测设备的IP地址
#         username 被测设备的用户名
#         password 被测设备的密码
#        navpromot 命令停止标记位
#             port 登录的端口
#        timeout   登录超时时间
#
def telnet(command,strand,ip="192.168.1.1",username="admin",password="admin",navpromot="#",port=60023,timeout=30):

    telnet=telnetlib.Telnet(ip,port=port,timeout=timeout)
    #telnet.set_debuglevel(3)

    #telnet登录
    telnet.read_until("login: ".encode())
    telnet.write(username.encode() + '\n'.encode())  
    telnet.read_until("Password: ".encode())
    telnet.write(password.encode() +'\n'.encode())
    telnet.read_until(navpromot.encode())

    #输入命令
    telnet.write(command.encode() + '\n'.encode())
    time.sleep(2)
    telnet.write('exit\n'.encode())

    #数据分析
    data = telnet.read_until(navpromot.encode()).decode()
    telnet_data = data.split("\r\n")
    for i in range(0,len(telnet_data)):
        t = telnet_data[i].find(strand)
        if t > 0 :
            return t
    

#
#函数作用：判断文件是否存在，文件是否有数据
#参数说明：file_path 文件的相对目录，在tools\tftpd目录下
# os.remove(file)
def tftpdown_test(ip_addr,file_name='Capture.pkt'):
    down_path = os.path.abspath(os.path.join(os.path.realpath(__file__), "../../tmp"))
    file_path = down_path + '\\' + file_name
    if os.path.exists(file_path):
        os.chmod( file_path, stat.S_IWRITE)
        os.remove(file_path)

    down_result = os.system('tftp -i ' + ip_addr + ' get ' + file_name + ' ' + file_path)
    if not os.path.exists(file_path):
        return 0
    else:
        file_size = os.path.getsize(file_path)
        print(file_size)
        if file_size > 0 :
            return 1
        else:
            return 0






