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
from micro_services.user.database import UserManager
from common.constant import weixin_oauth_url, weixin_appid, weixin_secret


def data_to_fe(user):
    d = {}
    if user:
        d['userId'] = user.get('user_id', '1')
        d['updateTime'] = user.get('update_time', '2')
        d['createTime'] = user.get('create_time', '3')
        d['userName'] = user.get('user_name', '4')
    return d


def login(request, context):
    """ 登录
    """
    metadata = dict(context.invocation_metadata())
    print('metadata', metadata)

    code = request.code

    url = weixin_oauth_url
    url_args = {
        'appid': weixin_appid,
        'secret': weixin_secret,
        'js_code': code,
        'grant_type': 'authorization_code',
    }
    r = requests.get(url, url_args=url_args)
    data = r.content
    res = {
        'data': data
    }

    return weixin_pb2.ResponseWeixinLogin(**res)
