# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""

from proto import weixin_pb2, weixin_pb2_grpc
from config import option
import grpc
from utilities.util import message_to_json
# from app.service.base_service import BaseService
from rpc.client_wrapper import ServiceClient


class WeixinClient(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(WeixinClient, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super(WeixinClient, self).__init__()
        self.server_name = 'srv-weixin'
        self.host = option.weixin_host
        self.port = option.weixin_port

    @property
    def client(self):
        if not hasattr(self, "_client"):
            self._client = self.get_client()
        return self._client

    @client.setter
    def client(self, value):
        # self._client = value
        pass

    def get_client(self):
        client = ServiceClient(weixin_pb2_grpc, 'WeixinStub', self.host, self.port)
        return client

    def login(self, user_id):
        # metadata = self.metadata
        metadata = {}
        request = weixin_pb2.RequestWeixinLogin(
            userId=user_id
        )
        response = self.client.stub.WeixinLogin(request,
            metadata=metadata,
            timeout=option.timeout_client_side,
        )
        data = message_to_json(response)
        return data

    def logout(self, user_id):
        # metadata = self.metadata
        metadata = {}
        request = weixin_pb2.RequestWeixinLogout(
            userId=user_id
        )
        response = self.client.stub.WeixinLogout(request,
            metadata=metadata,
            timeout=option.timeout_client_side,
        )
        data = message_to_json(response)
        return data