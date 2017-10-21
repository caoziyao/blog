# coding: utf-8


from enum import Enum, unique

__author__ = 'cczy'

@unique
class ResultCode(Enum):
    failure = 0
    success = 1