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
from config import option
import traceback
from flask import Flask
from .app.routes import register_blue
from concurrent import futures
from config import option
from common.request_tool import send_failure, send_success

app = Flask(__name__)

register_blue(app)


@app.errorhandler(500)
def error_handler_500(error):
    return send_failure(msg=str(error))


@app.teardown_request
def teardown_request(error):
    # 异常时候打印异常日志
    if error is not None:
        log.error(traceback.format_exc())


class ApiService(object):

    def __init__(self):
        pass

    def run(self):
        config = dict(
            port=option.api_port,
            host=option.api_host,
            debug=False,
            # debug=option.debug,
        )
        print('http://{}:{}'.format(config['host'], config['port']))
        app.run(**config)
