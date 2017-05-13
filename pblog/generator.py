# coding: utf-8

import os, sys
import shutil, datetime, markdown
from functools import partial
from pblog.settings import read_settings




_PROJECT_NAME = 'testblog'




def endwith(*endstring):
    """筛选特定后缀名
    a = endWith('.jpeg', '.jpg', '.png')  # 只识别后缀名为 .jpeg .jpg .png
    files = ['22.jpeg', '111.exe']
    f_file = filter(a, files)  # 文件名列表
    :param endstring:
    :return:
    """
    ends = endstring
    def run(s):
        f = map(s.endswith, ends)
        if True in f: return s
    return run


def render_template(path, txt):
    """
    md 渲染成 html
    :param path:
    :param txt:
    :return:
    """
    html = markdown.markdown(txt)
    with open(path, 'w+') as f:
        f.write(html)


def generate_file():
    """
    渲染生成改动的新文件
    使用命令 pblog -g 调用
    :return:
    """
    a = endwith('.md')
    files_set = set()
    content_path = os.path.join(_PROJECT_NAME, 'content')
    for root, dirs, files in os.walk(content_path, topdown=False):
        for name in files:
            files_set.add(name) if name.endswith('.md') else ''

    # f_file = filter(a, files_set)
    md_list = list(files_set)

    for md in md_list:
        md_path = os.path.join(content_path, md)
        file_path = os.path.join(content_path, md.replace('md', 'html'))
        with open(md_path, 'r') as f:
            txt = f.read()
            render_template(file_path, txt)


def get_base_md():
    """
    创建文件基础
    :return:
    """
    supart = 'super_article.md'
    supart_path = os.path.join(_PROJECT_NAME, 'content', supart)
    with open(supart_path, 'r') as f:
        return f.read()


def new_acticle(filename):
    """
    创建新文件
    使用命令 pblog new filename 调用
    :param filename:
    :return:
    """
    strtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    supart = get_base_md()
    super_article = supart.replace('TITLE', filename).replace('DATETIME', strtime)
    filename = filename + '.md'
    output_path = os.path.join(_PROJECT_NAME, 'content', filename)
    with open(output_path, 'w+') as f:
        f.write(super_article)
    print(filename)



def generate_blog(blogname):
    """Search the given path for files, and generate a static blog in output,
    using the given theme.
    """
    pass




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
    src = context['SAMPLES']
    dst = path

    # 则创建项目，不管存在
    if os.path.exists(dst):
        print('已经存在 {} 目录'.format(dst))
        # return
    try:
        if os.path.exists(dst):
            print('但我还是删了')
            shutil.rmtree(dst)
        shutil.copytree(src, dst)
    except OSError:
        pass


class Generator(object):
    """
    Base class generator
    """
    def __init__(self, settings):
        self.settings = read_settings(settings)


class Article(object):
    """Represents an article.
    Given a string, complete it's properties from here.

    :param string: the string to parse, containing the original content.
    :param markup: the markup language to use while parsing.
    """
    def __init__(self):
        pass


