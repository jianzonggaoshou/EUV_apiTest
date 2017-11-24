# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/emergency/add.json"
payload0 = {'emergencyName': '紧急电话测试分页0', 'emergencyCall': '029-123456'}
payload1 = {'emergencyName': '紧急电话测试分页1', 'emergencyCall': '029-123456'}
payload2 = {'emergencyName': '紧急电话测试分页2', 'emergencyCall': '029-123456'}
payload3 = {'emergencyName': '紧急电话测试分页3', 'emergencyCall': '029-123456'}
payload4 = {'emergencyName': '紧急电话测试分页4', 'emergencyCall': '029-123456'}
payload5 = {'emergencyName': '紧急电话测试分页5', 'emergencyCall': '029-123456'}
payload6 = {'emergencyName': '紧急电话测试分页6', 'emergencyCall': '029-123456'}
payload7 = {'emergencyName': '紧急电话测试分页7', 'emergencyCall': '029-123456'}
payload8 = {'emergencyName': '紧急电话测试分页8', 'emergencyCall': '029-123456'}
payload9 = {'emergencyName': '紧急电话测试分页9', 'emergencyCall': '029-123456'}
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
