# coding=utf-8
import urllib
import cookielib
import urllib2


class Login:
    # 第一步先给出账户密码网址准备模拟登录
    def __init__(self):
        pass

    post_data = urllib.urlencode({
        'userName': '15609109999',
        'userPwd': '123456',
    })
    loginUrl = 'https://www.ewaypro.cn/euvtest/api/user/login.json'

    # 第二步模拟登陆并保存登录的cookie
    filename = 'cookie.txt'  # 创建文本保存cookie
    myCookies = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(myCookies))  # 定义这个opener，对象是cookie
    resultCookies = opener.open(loginUrl, post_data)
    myCookies.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
    print("login end")
