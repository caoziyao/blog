# coding: utf-8

import os
from app.untils import log


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
        dirlist = path.split('/')[:-1]
        parents = sep.join(dirlist)

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

    def format_path(self, path):
        """
        文件路径 / 用 @ 代替
        :return:
        """
        sep = self.separator
        path = path.replace('/', sep)
        return path

    def all_files(self):
        """
        该文件夹下所有 文件 和 文件夹
        :return:
        """
        folder = self.path
        # 列出目录下的所有文件和目录
        file_list = os.listdir(folder)
        file_list = self.ignore_file(file_list)

        files, dirs = [], []
        for l in file_list:

            path = os.path.join(folder, l)
            dir = {
                'filename': l,
                'path': self.format_path(path),
            }

            if os.path.isdir(path):
                dirs.append(dir)
            elif os.path.isfile(path):
                files.append(dir)
            else:
                pass

        pdir = self.parent_path(folder)
        d = {
            'current': self.current_path(),
            'parent': pdir,
            'dirs': dirs,
            'files': files,
        }
        return d


    def list_all_files(self, path):
        """
        for root, dirs, files in os.walk(path, topdown=False):
        第一个为起始路径，
        第二个为起始路径下的文件夹,
        第三个是起始路径下的文件.
        """
        files_set = set()
        for root, dirs, files in os.walk(path, topdown=False):
            for name in files:
                files_set.add(name) if name.endswith('.md') else ''
        f = list(files_set)

        return f
