# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""
# https://python-consul.readthedocs.io/en/latest/#consul-agent
import consul

consul.Consul().Agent.Service().register()
