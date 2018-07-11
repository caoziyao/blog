# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc: api 服务
"""
from config import option
from flask import Flask
from .app.routes import register_blue

app = Flask(__name__)
register_blue(app)


def app_config():
    config = dict(
        port=option.api_port,
        host=option.api_host,
        debug=option.debug,
    )
    return config


def main():
    config = app_config()
    app.run(**config)


if __name__ == '__main__':
    main()
