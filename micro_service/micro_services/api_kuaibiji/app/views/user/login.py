# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11
@desc:
"""
# import ipdb
from flask import request
from flask import Blueprint
from rpc_client.weixin import WeixinClient
from common.request_tool import send_failure, send_success
from common.constants import weixin_oauth_url, weixin_appid, weixin_secret

mod = Blueprint('user_login', __name__)


@mod.route('/login')
def login():
    args = request.args
    code = args.get('code', '')

    args = {
        'appid': weixin_appid,
        'secret': weixin_secret,
        'js_code': code,
        'grant_type': 'authorization_code',
    }
    data = WeixinClient().login(args)

    return send_success(data=data)
