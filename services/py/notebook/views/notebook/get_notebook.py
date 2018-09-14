# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/8 
@desc:
"""
from notebook.database.notebook_manger import NotebookManger
from notebook.bussiness.notebook_controller import NotebookController
from base_common.request_service import send_failure, send_success
from base_common.utils import is_number, toint
from config_default.log import debug_log
from base_common.exceptions import ApiException

def get_notebooks(ids):
    """

    :param ids:
    :return:
    """
    m = NotebookManger()

    args = []
    for i in ids:
        if is_number(i):
            i = toint(i)
            args.append(i) if i else ''

    notebooks = m.get_notebooks(args)
    debug_log.info(notebooks)

    l = []
    for each in notebooks:
        d = {
            'id': each.id,
            'name': each.name,
        }
        l.append(d)
    return l


def get_one_notebook(_id):
    """

    :param _id:
    :return:
    """
    m = NotebookManger()
    nb = m.get_notebook(_id)
    if nb:
        d = {
            'id': nb.id,
            'name': nb.name,
        }
    else:
        d = {}

    return d


def get_notebook(request):
    """
    get notebook
    :param request:
    :return:
    """
    _id = request.get('id', '')
    if not _id:
        raise ApiException(msg='not id')

    if isinstance(_id, list):
        data = get_notebooks(_id)

    else:
        data = get_one_notebook(_id)

    return send_success(data=data)
