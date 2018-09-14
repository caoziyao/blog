# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/7
@desc:
"""
import traceback
from flask import Flask

app = Flask(__name__)

class BaseError(Exception):
    pass

class ApiException(BaseError):
    """
    """

    def __init__(self, code='', data='', message=''):
        self.code = code
        self.message = message
        self.data = data

def send_failure(data='', msg='failure', code='1'):
    """

    :param code:
    :param data:
    :param msg:
    :return:
    """
    r = {
        'code': code,
        'data': data,
        'msg': msg,
    }
    return r


@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return send_failure(msg='not found', code='4000123'), 404

@app.errorhandler(ApiException)
def error_handlers(e):
    """

    :return:
    """
    print('error_handlers ApiException')
    return send_failure(msg='not id')

@app.teardown_request
def after_request(error):
    if error is not None:  # 异常时候打印异常日志
        print(traceback.format_exc())

    return send_failure(msg='not ssssss')


@app.before_request
def before_request():
    raise ApiException(message='dudduu')

def sig_handler():
    print('sig_handler')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)
    # signal.
