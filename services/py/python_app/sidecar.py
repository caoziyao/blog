# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/7 
@desc:
"""

import uuid
import requests
import json

registry_uri = "http://microhq-sidecar:8081/registry"
broker_uri = "http://microhq-sidecar:8081/broker"
call_uri = "http://microhq-sidecar:8081"
headers = {'content-type': 'application/json'}

def register(service):
    return requests.post(registry_uri, data=json.dumps(service), headers=headers)

def deregister(service):
    return requests.delete(broker_uri, data=json.dumps(service), headers=headers)
    # return requests.delete(registry_uri, data=json.dumps(service), headers=headers)

def rpc_call(path, request):
    return requests.post(call_uri + path, data=json.dumps(request), headers=headers)

def http_call(path, request):
    return requests.post(call_uri + path, data=request)
