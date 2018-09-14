# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""
from base_common.consul_api.base.agent import Agent
from .http_client import HTTPClient

class Consul(object):

    def __init__( self, host='consul', port=8500):
        self.http = self.connect(host, port)
        self.agent = Agent(self)

    def connect(self, host, port):
        return HTTPClient(host, port)

