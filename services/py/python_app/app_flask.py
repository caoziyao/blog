# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""
import sys
import os
from flask import Flask, request
from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from python_app import sidecar
from jsonrpc import JSONRPCResponseManager, dispatcher

import uuid

app = Flask(__name__)

service = {
    "name": "srv-notebook",
    "nodes": [{
        "id": "srv-notebook-" + str(uuid.uuid4()),
        "address": "srv-notebook",
        "port": 4000,
    }],
}

@app.before_request
def before_request():
    print('s,')
    dispatcher["SayC.Hello"] = lambda s: "greeting=hello" + s["name"] + "!"

    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    s = Response(response.json, mimetype='application/json')
    return s

class AppNotebookService(object):

    def run(self):
        sidecar.register(service)
        app.run(host='0.0.0.0', port=4000, debug=True)
        sidecar.deregister(service)

if __name__ == '__main__':
    app = AppNotebookService()
    app.run()

