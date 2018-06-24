# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/15 
@desc:
"""

from werkzeug.wrappers import Request, Response
from werkzeug.serving import run_simple

from jsonrpc import JSONRPCResponseManager, dispatcher
from api import route

import uuid
import requests
import micro_sidecar

service = {
    "name": "go.micro.srv.codes",
    "nodes": [{
        "id": "go.micro.srv.codes-" + str(uuid.uuid4()),
        "address": "127.0.0.1",
        "port": 4001,
    }],
}

def init_handler():
    for k, v in route.items():
        dispatcher[k] = v

@Request.application
def application(request):
    print('in rpc codes')
    # dispatcher["Say.Hello"] = lambda s: "Hello " + s["name"] + "!"
    #
    # dispatcher["Say.Hello22"] = lambda s: "Hello22 " + s["name"] + "!"
    response = JSONRPCResponseManager.handle(request.data, dispatcher)
    return Response(response.json, mimetype='application/json')

if __name__ == '__main__':
    micro_sidecar.register(service)
    init_handler()
    run_simple('localhost', 4001, application)
    micro_sidecar.deregister(service)
