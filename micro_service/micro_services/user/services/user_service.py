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
from micro_services.user.database import UserManager
from .base_service import BaseService
from micro_services.user.handlers import (
    get_user_info,
    login,
    logout,
)


class Greeter(user_pb2_grpc.UserServicer):

    def GetUserInfo(self, request, context):
        """ 查询用户
        """
        return get_user_info(request, context)

    def Login(self, request, context):
        """ 登录
        """
        return login(request, context)

    def Logout(self, request, context):
        """ 登出
        """
        return logout(request, context)

        # metadata = dict(context.invocation_metadata())
        # print('metadata', metadata)
        #
        # user_id = request.userId
        # user_manger = UserManager()
        # user_data = user_manger.user_by_userid(user_id)
        #
        # data = self.data_to_fe(user_data)
        # res = dict(
        #     data=data
        # )
        # return user_pb2.GetUserResponse(**res)
