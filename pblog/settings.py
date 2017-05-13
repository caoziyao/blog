# coding: utf-8

import os


_DEFAULT_THEME = os.sep.join([os.path.dirname(os.path.abspath(__file__)), "themes"])


_DEFAULT_CONFIG = {'PATH': None,
                   'THEME': _DEFAULT_THEME,
                   'OUTPUT_PATH': 'output/',
                   'MARKUP': 'rst',
                   'STATIC_PATHS': ['css', 'images'],
                   'FEED_FILENAME': 'atom.xml',
                   'BLOGNAME': 'A Pelican Blog',
                   'BLOGURL': '',
                   'SAMPLES': 'samples'}


def read_settings(filename):
    """Load a Python file into a dictionary.
    """
    context = _DEFAULT_CONFIG.copy()
    if filename is None:
        pass

    return context