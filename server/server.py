# coding: utf-8

import os

"""
for root, dirs, files in os.walk(path, topdown=False):
第一个为起始路径，
第二个为起始路径下的文件夹,
第三个是起始路径下的文件.
"""


def files_from_path(path):
    files_set = set()
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            files_set.add(name) if name.endswith('.md') else ''
    f = list(files_set)

    return f
