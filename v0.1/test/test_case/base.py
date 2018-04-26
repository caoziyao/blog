# coding: utf-8

import os
import json
import logging
import base64, requests, time
import unittest
from pyquery import PyQuery as pq
from share import headers
from pathlib import Path
from test.config.config import path_test_data, path_output

logger = logging.getLogger('testlog')  # 获取dblog的日志配置



class Base(unittest.TestCase):
    """测试基础类"""

    def __init__(self, *args, **kwargs):
        super(Base, self).__init__(*args, **kwargs)
        self.headers = headers

    @classmethod
    def setUpClass(cls):
        """
        测试开始前执行
        :return:
        """
        pass

    def format_doc(self, docstring):
        """
        格式化 docstring
        """
        lines = docstring.split('\n')
        docs = []
        for l in lines:
            # s = l.strip() + '\n'
            s = l + '\n'
            docs.append(s)

        return ''.join(docs)

    def output_template(self, **res):
        """
        输出格式
        :return:
        url：/api/fc_datalist
        请求方式：POST
        数据格式：json
        {}
        返回格式：
        {}
        """
        api = res.get('api', '')
        method = res.get('method', '')
        req = res.get('req', '')
        response = res.get('response', '')
        remark = res.get('remark', '')

        r = 'url：{api} \n' \
            '请求方式：{methods} \n' \
            '数据格式：json \n' \
            '备注: {remark} \n' \
            '例子: \n' \
            '请求格式: \n' \
            '{request} \n' \
            '返回格式：\n' \
            '{response}'.format(
            api=api,
            methods=method,
            request=req,
            response=response.encode('utf-8'),
            remark=remark,
        ).strip()

        return r

    def output_text(self, **res):
        """
        输出文档
        :return:
        """
        rewrite = res.get('rewrite', False)
        filename = res.get('filename', 'defalut.txt')
        folder = path_output.joinpath(res.get('folder', 'defalut'))
        if not folder.exists():
            folder.mkdir()

        path = folder.joinpath(filename)
        if rewrite or not path.exists():
            text = self.output_template(**res)
            with open(str(path), 'w') as f:
                f.write(text)
                logging.info(u'{}更新了 api 文档'.format(filename.decode('utf-8')))
        else:
            # logging.info(u'{}不需要更新 api 文档'.format(filename.decode('utf-8')))
            pass




