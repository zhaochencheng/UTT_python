# coding:utf-8

import requests

url = "http://127.0.0.1/zentao/user-login.html"

body = {"account": "admin",
        "password": "1e10adc3949ba59abbe56e057f20f883e",
        # "keepLogin[]": "on",
        "referer": "http://127.0.0.1/zentao/my/"}

h = {"Content-Type": "application/x-www-form-urlencoded"}

# application/x-www-form-urlencoded这种格式的body传data参数
r = requests.post(url, data=body, headers=h)

print(r.text)  # 返回文本格式
# 如果返回有乱码
print(r.content.decode("utf-8"))



