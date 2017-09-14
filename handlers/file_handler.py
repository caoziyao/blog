# coding: utf-8

import os
from untils import log
from config.constant import SEPARATOR
"""
for root, dirs, files in os.walk(path, topdown=False):
第一个为起始路径，
第二个为起始路径下的文件夹,
第三个是起始路径下的文件.
"""

class FileHandler():

    def __init__(self, path):
        self.path = path
        self.separator = '@'


    def parent_path(self, path):
        """
        父文件夹路径，/ 用 @ 代替
        :return:
        """
        sep = self.separator
        if path == self.path:
            parents = path.replace('/', sep)
        else:
            parents = path

        return parents

    def current_path(self):
        """
        当前文件夹路径
        :return:
        """
        path = self.path
        sep = self.separator
        current = path.replace('/', sep)

        return current

    def ignore_file(self, file_list):
        """
        忽略 . 开头文件
        :param file_list: 文件列表
        :return: 文件列表
        """
        l = filter(lambda x: x[0] != '.', file_list)

        return l

    def all_files(self):
        """

        :return:
        """
        folder = self.path
        # 列出目录下的所有文件和目录
        file_list = os.listdir(folder)

        files, dirs = [], []

        file_list = self.ignore_file(file_list)
        for l in file_list:

            path = os.path.join(folder, l)
            dir = {
                'filename': l,
                'path': path.replace('/', SEPARATOR),
            }
            if os.path.isdir(path):
                dirs.append(dir)
            elif os.path.isfile(path):
                files.append(dir)
            else:
                pass

        pdir = self.parent_dir_from(folder)

        d = {
            'current': folder.replace('/', SEPARATOR),
            'parent': pdir,
            'dirs': dirs,
            'files': files,
        }
        return d



    def list_all_files(self, path):
        files_set = set()
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                files_set.add(name) if name.endswith('.md') else ''
        f = list(files_set)

        return f


    def parent_dir_from(self, folder):

        dirlist = folder.split('/')[:-1]
        # dirlist = [x for x in dirlist if x != '']
        path = SEPARATOR.join(dirlist)
        return path
