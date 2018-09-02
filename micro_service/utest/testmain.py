# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/2 
@desc:
python3 -m unittest utest/test_case/test_demo.py
python -m unittest discover <test_directory>
python -m unittest discover -s <directory> -p '*_test.py'
"""
import sys
import os

root = os.path.abspath(os.path.join(os.path.abspath(__file__), '..', '..'))
sys.path.append(root)

import unittest
from utest.test_case.test_demo import TestDemoCase
from utest.common.constant import EnumVerbosity


def add_tests():
    suite = unittest.TestSuite()
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemoCase))
    return suite


def start_dir_from_arv():
    """"""
    argv = sys.argv
    l = len(argv)

    if l == 2:
        dir = argv[1]
        start = os.path.join(root, 'utest', 'test_case', dir)
    else:
        start = os.path.join(root, 'utest', 'test_case')

    return start


def main():
    # main
    print('root', root)
    start_dir = start_dir_from_arv()
    loader = unittest.TestLoader()
    suite = loader.discover(start_dir, pattern='test_*.py')

    with open('UnittestTextReport.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=EnumVerbosity.detail.value)
        runner.run(suite)


if __name__ == '__main__':
    main()
