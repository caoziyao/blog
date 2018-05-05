# coding: utf-8


from .email_handler import EmailHandler

handlers = [
    (r'/api/email/send_email', EmailHandler),
]


__all__ = [
    handlers,
]
