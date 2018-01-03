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
def http200(Url):
    '''

    访问 URL ；输出http 状态码；
    查看访问状态
    '''
    try:
        j = 0
        for i in range(1, 2):
            url = Url
            resp = urlopen(url)
            code = resp.getcode()
            # print('the result is :', code)
            # print("%s"%url+"可以访问！")
            if code == 200:
                j = j+1
                print("%s" % url + "可以访问！"+'%d'%j)
            else:
                continue
        # print("the result is %d"%j)
    except Exception as  E:
        print(E)

#
# if __name__ == '__main__':
#
#         # http200(url3)
#         http200(url1)
http200(url2)
