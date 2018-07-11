# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
from flask import request
from flask import Blueprint, render_template
import json
from rpc.notebook import NoteBookClient
from rpc.user import UserClient
from common.request_tool import send_failure, send_success

mod = Blueprint('user', __name__)


@mod.route('/user_info')
def user():
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    args = request.args
    user_id = args.get('user_id', '')
    s = UserClient()
    user = s.user_by_id(user_id)
    user_data = user.get('data', '')
    if user_data:
        return send_success(data=user_data)
    else:
        return send_failure(msg='no user')


@mod.route('/login')
def login():
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    args = request.args
    code = args.get('code', '')

    WeixinService().weixin_login(code)


    # s = UserClient()
    # user = s.user_by_id(user_id)
    # user_data = user.get('data', '')
    # if not user_data:
    #     return send_failure(msg='no user')


@mod.route('/logout')
def logout():
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    args = request.args
    user_id = args.get('user_id', '')
    s = UserClient()
    user = s.user_by_id(user_id)
    user_data = user.get('data', '')
    if not user_data:
        return send_failure(msg='no user')
