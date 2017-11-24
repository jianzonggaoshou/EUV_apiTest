# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/user/add.json"
payload0 = {'userName': 'test3000', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload1 = {'userName': 'test3001', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload2 = {'userName': 'test3002', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload3 = {'userName': 'test3003', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload4 = {'userName': 'test3004', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload5 = {'userName': 'test3005', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload6 = {'userName': 'test3006', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload7 = {'userName': 'test3007', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload8 = {'userName': 'test3008', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload9 = {'userName': 'test3009', 'userPwd': '123456', 'realName': '测试分页', 'userType':'2', 'roleIds': '99'}
payload_list = [payload0, payload1, payload2, payload3, payload4, payload5, payload6, payload7, payload8, payload9]

for i in range(3, 10):
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