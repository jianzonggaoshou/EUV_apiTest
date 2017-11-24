# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/defaultFlow/add.json"
payload0 = {'deptId': '20', 'nodesString': '技术组员'}
payload1 = {'deptId': '0', 'nodesString': '技术组员'}
payload2 = {'deptId': '0', 'nodesString': '技术组员'}
payload_list = [payload0, payload1, payload2]

for i in range(0, 3):
    r = requests.post(url=url, data=payload_list[i], cookies=Login.myCookies)
    print(r.text)

# r = requests.get(url=url, cookies=myCookies)
# result = r.json()
# print(r.text)
# print(r.status_code)
# print(result)
# # 第三步利用cookie请求访问另一个网址
# url = "http://172.16.40.240:8888/sitopeuv/api/room/user/list.json"
# r = requests.get(url=url, cookies=myCookies)
# print(r.text)
# print(r.status_code)
