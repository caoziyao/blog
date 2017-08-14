# coding: utf-8

from flask import Flask, render_template, blueprints
from route.index import app as route_index
from route.edit import app as route_edit

app = Flask(__name__)



def register_app():
    """
    注册蓝图
    :return:
    """
    app.register_blueprint(route_index)
    app.register_blueprint(route_edit, url_prefix='/edit')



def main():
    config = {
        'host': '0.0.0.0',
        'port': 3000,
        'debug': True,
    }
    register_app()

    app.run(**config)

if __name__ == '__main__':
    main()