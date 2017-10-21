# coding: utf-8

import os
from datetime import datetime

class DatetimeHandler(object):
    # _instance = None
    # _members = {}

    def __init__(self):
        pass
        # self.path = os.path.join('config', 'config.json')
        # self.load_config()

    @classmethod
    def format_tostring(cls, date, fmt='%Y-%d-%m %H:%M:%S'):
        """
        datetime to str
        :param date: datetime 格式，或者 None
        :param fmt:
        :return:
        """
        if isinstance(date, datetime):
            d = date.strftime(fmt)
        elif date is None :
            d = ''
        else:
            raise TypeError('dateime 类型错误')

        return d


config = DatetimeHandler()