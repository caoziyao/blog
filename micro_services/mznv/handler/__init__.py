# coding: utf-8

from .index_handlers import handlers as index_handlers
from .test_handlers import handlers as test_handlers
from .tree_handlers import handlers as tree_handlers
from .book_handlers import handlers as book_handlers
from .user_handlers import handlers as user_handlers
from .email_handlers import handlers as email_handlers

handlers = []

handlers.extend(index_handlers)
handlers.extend(test_handlers)
handlers.extend(tree_handlers)
handlers.extend(book_handlers)
handlers.extend(user_handlers)
handlers.extend(email_handlers)


__all__ = [
    handlers,
]

