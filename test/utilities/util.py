# coding:utf-8
# !/user/bin/python

import json

def ucode_json(data):
    """

    :param args:
    :param kwargs:
    :return:
    """
    s = json.loads(data, encoding='utf-8')
    rdata = json.dumps(s, ensure_ascii=False, encoding='utf-8')

    return rdata