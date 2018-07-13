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

mod = Blueprint('notebook', __name__)


@mod.route('/notebook')
def user():
    args = request.args
    user_id = args.get('user_id', '')
    user_client = UserClient()
    user = user_client.user_by_id(user_id)
    udata = user.get('data')

    s = NoteBookClient()
    data = s.get_notebooks()

    if udata:
        s = NoteBookClient()
        data = s.get_notebooks()
        return send_success(data=data)
    else:
        return send_failure(msg='not user')


@mod.route('/notebook', methods=['POST'])
def add_notebook():
    pass
