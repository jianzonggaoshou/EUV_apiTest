# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/regulation/add.json"
payload0 = {'regulationName': '规章制度测试分页0', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload1 = {'regulationName': '规章制度测试分页1', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload2 = {'regulationName': '规章制度测试分页2', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload3 = {'regulationName': '规章制度测试分页3', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload4 = {'regulationName': '规章制度测试分页4', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload5 = {'regulationName': '规章制度测试分页5', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload6 = {'regulationName': '规章制度测试分页6', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload7 = {'regulationName': '规章制度测试分页7', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload8 = {'regulationName': '规章制度测试分页8', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
payload9 = {'regulationName': '规章制度测试分页9', 'createPersonName': '许臻', 'createDeptName':'研发部', 'implStartTime': '2017-10-23', 'regulationContent': '测试test1'}
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
