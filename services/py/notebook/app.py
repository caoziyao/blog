# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/7 
@desc:
"""
import traceback
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
from notebook.views.rpc import patchers
from base_common.request_service import send_failure, send_success
from config_default.log import debug_log
from base_common.exceptions import ApiException
from notebook.config import config
from base_common.consul_api.std.consul import Consul

app = Flask(__name__)


# service = {
#     "name": "srv-notebook",
#     "nodes": [{
#         "id": "srv-notebook-" + str(uuid.uuid4()),
#         "address": "srv-notebook",
#         "port": 4000,
#     }],
# }

@app.route('/health')
def health():
    data = {
        'status': 'srv-notebook healthy'
    }
    return json.dumps(data)


def register():
    consul = Consul()

    data = {
        'name': 'srv-notebook',
        'address': 'srv-notebook',
        "service_id": "srv-notebook-" + str(uuid.uuid4()),
        # "service_id": "srv-weixin-random_128",
        "port": 4000,
        'check': {
            'http': 'http://srv-notebook:{port}/health'.format(port=4000),
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


class AppNotebookService(object):

    def run(self):
        register()
        app.run(host='0.0.0.0', port=4000, debug=config.debug)


def sig_handler():
    print('sig_handler')


if __name__ == '__main__':
    s = AppNotebookService()
    s.run()
