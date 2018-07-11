# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""
import json
from proto import user_pb2
from proto import user_pb2_grpc
from micro_services.user.database import UserManager


def data_to_fe(user):
    d = {}
    if user:
        d['userId'] = user.get('user_id', '')
        d['updateTime'] = user.get('update_time', '')
        d['createTime'] = user.get('create_time', '')
        d['userName'] = user.get('user_name', '')
    return d


def get_user_info(request, context):
    """
    查询用户
    """
    metadata = dict(context.invocation_metadata())
    print('metadata', metadata)

    user_id = request.userId
    user_manger = UserManager()
    user_data = user_manger.user_by_userid(user_id)

    data = data_to_fe(user_data)
    res = dict(
        data=data
    )
    return user_pb2.GetUserResponse(**res)
