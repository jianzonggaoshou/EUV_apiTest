# -*- coding: utf-8 -*-
import cookielib
import requests
import urllib
import urllib2

# url = "http://172.16.40.240:8888/sitopeuv/api/user/login.json"
# headers = {"Content-Type": "application/json"}
# data = {"userName": "yanxin",
# 		"userPwd": "123456",}
# r = requests.post(url=url, json=data, headers=headers)
# response = r.text
# print(data)
# print(r.text)
# print(r.status_code)
# print(1)
#
# # 断言
# url = "http://172.16.40.240:8888/sitopeuv/api/role/add.json"
# headers = {"Content-Type": "application/json"}
# data = {"roleName": "xuzhen",
# 		"roleRemark": "123",}
# r = requests.post(url=url, json=data, headers=headers)
# response = r.text
# print(data)
# print(r.text)
# print(r.status_code)
# print(2)

# 第一步先给出账户密码网址准备模拟登录
postdata = urllib.urlencode({
	'userName': 'biandongfeng',
	'userPwd': '12345678'  # 密码这里就不泄漏啦，嘿嘿嘿
})
loginUrl = 'http://172.16.40.240:8888/sitopeuv/api/user/login.json'  # 登录教务系统的URL，成绩查询网址

# 第二步模拟登陆并保存登录的cookie
filename = 'cookie.txt'  # 创建文本保存cookie
mycookie = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(mycookie))  # 定义这个opener，对象是cookie
result = opener.open(loginUrl, postdata)
mycookie.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中

# 第三步利用cookie请求访问另一个网址，教务系统总址

url = "http://172.16.40.240:8888/sitopeuv/api/role/add.json"
headers = {"Content-Type": "application/json"}
data = {"roleName": "xuzhen",
		"roleRemark": "123",}
r = requests.post(url=url, json=data, headers=headers, cookies=mycookie)
response = r.text
print(data)
print(r.text)
print(r.status_code)
