# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/bag/job/add.json"
payload0 = {'jobName': '作业包测试0', 'jobRemark': '测试mark123'}
payload1 = {'jobName': '作业包测试1', 'jobRemark': '测试mark123'}
payload2 = {'jobName': '作业包测试2', 'jobRemark': '测试mark123'}
payload3 = {'jobName': '作业包测试3', 'jobRemark': '测试mark123'}
payload4 = {'jobName': '作业包测试4', 'jobRemark': '测试mark123'}
payload5 = {'jobName': '作业包测试5', 'jobRemark': '测试mark123'}
payload6 = {'jobName': '作业包测试6', 'jobRemark': '测试mark123'}
payload7 = {'jobName': '作业包测试7', 'jobRemark': '测试mark123'}
payload8 = {'jobName': '作业包测试8', 'jobRemark': '测试mark123'}
payload9 = {'jobName': '作业包测试9', 'jobRemark': '测试mark123'}
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
