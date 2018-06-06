# coding: utf-8


from .login_handler import LoginHandler
from .sigin_handler import SiginHandler



handlers = [
    (r'/api/user/login', LoginHandler),
    (r'/api/user/sigin', SiginHandler),
]

__all__ = [
    handlers,
]
