# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/2 
@desc:

python3 -m unittest utest/test_case/test_demo.py
"""
import sys
import os
import unittest

sys.path.append('..')
from utest.test_case.test_demo import TestDemoCase


def main():
    suite = unittest.TestSuite()

    # tests = [TestDemoCase("test_add"), TestMathFunc("test_minus"), TestMathFunc("test_divide")]
    suite.addTests(unittest.TestLoader().loadTestsFromTestCase(TestDemoCase))
    # suite.addTests(tests)

    with open('UnittestTextReport.txt', 'w') as f:
        runner = unittest.TextTestRunner(stream=f, verbosity=2)
        runner.run(suite)
    # runner = unittest.TextTestRunner(verbosity=2)
    # runner.run(suite)


if __name__ == '__main__':
    main()