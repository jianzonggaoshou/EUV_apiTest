# -*- coding: utf-8 -*-
import unittest
import cookielib
import requests
import urllib
import urllib2


class GetRoomListTest(unittest.TestCase):
    """查询配电室接口测试"""

    def setUp(self):
        print('test start...')
        # 第一步先给出账户密码网址准备模拟登录
        post_data = urllib.urlencode({
            'userName': '15609100803',
            'userPwd': '123456',
        })
        loginUrl = 'http://172.16.40.240:8888/sitopeuv/api/user/login.json'

        # 第二步模拟登陆并保存登录的cookie
        filename = 'cookie.txt'  # 创建文本保存cookie
        self.myCookies = cookielib.MozillaCookieJar(filename)  # 声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
        opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.myCookies))  # 定义这个opener，对象是cookie
        self.resultCookies = opener.open(loginUrl, post_data)
        self.myCookies.save(ignore_discard=True, ignore_expires=True)  # 保存cookie到cookie.txt中
        print("login end")

    def tearDown(self):
        print('test end...')

    def test_get_room_error(self):
        """配电室roomId为60，查询成功"""
        # 第三步利用cookie请求访问另一个网址
        url = "http://172.16.40.240:8888/sitopeuv/api/room/user/list.json"
        r = requests.get(url=url, cookies=self.myCookies)
        print(r.text)
        print(r.status_code)

        # # 断言
        result = r.json()
        print (result['errorCode'])
        # self.assertEqual(result['errorCode'], 0)
        # print (result['data'][0]['roomId'])
        # self.assertEqual(result['data'][0]['roomId'], 60)
        # print (result['data'][0]['roomName'])
        # self.assertEqual(result['data'][0]['roomName'], u'西咸新区B楼配电室-720测试')
        # print (result['data'][0]['roomRemark'])
        # self.assertEqual(result['data'][0]['roomRemark'], u'西咸新区B楼配电室-720测试')


if __name__ == '__main__':
    unittest.main()
