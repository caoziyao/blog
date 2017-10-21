# coding: utf-

import redis
from app.handlers import config
from app.untils import log

class DataCache(object):
    _instance = None
    _client = None
    _authed = False

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(DataCache, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        if self._client is None:
            cf = config.redis
            pool = redis.ConnectionPool(
                host=cf['host'],
                port=cf['port'],
                db=cf['db'],
                password=cf['password'],
                decode_responses=True,
            )
            self._client = redis.Redis(connection_pool=pool)
            self.test()

    @property
    def redis(self):
        """
        :return:
        """
        return self._client

    def test(self):
        """

        :return:
        """
        key = "test_key"
        self._client.set(key, 'redis test ok')
        self._client.delete(key)
        log('redis test ok')

    def client_info(self):
        """

        :return:
        """
        info = self._client.info()
        return info

    def __getattr__(self, name):
        return getattr(self._client, name)


redis_client = DataCache().redis