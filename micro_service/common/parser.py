# coding: utf-8
"""
@author: csy
@license: (C) Copyright 2017-2018
@contact: wyzycao@gmail.com
@time: 2018/9/2 
@desc:
"""

import argparse


def parse_args():

    parser = argparse.ArgumentParser()

    parser.add_argument("-l", help="list of micro service")
    parser.add_argument("-h", "--help", help="help of services")

    args = parser.parse_args()

