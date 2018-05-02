# coding: utf-8


from .book_handler import BookHandler

handlers = [
    (r'/api/book/get_book_list', BookHandler),
]


__all__ = [
    handlers,
]
