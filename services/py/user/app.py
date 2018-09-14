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

root = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
sys.path.append(root)

import signal
import uuid
from flask import Flask, request
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple
import json
from base_common import sidecar
from jsonrpc import JSONRPCResponseManager, dispatcher
from user.views.rpc import patchers
from user.config import config
from base_common.consul_api.std.consul import Consul

app = Flask(__name__)


@app.route('/health')
def health():
    data = {
        'status': 'srv-user healthy'
    }
    return json.dumps(data)


def register():
    consul = Consul()

    data = {
        'name': 'srv-user',
        'address': 'srv-user',
        "service_id": "srv-user-" + str(uuid.uuid4()),
        # "service_id": "srv-weixin-random_128",
        "port": 4000,
        'check': {
            'http': 'http://srv-user:{port}/health'.format(port=4000),
            'interval': '10s',
            "DeregisterCriticalServiceAfter": "2m",

        }
    }

    consul.agent.service.register(**data)


def register_patcher():
    for k, v in patchers.items():
        dispatcher[k] = v


@app.route('/', methods=['POST'])
def index():
    register_patcher()
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    s = Response(response.json, mimetype='application/json')

    return s


class AppUserService(object):

    def run(self):
        register()
        app.run(host='0.0.0.0', port=4000, debug=config.debug)


if __name__ == '__main__':
    s = AppUserService()
    s.run()
