# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""
from .agent_service import Service
from .agent_check import Check

class Agent(object):
    """
    The Agent endpoints are used to interact with a local Consul agent.
    Usually, services and checks are registered with an agent, which then
    takes on the burden of registering with the Catalog and performing
    anti-entropy to recover from outages.
    """
    def __init__(self, agent):
        self.agent = agent
        self.service = Service(agent)
        self.check = Check(agent)