# coding: utf-8

import unittest
from micro_services.api_kuaibiji import app_run as flaskr

class BaseCase(unittest.TestCase):
    """测试基础类"""

    def __init__(self, *args, **kwargs):
        super(BaseCase, self).__init__(*args, **kwargs)

    @classmethod
    def setUpClass(cls):
        """
        测试开始前执行
        :return:
        """
        pass

    def setUp(self):
        flaskr.app.config['TESTING'] = True
        self.app = flaskr.app.test_client()

    def tearDown(self):
        pass
