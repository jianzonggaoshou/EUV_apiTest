# coding=utf-8
import requests
from public import Login

url = "http://172.16.40.240:8888/sitopeuv/api/equipment/type/add.json"
payload0 = {'equipmentTypeName': '测试分页1', 'equipmentTypeRemark': '测试mark123'}
payload1 = {'equipmentTypeName': '测试分页2', 'equipmentTypeRemark': '测试mark123'}
payload2 = {'equipmentTypeName': '测试分页3', 'equipmentTypeRemark': '测试mark123'}
payload3 = {'equipmentTypeName': '测试分页4', 'equipmentTypeRemark': '测试mark123'}
payload4 = {'equipmentTypeName': '测试分页5', 'equipmentTypeRemark': '测试mark123'}
payload5 = {'equipmentTypeName': '测试分页6', 'equipmentTypeRemark': '测试mark123'}
payload6 = {'equipmentTypeName': '测试分页7', 'equipmentTypeRemark': '测试mark123'}
payload7 = {'equipmentTypeName': '测试分页8', 'equipmentTypeRemark': '测试mark123'}
payload8 = {'equipmentTypeName': '测试分页9', 'equipmentTypeRemark': '测试mark123'}
payload9 = {'equipmentTypeName': '测试分页10', 'equipmentTypeRemark': '测试mark123'}
payload10 = {'equipmentTypeName': '测试分页11', 'equipmentTypeRemark': '测试mark123'}
payload11 = {'equipmentTypeName': '测试分页12', 'equipmentTypeRemark': '测试mark123'}
payload12 = {'equipmentTypeName': '测试分页13', 'equipmentTypeRemark': '测试mark123'}
payload13 = {'equipmentTypeName': '测试分页14', 'equipmentTypeRemark': '测试mark123'}
payload14 = {'equipmentTypeName': '测试分页15', 'equipmentTypeRemark': '测试mark123'}
payload15 = {'equipmentTypeName': '测试分页16', 'equipmentTypeRemark': '测试mark123'}
payload_list = [payload0, payload1, payload2, payload3, payload4, payload5, payload6, payload7, payload8, payload9, payload10, payload11, payload12, payload13, payload14, payload15]

for i in range(3, 16):
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
