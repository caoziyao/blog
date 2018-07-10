# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/8 
@desc:
"""
from proto import user_pb2, user_pb2_grpc
from config import option
import grpc
from utilities.util import message_to_json
# from app.service.base_service import BaseService
from rpc.client_wrapper import ServiceClient


class UserClient(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(UserClient, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super(UserClient, self).__init__()
        self.server_name = 'srv-user'
        self.host = option.user_host
        self.port = option.user_port

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
        client = ServiceClient(user_pb2_grpc, 'UserStub', self.host, self.port)
        return client

    def user_by_id(self, user_id):
        # metadata = self.metadata
        metadata = {}
        request = user_pb2.GetUserRequest(
            userId=user_id
        )
        response = self.client.stub.GetUserInfo(request,
            metadata=metadata,
            timeout=option.timeout_client_side,
        )
        data = message_to_json(response)
        return data