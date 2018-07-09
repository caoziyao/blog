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
from app.service.user import UserService
from app.config import option
import grpc
from app.utilities.util import message_to_json
from app.service.base_service import BaseService
from app.service.client_wrapper import ServiceClient


class NoteBookService(BaseService):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(NoteBookService, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super(NoteBookService, self).__init__()
        self.server_name = 'srv-notebook'
        self.host = option.notebook_host
        self.port = option.notebook_port

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
        client = ServiceClient(notebook_pb2_grpc, 'NotebookStub', self.host, self.port)
        return client

    def get_notebooks(self):
        metadata = self.metadata
        request = notebook_pb2.GetNoteBookRequest(
            userId='oMNol0Yk9XeI_0jHsYuFgFsQ2h6s'
        )

        response = self.client.stub.GetNotebookInfo(request,
            metadata=metadata,
            timeout=option.timeout_client_side,
        )
        s = message_to_json(response)
        return s

