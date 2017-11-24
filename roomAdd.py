# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/room/add.json"
payload0 = {'roomName': 'ceshi测试0', 'roomType': '1', 'roomRemark': '备注test1'}
payload1 = {'roomName': 'ceshi测试1', 'roomType': '1', 'roomRemark': '备注test1'}
payload2 = {'roomName': 'ceshi测试2', 'roomType': '1', 'roomRemark': '备注test1'}
payload_list = [payload0, payload1, payload2]

for i in range(0, 3):
    r = requests.post(url=url, data=payload_list[i], cookies=Login.myCookies)
    print(r.text)

# r = requests.get(url=url, cookies=Login.myCookies)
# print(r.text)
# print(r.status_code)
# # 第三步利用cookie请求访问另一个网址
# url = "http://172.16.40.240:8888/sitopeuv/api/room/user/list.json"
# r = requests.get(url=url, cookies=myCookies)
# print(r.text)
# print(r.status_code)