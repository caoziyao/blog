# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc: user 服务
"""
from .service import UserService

def main():
    s = UserService()
    s.run()

if __name__ == '__main__':
    main()
