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
from common.logger import log
from utilities.util import dtime2str


def data_to_fe(user):
    d = {}
    if user:
        d['userId'] = str(user.get('id', ''))
        d['updateTime'] = dtime2str(user.get('update_time', ''))
        d['createTime'] = dtime2str(user.get('create_time', ''))
        d['userName'] = user.get('username', '')
    return d


def get_user_info(request, context):
    """
    查询用户
    """
    metadata = dict(context.invocation_metadata())

    user_id = request.userId
    user_manger = UserManager()

    query = {
        'id': user_id
    }
    user_data = user_manger.user_from(query)

    data = data_to_fe(user_data)

    res = dict(
        data=data
    )
    return user_pb2.GetUserResponse(**res)
