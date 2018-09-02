# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
from flask import request, session
from flask import Blueprint, render_template
import json
from rpc_client.notebook import NoteBookClient
from rpc_client.user import UserClient
from common.request_tool import send_failure, send_success

mod = Blueprint('notebook', __name__)


@mod.route('/notebook', methods=['GET'])
def user():
    args = request.args
    header = request.headers

    notebook_id = args.get('notebook_id', '')
    token = header.get('token', '')


    user_client = UserClient()
    user = user_client.user_by_id(notebook_id)
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
def notebook_add():
    pass



@mod.route('/notebook', methods=['DELETE'])
def notebook_delete():
    pass
