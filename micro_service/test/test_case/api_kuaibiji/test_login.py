# # coding:utf-8
# # !/user/bin/python
# import os
# import json
# import logging
# import base64, requests, time
# import unittest
# from test_case.base import Base
# from pyquery import PyQuery as pq
# from test.config.config import path_test_data, host
# from test_case.base_vars import vars
# from share.request_headers import headers
#
#
# logger = logging.getLogger('testlog')  # 获取dblog的日志配置
#
#
# payload = {}
# cookies = None
# csrf = ''
#
#
# class TestLogin(Base):
#
#     def __init__(self, *args, **kwargs):
#         super(TestLogin, self).__init__(*args, **kwargs)
#
#     def data(self):
#         """
#         测试数据
#         :return:
#         """
#         pass
#
#     def csrf(self):
#         """
#         测试 login
#         :return:
#         """
#         api = '/user/login'
#         url = host + api
#         r = vars.session.get(url)
#         content = r.content
#         cookies = r.cookies
#
#         e = pq(content)
#         csrf = e('meta[name="csrf-token"]').attr('content')
#
#         payload = {
#             "csrf_token": "{}".format(csrf),
#         }
#         vars.payload = payload
#         vars.cookies = cookies
#         vars.csrf = csrf
#         vars.session.headers.update({'X-CSRFToken': vars.csrf})
#         assert r.status_code == 200
#
#
#     def test_login(self):
#         """
#         登录
#         请求参数：
#         {
#           "username": str 必须 // 用户名
#             "password": str 必须 // 密码
#         }
#         返回参数：
#         """
#         self.csrf()
#         username = 'wangxin02@soovii.com'
#         # username = 'yangqian02@soovii.com'
#         passwd = '123456'
#
#         api = '/user/login'
#         url = host + api
#         d = {
#             "username": "{}".format(username),
#             "password": "{}".format(passwd),
#         }
#         params = {
#             'headers': headers,
#             'data': d,
#             'verify': False,
#             'cookies': vars.cookies,
#         }
#
#         r = vars.session.post(url, **params)
#         docstring = self.format_doc(self.test_login.__doc__.strip())
#         # content = json.dumps(json.loads(r.content), indent=2, ensure_ascii=False)
#         d = json.dumps(d, indent=2)
#
#         res = {
#             'filename': 'login.txt',
#             'api': api,
#             'method': 'post',
#             'req': d,
#             'response': '',
#             'folder': 'login',
#             'rewrite': False,
#             'remark': docstring,
#         }
#         self.output_text(**res)
#
#         assert r.status_code == 200
#
#
#
