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

root = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
sys.path.append(root)
import requests
import uuid
from flask import Flask, request
from werkzeug.wrappers import Request, Response
import json
from base_common import sidecar
from jsonrpc import JSONRPCResponseManager, dispatcher
from weixin.views.rpc import patchers
from weixin.config import config
from base_common.consul_api.std.consul import Consul

app = Flask(__name__)


@app.route('/health')
def health():
    data = {
        'status': 'healthy===dudu'
    }
    return json.dumps(data)


def register():
    consul = Consul()

    name = config.service_name
    address = config.address
    data = {
        'name': name,
        'address': 'srv-weixin',
        "service_id": "srv-weixin-random_" + str(uuid.uuid4()),
        # "service_id": "srv-weixin-random_128",
        "port": 4005,
        'check': {
            'http': 'http://srv-weixin:{port}/health'.format(port=4005),
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

class AppWeixinService(object):

    def __init__(self):
        pass

    def run(self):
        register()

        app.run(host='0.0.0.0', port=4005, debug=config.debug)


if __name__ == '__main__':
    s = AppWeixinService()
    s.run()
