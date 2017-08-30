# -*- coding: utf-8 -*-
import cookielib
import requests
import urllib
import urllib2

# 第一步先给出账户密码网址准备模拟登录
postData = urllib.urlencode({
	'userName': 'biandongfeng',
	'userPwd': '123456',
})
loginUrl = 'http://172.16.40.249:8080/sitopeuv/api/user/login.json'

# 第二步模拟登陆并保存登录的cookie
filename = 'cookie.txt'  # 创建文本保存cookie
myCookies = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(myCookies))  # 定义这个opener，对象是cookie
result = opener.open(loginUrl, postData)
myCookies.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
print("login end")

# 第三步利用cookie请求访问另一个网址

url = "http://172.16.40.249:8080/sitopeuv/api/room/user/list.json"
r = requests.get(url=url, params={'roomId': '1'}, cookies=myCookies)
print(r.text)
print(r.status_code)
print("123....")

# 断言
result1 = r.json()
print (result1['data'][0]['roomId'])

assert result1['data'][0]['roomId'] == 61
