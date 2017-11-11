# coding:utf-8
# !/user/bin/python

import os
import time
import unittest
import HTMLTestRunner
import logging.config
from pathlib import Path
from test_case import login_cases
from test_case import scene_cases

LogFilePath = os.path.join('config', 'logger.conf')  # 默认配置日志路径
logging.config.fileConfig(LogFilePath)
logger = logging.getLogger('testlog')  # 获取dblog的日志配置


def creatsuite_all():
    testunit = unittest.TestSuite()
    test_dir = os.path.join(os.path.curdir, 'test_case')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit


# 构造测试集
def creatsuite():
    suite = unittest.TestSuite()
    suite.addTests(login_cases)
    suite.addTests(scene_cases)
    return suite


def run_with_html(suite):
    # 定义报告存放路径
    filename = 'result_' + time.strftime("%Y-%m-%d %H_%M_%S") + '.html'
    path = os.path.join('report', filename)
    if not os.path.exists('report'):
        os.makedirs('report')
    with open(path, 'wb') as f:
        runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'测试报告', description=u'用例执行情况：')
        # 运行测试用例
        runner.run(suite)


def option_define():
    pass


def main():
    suite = creatsuite()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()


    # todo
    # 把 post 提交的数据放到 excel/json 里面
    # 部署 rar 在线文档
    # 编写在线文档
