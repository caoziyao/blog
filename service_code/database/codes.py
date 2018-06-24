# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/6/15 
@desc:
"""
from enum import Enum, unique


@unique
class EnumSystemCode(Enum):
    success: 1
    system_error = 10001
    service_unavailable = 10002
    remote_service_error = 10003
    ip_limit = 10004
    permission_denied = 10005
    appkey_missing = 10006
    unsupport_mediatype = 10007
    param_error = 10008
    system_busy = 10009
    job_expired = 10010
    rpc_error = 10011
    illegal_request = 10012
    invalid_user = 10013
    api_permissions = 10014
    param_miss = 10016
    param_invalid = 10017

    json_parse_error = 10100


@unique
class EnumServiceCode(Enum):

    # 通用服务 00 预留01
    user_not_exists = 20002
    invalid_object_id = 20003

    # 用户服务 02
    auth_faild = 20201

    # 笔记本服务 03
    exist_notebook = 20301
    notebook_not_exist = 20302
    exist_note = 20303
    note_not_exist = 20304


system_error_codes = {
    1: 'success',
    10001: 'system error',
    10002: 'service unavailable',
    10003: 'Remote service error',
    10004: 'IP limit',
    10005: 'Permission denied, need a high level appkey',
    10006: 'Source paramter (appkey) is missing',
    10007: 'Unsupport mediatype ({})',
    10008: 'Param error, see doc for more info',
    10009: 'Too many pending tasks, system is busy',
    10010: 'Job expired',
    10011: 'RPC error',
    10012: 'Illegal request',
    10013: 'Invalid user',
    10014: 'Insufficient app permissions',
    10016: 'Miss required parameter ({}) , see doc for more info',
    10017: "Parameter ({})'s value invalid, expect ({}) , but get ({}) , see doc for more info",

    10100: 'json parse error',
}

service_error_codes = {
    # 通用服务 00 预留01
    20002: 'User does not exists',
    20003: 'invalid id: not a valid ObjectId',

    # 用户服务 02
    20201: 'Auth faild',

    # 笔记本服务 03
    20301: 'Already exist notebook',
    20302: 'notebook does not exists',
    20303: 'Already exist note',
    20304: 'note does not exists',
}




