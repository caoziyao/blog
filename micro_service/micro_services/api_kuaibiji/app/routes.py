# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""

from .views import mod_index
from .views import mod_user
from .views import mod_notebook

def register_blue(app):
    app.register_blueprint(mod_index, url_prefix='/')
    app.register_blueprint(mod_user, url_prefix='/user')
    app.register_blueprint(mod_notebook, url_prefix='/notebook')
