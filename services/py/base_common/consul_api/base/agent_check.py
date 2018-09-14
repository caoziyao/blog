# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""

class Check(object):
    """
    https://www.consul.io/api/agent/check.html
    """
    def __init__(self, agent):
        self.agent = agent