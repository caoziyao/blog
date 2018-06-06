# coding: utf-8

import hashlib
from app.cache import redis_client

def cache_func(expire_time):
    def decorator(func):
        def wrap(*args, **kwargs):
            cache_key = func.__name__
            data = redis_client.get_bylock(cache_key)
            if data:
                print('read redis')
                return data
            else:
                data = func(*args, **kwargs)
                redis_client.set_bylock(cache_key, data, expire_time)
                return data
        return wrap

    return decorator



def hexdigest(pwd):

    salt = 'abcdefght'

    def hashhex(ascii_str):
        m = hashlib.sha1()
        m.update(ascii_str.encode('ascii'))
        r = m.hexdigest()
        return r

    r = hashhex(pwd)
    r = hashhex(r + salt)
    return r

def main():
    print(hexdigest('1221'))

if __name__ == '__main__':
    main()