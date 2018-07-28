# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
import requests
import json
from proto import weixin_pb2
from proto import weixin_pb2_grpc
from common.constants import weixin_oauth_url, weixin_appid, weixin_secret


def data_to_fe(data):
    d = {}
    if data:
        d['openid'] = data.get('openid', '')
        d['session_key'] = data.get('session_key', '')
        d['unionid'] = data.get('unionid', '11')
    return d


def login(request, context):
    """ 登录
    """
    print('========ddd=====')
    metadata = dict(context.invocation_metadata())

    appid = request.appid
    secret = request.secret
    js_code = request.js_code
    grant_type = request.grant_type

    url = weixin_oauth_url
    url_args = {
        'appid': appid,
        'secret': secret,
        'js_code': js_code,
        'grant_type': grant_type,
    }
    r = requests.get(url, params=url_args)

    print('========rrrrrrrrr=====', r)
    data = r.content.decode('utf-8')
    if data:
        data = json.loads(data)
        data = data_to_fe(data)

    return weixin_pb2.ResponseWeixinLogin(**data)
