# coding: utf-8

import os
from flask import Flask, render_template, blueprints
from route.index import app as route_index
from route.edit import app as route_edit
from route.page import app as route_page
from route.folder import app as route_folder
from handlers import config

app = Flask(__name__)


def register_route():
    """
    注册蓝图
    :return:
    """
    app.register_blueprint(route_index)
    app.register_blueprint(route_edit, url_prefix='/edit')
    app.register_blueprint(route_page, url_prefix='/page')
    app.register_blueprint(route_folder, url_prefix='/folder')


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
