# coding:utf-8
import os
import time
import unittest
from pathlib import Path
# from test.test_case.index import cases_index

def creat_suite_all():
    testunit = unittest.TestSuite()
    test_dir = os.path.join(os.path.curdir, 'test', 'test_case')
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py', top_level_dir=None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit


# 构造测试集
def creat_suite():
    suite = unittest.TestSuite()
    # suite.addTests(cases_index)
    return suite


def option_define():
    pass


def main():
    suite = creat_suite_all()
    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == '__main__':
    main()
