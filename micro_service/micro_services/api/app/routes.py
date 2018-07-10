# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""

from .views import index_mod

def register_blue(app):
    app.register_blueprint(index_mod, url_prefix='/')
