import time
import hashlib

salt = 'random salt'

def log(*args, **kwargs):
    """
    调试信息
    time.time() 返回 unix time
    strftime 把 unix time 转换为普通人类可以看懂的格式
    """
    format = '%Y-%m-%d %H:%H:%S'
    value = time.localtime(int(time.time()))
    dt = time.strftime(format, value)
    with open('log.txt', 'a', encoding='utf-8') as f:
        print(dt, *args, file=f, **kwargs)


def sh1hexdigest(pwd):
    """
    摘要算法
    """
    def sh1hex(ascii_str):
        return hashlib.sha1(ascii_str.encode('ascii')).hexdigest()
    s1 = sh1hex(pwd)
    s2 = sh1hex(s1 + salt)
    return s2

# log('hello log')