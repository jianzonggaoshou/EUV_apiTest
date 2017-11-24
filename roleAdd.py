# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/role/add.json"
payload0 = {'roleName': '测试分页0', 'roleRemark': '测试mark123'}
payload1 = {'roleName': '测试分页1', 'roleRemark': '测试mark123'}
payload2 = {'roleName': '测试分页2', 'roleRemark': '测试mark123'}
payload3 = {'roleName': '测试分页3', 'roleRemark': '测试mark123'}
payload4 = {'roleName': '测试分页4', 'roleRemark': '测试mark123'}
payload5 = {'roleName': '测试分页5', 'roleRemark': '测试mark123'}
payload6 = {'roleName': '测试分页6', 'roleRemark': '测试mark123'}
payload7 = {'roleName': '测试分页7', 'roleRemark': '测试mark123'}
payload8 = {'roleName': '测试分页8', 'roleRemark': '测试mark123'}
payload9 = {'roleName': '测试分页9', 'roleRemark': '测试mark123'}
payload_list = [payload0, payload1, payload2, payload3, payload4, payload5, payload6, payload7, payload8, payload9]

for i in range(0, 10):
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