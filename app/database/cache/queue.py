# coding: utf-8

from .data_cache import redis_client

class QueueBase(object):

    def __init__(self, key):
        """
        client : redis对象
        key : redis list
        :param key:
        """
        self.client = redis_client
        self.key = key

    def push(self, request):
        """Push a request"""
        raise NotImplementedError

    def pop(self, request):
        """Pop a request"""
        raise NotImplementedError

    def clear(self):
        """Clear queue"""
        self.client.delect(self.key)


class FifoQueue(QueueBase):

    def __init__(self, key):
        super(FifoQueue, self).__init__(key)


    def __len__(self):
        """Return the length of the queue"""
        return self.client.llen(self.key)

    def push(self, request):
        """Push a request"""
        self.client.lpush(self.key, request)

    def pop(self, timeout=0):
        """Pop a request"""
        if timeout > 0:
            data = self.client.brpop(self.key, timeout)
            if isinstance(data, tuple):
                data = data[1]
        else:
            data = self.client.rpop(self.key)

        return data


    def contains(self, key):
        """contains key"""
        pass