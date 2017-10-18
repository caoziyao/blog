# coding: utf-8

import os
from flask import Flask
from app.route.index import app as route_index
from app.route.edit import app as route_edit
from app.route.article import app as route_page
from app.route.hot_spot import app as route_hot_spot
from app.handlers import config
from config.constant import static_folder

app = Flask(__name__, static_url_path=static_folder)

def register_route():
    """
    注册蓝图
    :return:
    """
    app.register_blueprint(route_index)
    app.register_blueprint(route_edit, url_prefix='/edit')
    app.register_blueprint(route_hot_spot, url_prefix='/hotspot')
    app.register_blueprint(route_page, url_prefix='/article')

def configure_app():
    """
    # 设置 secret_key 来使用 flask 自带的 session
    """
    register_route()
    return app  # gunicorn


def main():
    cf = config
    setting = {
        'host': cf.host,
        'port': cf.port,
        'debug': cf.debug,
    }
    register_route()
    app.run(**setting)


if __name__ == '__main__':
    main()
