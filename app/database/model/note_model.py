# coding: utf-8

from .base_model import BaseModel

class NoteModel(BaseModel):
    """
    tb_note
    """
    def __init__(self):
        super(NoteModel, self).__init__('tb_note')

    def load_members(self):
        """
        加载数据库字段
        :return:
        """
        result = super(NoteModel, self).load_members()
        return result

    def update(self):
        """
        将内存中的项目数据以更新的方式存入数据库
        :return:
        """
        self.update_data('id')