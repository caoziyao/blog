# coding: utf-8

import os

"""
for root, dirs, files in os.walk(path, topdown=False):
第一个为起始路径，
第二个为起始路径下的文件夹,
第三个是起始路径下的文件.
"""

def list_all_files(path):
    files_set = set()
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            files_set.add(name) if name.endswith('.md') else ''
    f = list(files_set)

    return f


def parent_dir_from(folder):

    dirlist = folder.split('/')[:-1]
    # dirlist = [x for x in dirlist if x != '']
    path = '_'.join(dirlist)
    return path

def listdir(folder):
    ls = os.listdir(folder)  # 列出目录下的所有文件和目录
    parent = parent_dir_from(folder)
    files = []
    dirs = []
    for l in ls:
        path = os.path.join(folder, l)
        dir = {
            'filename': l,
            'path': path.replace('/', '_'),
        }
        if os.path.isdir(path):
            dirs.append(dir)
        elif os.path.isfile(path):
            files.append(dir)
        else:
            pass

    d = {
        'current': folder.replace('/', '_'),
        'parent': parent,
        'dirs': dirs,
        'files': files,
    }
    return d
