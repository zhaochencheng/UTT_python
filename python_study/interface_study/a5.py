# coding:utf-8

import requests

url = "http://127.0.0.1/zentao/user-login.html"

# 字典
body = {"account": "xxx",
        "psw": "111"
       }

h = {"Content-Type": "application/x-www-form-urlencoded"}

# application/json这种格式的body传json参数
r = requests.post(url, json=body, headers=h)




print(r.text)  # 返回文本格式
# 如果返回有乱码
print(r.content.decode("utf-8"))

# multipart/form-data 如果是文件上传，传file参数

