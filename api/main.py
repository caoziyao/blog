# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc: api 服务
"""
from app.config import option
from flask import Flask
from app.routes import register_blue


def make_app():
    app = Flask(__name__)
    register_blue(app)
    return app


def main():
    config = dict(
        port=option.port,
        host=option.host,
        debug=option.debug,
    )
    app = make_app()
    app.run(**config)


if __name__ == '__main__':
    main()
