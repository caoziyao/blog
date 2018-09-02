# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc:
"""
from proto import notebook_pb2
from proto import notebook_pb2_grpc, user_pb2, user_pb2_grpc
from rpc_client.user import UserClient
from config import config
import grpc
from utilities.util import message_to_json
# from app.service.base_service import BaseService
from rpc_client.client_wrapper import ServiceClient
from common.exceptions import RPCException


class NoteBookClient(object):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NoteBookClient, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super(NoteBookClient, self).__init__()
        self.server_name = 'srv-notebook'
        self.host = config.notebook_host
        self.port = config.notebook_port

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
            client = ServiceClient(notebook_pb2_grpc, 'NotebookStub', self.host, self.port)
            return client
        except grpc.RpcError as e:
            msg = str(e)
            raise RPCException(msg=msg)

    def get_notebooks(self):
        """

        :return:
        """
        # metadata = self.metadata
        metadata = {}
        request = notebook_pb2.GetNoteBookRequest(
            user_id='1'
        )

        stub = self.client.stub
        try:
            response = stub.GetNotebookInfo(
                request,
                metadata=metadata,
                timeout=config.timeout_client_side,
            )
        except grpc.RpcError as e:
            msg = str(e)
            raise RPCException(msg='calling rpc application')
        else:
            s = message_to_json(response)
            return s
