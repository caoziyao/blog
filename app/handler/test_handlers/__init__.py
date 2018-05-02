# coding: utf-8


from .test_handler import TestHandler


handlers = [
    (r'/test', TestHandler),
]


__all__ = [
    handlers,
]
