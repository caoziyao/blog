# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""

from proto import weixin_pb2, weixin_pb2_grpc
from config import config
import grpc
from utilities.util import message_to_json
# from app.service.base_service import BaseService
from rpc_client.client_wrapper import ServiceClient
from common.exceptions import RPCException
from .handlers import login

class WeixinClient(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(WeixinClient, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super(WeixinClient, self).__init__()
        self.server_name = 'srv-weixin'
        self.host = config.weixin_host
        self.port = config.weixin_port

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
        try:
            client = ServiceClient(weixin_pb2_grpc, 'WeixinStub', self.host, self.port)
            return client
        except grpc.RpcError as e:
            msg = str(e)
            raise RPCException(msg=msg)

    def login(self, args):
        # metadata = self.metadata
        data = login(self.client, args)
        return data
        # metadata = {}
        # request = weixin_pb2.RequestWeixinLogin(
        #     appid=appid,
        #     secret=secret,
        #     js_code=js_code,
        #     grant_type=grant_type,
        # )
        # try:
        #     response = self.client.stub.WeixinLogin(request,
        #                                             metadata=metadata,
        #                                             timeout=config.timeout_client_side,
        #                                             )
        # except grpc.RpcError as e:
        #     msg = str(e)
        #     raise RPCException(msg='calling rpc weixin application')
        # else:
        #     data = message_to_json(response)
        #     return data

    def logout(self, user_id):
        # metadata = self.metadata
        metadata = {}
        request = weixin_pb2.RequestWeixinLogout(
            userId=user_id
        )
        try:
            response = self.client.stub.WeixinLogout(request,
                                                     metadata=metadata,
                                                     timeout=config.timeout_client_side,
                                                     )
        except grpc.RpcError as e:
            msg = str(e)
            raise RPCException(msg='calling rpc weixin application')
        else:
            data = message_to_json(response)
            return data
