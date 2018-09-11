# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/7 
@desc:
"""
import sys
import os
import signal
import uuid
from flask import Flask, request
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import json
from python_app import sidecar
from jsonrpc import JSONRPCResponseManager, dispatcher
from user.views.rpc import patchers

app = Flask(__name__)

service = {
    "name": "srv-user",
    "nodes": [{
        "id": "srv-user-" + str(uuid.uuid4()),
        "address": "srv-user",
        "port": 4000,
    }],
}


def register_patcher():
    for k, v in patchers.items():
        dispatcher[k] = v


def auto_response():
    """

    :return:
    """
    b = request.data.decode('utf-8')
    c = json.loads(b)
    return json.dumps({"jsonrpc": "2.0", "result": c, "id": 2})


@app.before_request
def before_request():
    register_patcher()
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    s = Response(response.json, mimetype='application/json')
    return s


class AppUserService(object):

    def run(self):
        # sidecar.deregister(service)
        sidecar.register(service)
        app.run(host='0.0.0.0', port=4000, debug=True)
        # sidecar.deregister(service)


if __name__ == '__main__':
    app = AppUserService()
    app.run()
