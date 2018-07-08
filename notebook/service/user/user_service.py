# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/8 
@desc:
"""
import grpc
from proto import user_pb2
from proto import user_pb2_grpc
from service.base_service import BaseService

# from protobuf_to_dict import protobuf_to_dict

from utilities.util import message_to_json
from config import option


# host = '0.0.0.0'
# port = 8005

class UserService(BaseService):

    def __init__(self):
        super(UserService, self).__init__()
        self.server_name = 'srv-user'
        self.host = option.user_host
        self.port = option.user_port
        self.channel = grpc.insecure_channel('{}:{}'.format(self.host, str(self.port)))

    def user_by_id(self, user_id):
        channel = self.channel

        try:
            grpc.channel_ready_future(channel).result(timeout=option.timeout_channel)
        except grpc.FutureTimeoutError:
            print('time out')
            raise Exception('Error connecting to {} server '.format(self.server_name))
        else:
            stub = user_pb2_grpc.UserStub(channel)
            metadata = self.metadata

            response = stub.GetUserInfo(user_pb2.GetUserRequest(
                userId=user_id),
                metadata=metadata,
                timeout=option.timeout_client_side,
            )
            res = message_to_json(response)
            data = res.get('data', None)

            return data
