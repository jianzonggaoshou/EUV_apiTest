# coding=utf-8
import requests
from public import Login
import time
import random

url = "https://www.ewaypro.cn/euvtest/api/message/send/system.json"
payload0 = {'messageTitle': '消息规律测试0', 'messageContent': '消息规律测试0', 'messageType':'1'}
payload1 = {'messageTitle': '消息规律测试1', 'messageContent': '消息规律测试1', 'messageType':'1'}
payload2 = {'messageTitle': '消息规律测试2', 'messageContent': '消息规律测试2', 'messageType':'1'}
payload3 = {'messageTitle': '消息规律测试3', 'messageContent': '消息规律测试3', 'messageType':'1'}
payload4 = {'messageTitle': '消息规律测试4', 'messageContent': '消息规律测试4', 'messageType':'1'}
payload5 = {'messageTitle': '消息规律测试5', 'messageContent': '消息规律测试5', 'messageType':'1'}
payload6 = {'messageTitle': '消息规律测试6', 'messageContent': '消息规律测试6', 'messageType':'1'}
payload7 = {'messageTitle': '消息规律测试7', 'messageContent': '消息规律测试7', 'messageType':'1'}
payload8 = {'messageTitle': '消息规律测试8', 'messageContent': '消息规律测试8', 'messageType':'1'}
payload9 = {'messageTitle': '消息规律测试9', 'messageContent': '消息规律测试9', 'messageType':'1'}
payload_list = [payload0, payload1, payload2, payload3, payload4, payload5, payload6, payload7, payload8, payload9]

for kk in range(0, 100):
    kk = 1
    kk = kk + 1
    print (kk)
    for i in range(0, 10):
        time.sleep(30)
        r = requests.post(url=url, data=payload_list[i], cookies=Login.myCookies)
        print(r.text)
    time.sleep(600)


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
