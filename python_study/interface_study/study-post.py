# -*- coding: utf-8 -*-
# @Time    : 2018/3/9 10:20
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : study-post.py
# @Software: PyCharm Community Edition
import requests
url = 'http://200.200.202.159:8080/rest/gadget/1.0/login'
body = {
'os_username':'zhao.chencheng',
    'os_password':'zhaochencheng'
}
h = {'Content-Type': 'application/x-www-form-urlencoded',
     'charset':'UTF-8',
'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0',
'Accept':'*/*',
'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
'Accept-Encoding': 'gzip, deflate',
'X-Requested-With': 'XMLHttpRequest'

     }
cookies = {'atlassian.xsrf.token':'BEDQ-ZFUO-20W9-W7OT|b0d48c7391480e762255423625e219a0b394895d|lout', 'JSESSIONID':'00C67998A6C90BA75F452D34558A0F29'
}
r = requests.post(url,data=body,headers=h,cookies=cookies)
print(r.text)