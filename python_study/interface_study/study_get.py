
# @Time    : 2018/3/8 11:00
# @Author  : zhao.chencheng
# @Email   : 907779487@qq.com
# @File    : study_get.py
# @Software: PyCharm Community Edition
# coding:utf-8
import requests
# r = requests.get("http://www.cnblogs.com/yoyoketang/")
# print(r.status_code)
# print(r.text)
# #Get带参数params
# url = "http://www.cnblogs.com/mvc/blog/news.aspx "
# par = {"blogApp":"yoyoketang"}
# h = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0",
# "Cookie":"CNZZDATA3347352=cnzz_eid%3D448742801-1505732599-%26ntime%3D1513078685; UM_distinctid=15e94ce9f3ca24-07173fbc1846688-47554336-1fa400-15e94ce9f3db06; _ga=GA1.2.1075438819.1505800282; _gid=GA1.2.1297242079.1520478131"
# }
# r = requests.get(url,params=par,headers=h )
# print(r.text)
# r = requests.get("https://www.baidu.com/",verify=False)
# print(r.url)
# print(r.encoding) #编码
# print(r.content) #获取返回内容（自动解码zip）
# print(r.headers)
# print(r.cookies)
# r = requests.get("http://200.200.202.159:8080/secure/Dashboard.jspa")
# print(r.url)
# print(r.status_code)
# print(r.text)
# url = "http://200.200.202.159:8080/rest/webResources/1.0/resources"
# # r1 = requests.post()
# r = requests.get("https://github.com/timeline.json",stream=True)
# print(r.text)
# print(r.encoding)
# # print(r.url)
# # payload = {'key1':'value','key2':'value2'}
# # r = requests.get("http://httpbin.org/get",params=payload)
# # print(r.url)
# # print(r.content)
# # from  PIL import Image
# # from io import BytesIO
# # i = Image.open(BytesIO(r.content))
# # print(r.json())
# print(r.raw)
# # print(r.raw.read(1))
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent':'my-app/0.0.1'}
# r = requests.get(url,headers=headers)
# print(r.headers)
# print(r.text)
# payload = {'key1':'value1','key2':'value2'}
# payload = (('key1','value1'),('key1','value2'))
# r = requests.post("http://httpbin.org/post",data=payload)
# print(r.text)
r = requests.get('https://api.github.com/user',auth=('user','pass'))
print(r.status_code)
print(r.headers['content-type'])