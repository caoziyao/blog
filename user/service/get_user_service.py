# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc:
"""
import json
from proto import user_pb2
from proto import user_pb2_grpc
from database import UserManager
from .base_service import BaseService

class Greeter(user_pb2_grpc.UserServicer):

    def data_to_fe(self, user):

        d = {}
        if user:
            d['userId'] = user.get('user_id', '')
            d['updateTime'] = user.get('update_time', '')
            d['createTime'] = user.get('create_time', '')
            d['userName'] = user.get('user_name', '')
        return d

    def GetUserInfo(self, request, context):
        """
        查询用户
        """
        metadata = dict(context.invocation_metadata())
        print('metadata', metadata)

        user_id = request.userId
        print('user', user_id)
        user_manger = UserManager()
        user_data = user_manger.user_by_userid(user_id)

        data = self.data_to_fe(user_data)

        res = dict(
            data=data
        )
        return user_pb2.GetUserResponse(**res)
