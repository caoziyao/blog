# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/15 
@desc:
"""
import traceback
from proto import weixin_pb2, weixin_pb2_grpc
from config import option
import grpc
from utilities.util import message_to_json
# from app.service.base_service import BaseService
from rpc.client_wrapper import ServiceClient
from common.exceptions import RPCException


def login(client, args):
    # metadata = self.metadata
    metadata = {}

    appid = args.get('appid', '')
    secret = args.get('secret', '')
    js_code = args.get('js_code', '')
    grant_type = args.get('grant_type', '')

    request = weixin_pb2.RequestWeixinLogin(
        appid=appid,
        secret=secret,
        js_code=js_code,
        grant_type=grant_type,
    )
    try:
        response = client.stub.WeixinLogin(request,
                                           metadata=metadata,
                                           # timeout=option.timeout_client_side,
                                           )
    except grpc.RpcError as e:
        msg = traceback.format_exc()
        raise RPCException(msg=msg)
    else:
        data = message_to_json(response)
        return data
