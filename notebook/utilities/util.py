# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6 
@desc:
"""

import hashlib
import functools
import logging
import traceback
import json
from bson import ObjectId
from cryptography.fernet import Fernet
from config import option
from datetime import datetime, timezone, timedelta
from tornado.httpclient import HTTPError
from google.protobuf.json_format import MessageToJson

# from src.common.exceptions import InternalError, ServerError
# from src.common.server_code import EnumServiceCode, EnumSystemCode, error_msg_from_code

logger = logging.getLogger('log')


def message_to_json(response):
    """
    grpc message -> json
    :param response: grpc message
    :return:
    """
    r = MessageToJson(response)
    d = json.loads(r)
    return d


def to_objectid(str_id):
    """
    str 转换为 ObjectId
    :param str_id:
    :return:
    """
    try:
        b = ObjectId(str_id)
        return b
    except Exception as e:
        err = traceback.format_exc()
        logger.error(err)
        # raise ServerError(EnumServiceCode.invalid_object_id)


def login_require(func):
    """
    登陆装饰器，func的执行必须是已登陆用户，否则跳转到登陆页面 (403)
    :param func: 被装饰的函数
    :return:
    """

    @functools.wraps(func)
    def wrapper(self, *args, **kwargs):
        current_user = self.get_current_user()
        if not current_user:
            raise HTTPError(403)
        return func(self, *args, **kwargs)

    return wrapper


def utc_to_localtime(utc):
    """
    utc 转换为当地时间
    utc: datetime 类型
    :return: 当地时间的 datetime 类型
    """
    utc = utc.replace(tzinfo=timezone.utc)
    hours = datetime.now().hour - datetime.utcnow().hour
    tzutc_local = timezone(timedelta(hours=hours))
    local_dt = utc.astimezone(tzutc_local)
    return local_dt


def encrypt(code):
    """
    对称加密
    code: str
    :return:
    """
    code = code.encode()
    key = option.secret.encode()
    f = Fernet(key)
    token = f.encrypt(code).decode()
    return token


def decrypt(code):
    """
    对称解码
    :param code: str
    :return:
    """
    try:
        bcode = code.encode()
        key = option.secret.encode()
        f = Fernet(key)
        de = f.decrypt(bcode)

        de = de.decode()
        return de
    except Exception as e:
        logger.info('decrypt {} error'.format(code))
        return ''


def hexdigest(pwd):
    """"""
    salt = 'abcdefg'

    def hashhex(ascii_str):
        m = hashlib.sha1()
        m.update(ascii_str.encode('ascii'))
        r = m.hexdigest()
        return r

    r = hashhex(pwd)
    r = hashhex(r + salt)
    return r
