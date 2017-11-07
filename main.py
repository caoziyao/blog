# coding: utf-8

import os
import logging.config
from flask import Flask
from app.handlers import config
from config.constant import static_folder
from app.route import route_index, route_edit, route_hot_spot, route_page, route_basis

app = Flask(__name__, static_url_path=static_folder)

path = os.path.join('config', 'logger.conf')       # 默认配置日志路径
logging.config.fileConfig(path)
logger = logging.getLogger()

def register_route():
    """
    注册蓝图
    :return:
    """
    app.register_blueprint(route_index)
    app.register_blueprint(route_edit, url_prefix='/edit')
    app.register_blueprint(route_hot_spot, url_prefix='/hotspot')
    app.register_blueprint(route_page, url_prefix='/article')
    app.register_blueprint(route_basis, url_prefix='/basis')


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
