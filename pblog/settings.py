# coding: utf-8

import os
import yaml


def read_settings(blogname):
    """Load a Python file into a dictionary.
    """
    blog_path = os.path.join(blogname, '_config.yml')
    with open(blog_path, 'r') as f:
        context = yaml.load(f)
        return context