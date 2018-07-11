# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
from flask import Blueprint, render_template
mod = Blueprint('index', __name__)


@mod.route('/')
def index():
    return render_template('index.html')

