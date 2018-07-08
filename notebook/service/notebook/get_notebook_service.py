# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/7/6
@desc:
"""
from proto import notebook_pb2
from proto import notebook_pb2_grpc
from database import NoteBookManager
from service.user import UserService


class Greeter(notebook_pb2_grpc.NotebookServicer):

    def data_to_fe(self, books):
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

    def GetNotebookInfo(self, request, context):
        """
        查询笔记本
        """
        metadata = dict(context.invocation_metadata())

        user_id = request.user_id

        # user_service = UserService()
        # user = user_service.user_by_id(user_id)

        # user_id = 'shllo'

        # if user:
        notebook_manger = NoteBookManager()
        books = notebook_manger.notebooks_by_userid(user_id)
        data = self.data_to_fe(books)
        res = dict(
            data=data,
            user={},
        )
        return notebook_pb2.GetNoteBookResponse(**res)
        # else:
        #     res = dict(
        #         code='20200',
        #         message='error',
        #         data='',
        #     )
        #     return notebook_pb2.ErrorResponse(**res)
