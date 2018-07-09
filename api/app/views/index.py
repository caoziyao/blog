# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
from flask import Blueprint, render_template
import json
from app.service.notebook import NoteBookService
from app.service.user import UserService

mod = Blueprint('index', __name__)

@mod.route('/')
def index():
    return render_template('index.html')


@mod.route('/user')
def user():
    s = UserService()
    data = s.user_by_id('oMNol0Yk9XeI_0jHsYuFgFsQ2h6s')
    return json.dumps(data)


@mod.route('/notebook')
def notebook():
    s = NoteBookService()
    data = s.get_notebooks()

    return json.dumps(data)
