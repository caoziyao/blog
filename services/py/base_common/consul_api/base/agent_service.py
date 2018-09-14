# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/14 
@desc:
"""
import json


class Service(object):

    def __init__(self, agent):
        self.agent = agent

    def register(
            self,
            name,
            address=None,
            service_id=None,
            port=None,
            check=None,
            tags=None,
    ):
        """
        http://consul:8500/v1/agent/service/register
        https://www.consul.io/api/agent/service.html
        'check': {
            'http': 'http://srv-weixin:4000/health',
            'interval': '10s'
        }
        :return:
        """
        payload = {}

        payload['name'] = name
        if service_id:
            payload['id'] = service_id
        if address:
            payload['address'] = address
        if port:
            payload['port'] = port
        if tags:
            payload['tags'] = tags
        if check:
            payload['check'] = check
        else:
            # agent_check
            pass

        params = []

        uri = '/v1/agent/service/register'
        r = self.agent.http.put(
            uri,
            params=params,
            data=json.dumps(payload)
        )

        return r

    def deregister(self, service_id):
        """
        Used to remove a service from the local agent. The agent will
        take care of deregistering the service with the Catalog. If
        there is an associated check, that is also deregistered.
        """
        uri = '/v1/agent/service/deregister/{}'.format(service_id)
        r = self.agent.http.put(uri)

        return r
