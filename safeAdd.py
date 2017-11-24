# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/bag/security/add.json"
payload0 = {'securityName': 'ceshi测试0', 'securityRemark': '测试mark123'}
payload1 = {'securityName': 'ceshi测试1', 'securityRemark': '测试mark123'}
payload2 = {'securityName': 'ceshi测试2', 'securityRemark': '测试mark123'}
payload3 = {'securityName': 'ceshi测试3', 'securityRemark': '测试mark123'}
payload4 = {'securityName': 'ceshi测试4', 'securityRemark': '测试mark123'}
payload5 = {'securityName': 'ceshi测试5', 'securityRemark': '测试mark123'}
payload6 = {'securityName': 'ceshi测试6', 'securityRemark': '测试mark123'}
payload7 = {'securityName': 'ceshi测试7', 'securityRemark': '测试mark123'}
payload8 = {'securityName': 'ceshi测试8', 'securityRemark': '测试mark123'}
payload9 = {'securityName': 'ceshi测试9', 'securityRemark': '测试mark123'}
payload_list = [payload0, payload1, payload2, payload3, payload4, payload5, payload6, payload7, payload8, payload9]

for i in range(0, 10):
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