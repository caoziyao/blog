# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/13 
@desc:
"""
from proto import notebook_pb2
from proto import notebook_pb2_grpc
from rpc.user import UserClient
from micro_services.notebook.database import NoteBookManager


def data_to_fe(books):
    data = []
    for book in books:
        d = {}
        d['title'] = book.get('title', '')
        d['summary'] = book.get('summary', '')
        d['image'] = book.get('image', '')
        d['userId'] = book.get('user_id', '')
        d['id'] = book.get('id', '')
        data.append(d)
    return data


def get_notebook(request, context):
    """
    查询笔记本
    """
    metadata = dict(context.invocation_metadata())
    user_id = request.user_id
    user_id = 1

    # if user:
    notebook_manger = NoteBookManager()
    books = notebook_manger.notebook_from(user_id)
    data = data_to_fe(books)
    res = dict(
        data=data,
        user={},
    )
    return notebook_pb2.GetNoteBookResponse(**res)
