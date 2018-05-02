# coding: utf-8


from .index_handler import MainHandler


handlers = [
    (r'/', MainHandler),
]


__all__ = [
    handlers,
]
