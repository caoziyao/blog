# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/11 
@desc:
"""

import time
import grpc
from concurrent import futures
from proto import user_pb2_grpc
from config import option
from common.constant import weixin_oauth_url, weixin_appid, weixin_secret
import json
from proto import weixin_pb2, weixin_pb2_grpc
from micro_services.user.database import UserManager

class WeixinService(weixin_pb2_grpc.WeixinServicer):

    def WeixinLogin(self, request, context):
        metadata = dict(context.invocation_metadata())
        print('metadata', metadata)

    def WeixinLogout(self, request, context):
        metadata = dict(context.invocation_metadata())
        print('metadata', metadata)