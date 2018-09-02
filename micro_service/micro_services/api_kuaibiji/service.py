# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/10 
@desc:
"""
from common.logger import log, dblog
import grpc
from config import config
import traceback
from flask import Flask, current_app, g
from concurrent import futures
from config import config
from common.request_tool import send_failure, send_success
from .app.routes import register_blue
from .app.handlers import BaseHandler

app = Flask(__name__)
register_blue(app)


@app.before_request
def before_request():
    """所有请求前执行方法"""
    handler = BaseHandler()
    g.handler = handler


@app.errorhandler(500)
def error_handler_500(error):
    """
    返回 500 错误处理函数
    :param error:
    :return:
    """
    err_msg = traceback.format_exc()
    if config.debug:
        data = {
            'debug_info': err_msg
        }
    else:
        data = {}
    return send_failure(msg=str(error), data=data)


@app.teardown_request
def teardown_request(error):
    """
    异常时候打印异常日志
    :param error:
    :return:
    """
    if error is not None:
        log.error(traceback.format_exc())


class ApiService(object):

    def __init__(self):
        pass

    def make_app(self):
        return app

    def run(self):
        config = dict(
            port=config.api_port,
            host=config.api_host,
            debug=False,
            # debug=config.debug,
        )
        print('http://{}:{}'.format(config['host'], config['port']))
        app.run(**config)
