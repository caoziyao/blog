# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""

class MysqlBaseManger(object):

    pass
    # def model_to_json(self, mdoel, feilds=None):
    #     """
    #     model to json
    #     feilds: []
    #     :param mdoel:
    #     :return:
    #     """
    #     columns = mdoel.__table__.columns
    #     if not feilds:
    #         d = {
    #             c.name: getattr(mdoel, c.name, None) for c in columns
    #         }
    #     else:
    #         k = list(set(columns) - set(feilds))
    #         d = {
    #             c.name: getattr(mdoel, c.name, None) for c in k
    #         }
    #     return d