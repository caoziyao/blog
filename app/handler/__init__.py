# coding: utf-8

from .index_handlers import handlers as index_handlers
from .test_handlers import handlers as test_handlers
from .tree_handlers import handlers as tree_handlers
from .book_handlers import handlers as book_handlers

handlers = []

handlers.extend(index_handlers)
handlers.extend(test_handlers)
handlers.extend(tree_handlers)
handlers.extend(book_handlers)


__all__ = [
    handlers,
]

