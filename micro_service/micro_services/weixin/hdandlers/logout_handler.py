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
        d['userId'] = user.get('user_id', '1')
        d['updateTime'] = user.get('update_time', '2')
        d['createTime'] = user.get('create_time', '3')
        d['userName'] = user.get('user_name', '4')
    return d

def logout(request, context):
    """
    查询用户
    """
    metadata = dict(context.invocation_metadata())
    print('metadata', metadata)

    user = {}
    user_data = data_to_fe(user)
    res = dict(
        data=user_data
    )
    return user_pb2.GetUserResponse(**res)
