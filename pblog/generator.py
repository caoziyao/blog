# coding: utf-8

import os
import shutil

_DEFAULT_THEME = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "themes"])
_DEFAULT_CONFIG = {'PATH': None,
                   'THEME': _DEFAULT_THEME,
                   'OUTPUT_PATH': 'output/',
                   'MARKUP': 'rst',
                   'STATIC_PATHS': ['css', 'images'],
                   'FEED_FILENAME': 'atom.xml',
                   'BLOGNAME': 'A Pelican Blog',
                   'BLOGURL': ''}

def read_settings(filename):
    """Load a Python file into a dictionary.
    """
    context = _DEFAULT_CONFIG.copy()
    if filename is None:
        pass




    return context


def generate_output(path=None, settings=None):
    """Given a list of files, a template and a destination,
    output the static files.

    :param path: the path where to find the files to parse
    :param theme: where to search for templates
    :param output_path: where to output the generated files
    :param markup: the markup language to use while parsing
    :param settings: the settings file to use
    """
    # 生成项目
    context = read_settings(settings)
    path = path or context['PATH']
    theme = context['THEME']
    output_path = context['OUTPUT_PATH']

    # 如果不存在项目，则创建
    if not os.path.exists(path):
        os.mkdir(path)
        try:
            src = 'samples'
            dst = path
            shutil.copytree(src, dst)
        except OSError:
            pass


