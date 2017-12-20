# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 9:34
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : http200.py
# @Software: PyCharm Community Edition

from urllib.request import urlopen

url = 'http://192.168.30.1'
# resp = urlopen(url)
# code = resp.getcode()
# print('the result is :', code)
def http200(Url):
    '''

    访问 URL ；输出http 状态码；
    查看访问状态
    '''
    url = Url
    resp = urlopen(url)
    code = resp.getcode()
    print('the result is :', code)
    print("%s"%url+"可以访问！")

if __name__ == '__main__':
    http200(url)