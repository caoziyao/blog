# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11
@desc:
"""

# import ipdb
from flask import request, session, current_app, abort
from flask import Blueprint, render_template, current_app, g
import json
from rpc_client.notebook import NoteBookClient
from rpc_client.user import UserClient
from common.request_tool import send_failure, send_success, login_required
from database import redis_client

mod = Blueprint('user_get_user', __name__)


@mod.route('/user_info')
# @login_required
def get_user():
    # 'oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
    args = request.args
    user_id = args.get('user_id', '')

    s = UserClient()
    user = s.user_by_id(user_id)

    user_data = user.get('data', '')
    if user_data:
        return send_success(data=user_data)
    else:
        return send_failure(msg='note user')
