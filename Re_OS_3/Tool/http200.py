# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 9:34
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : http200.py
# @Software: PyCharm Community Edition

from urllib.request import urlopen

url = 'http://www.baidu.com'
url1 = 'http://www.163.com'
url2 = 'http://www.utt.com.cn'
url3 = 'http://192.168.2.104'
# resp = urlopen(url)
# code = resp.getcode()
# print('the result is :', code)
class httpcode():
    def http200(self,Url):
        '''
        访问 URL ；输出http 状态码；
        查看访问状态
        这个加了异常捕获，不会产生中断
        '''
        try:
            for i in range(1, 2):
                url = Url
                resp = urlopen(url)
                code = resp.getcode()
                # print('the result is :', code)
                # print("%s"%url+"可以访问！")
                if code == 200:
                    print("%s" % url + "可以访问！")
                else:
                    continue
        except Exception as  E:
            print(E)
            if E:
                print("无法访问该%s 地址！"%url)
            else:
                raise BaseException("功能不生效")

    def http200ok(self,Url):
        '''
       访问 URL ；输出http 状态码；
       查看访问状态
       这个未加异常捕获，无法访问；程序就会报错
       '''
        resp = urlopen(Url)
        code = resp.getcode()
        if code == 200:
            print("%s" % url + "可以访问！")
        else:
            pass
            # continue
        # for i in range(1, 2):
        #     url = Url
        #     resp = urlopen(url)
        #     code = resp.getcode()
        #     # print('the result is :', code)
        #     # print("%s"%url+"可以访问！")
        #     if code == 200:
        #         print("%s" % url + "可以访问！")
        #     else:
        #         continue

#
if __name__ == '__main__':
    # httpcode().http200(url)
    httpcode().http200ok("http://" + "www.163.com")

# http200(url2)
