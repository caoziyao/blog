# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11
@desc:
"""
from .get_user_info import mod as mod_user_info
from .login import mod as mod_login
from .logout import mod as mod_logout


def register_blue_user(app):
    app.register_blueprint(mod_user_info, url_prefix='/api')
    app.register_blueprint(mod_login, url_prefix='/api')
    app.register_blueprint(mod_logout, url_prefix='/api')
