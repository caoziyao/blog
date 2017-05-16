# coding: utf-8

import os, sys
import shutil, datetime, markdown
from functools import partial
from pblog.settings import read_settings
from pblog.utils import endwith
from pblog.utils import project_name, output_path, CONF


class Generator(object):
    """
    Base class generator
    """
    def __init__(self):
        project_name = 'samples'
        self.settings = read_settings(project_name)
        self.project_name = project_name
        print(self.settings)

        for k, v in self.settings:
            CONF[k] = v
        # CONF['project_name'] = project_name


class ArticlesGenerator(Generator):
    """Represents an article.
    Given a string, complete it's properties from here.

    :param string: the string to parse, containing the original content.
    :param markup: the markup language to use while parsing.
    """
    def __init__(self):
        super(ArticlesGenerator).__init__()
        self.articles = []
        self.dates = {}
        self.years = {}
        self.tags = {}
        self.categories = {}



    def base_file(self):
        """
        创建文件基础
        :return:
        """
        supart = 'super_article.md'
        project_name = CONF['project_name']
        supart_path = os.path.join(project_name, 'content', supart)
        with open(supart_path, 'r') as f:
            return f.read()

    def generate_article(self, filename):
        """
        创建新文件
        使用命令 pblog new filename 调用
        :param filename:
        :return:
        """
        project_name = CONF['project_name']
        strtime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        supart = self.base_file()
        super_article = supart.replace('TITLE', filename).replace('DATE', strtime)
        filename = filename + '.md'
        with open(output_path, 'w+') as f:
            f.write(super_article)
        print(filename)


    def generate_static_content(self):
        pass


    def generate_static_output(self):
        """
        渲染生成改动的新文件
        使用命令 pblog -g 调用
        :return:
        """
        content_path = os.path.join(project_name, 'content')

        # 搜索后缀名为 .md 文件
        files_set = set()
        for root, dirs, files in os.walk(content_path, topdown=False):
            for name in files:
                files_set.add(name) if name.endswith('.md') else ''
        content_list = list(files_set)

        # 生成 html 文件
        for md in content_list:
            mfile = os.path.join(content_path, md)
            htmlfilename = md.split('.', 1)[0] + '.html'
            htmlfile = os.path.join(output_path, htmlfilename)
            with open(mfile, 'r') as f:
                txt = f.read()
                html = markdown.markdown(txt)
                with open(htmlfile, 'w+') as f:
                    print('generate {}'.format(htmlfile))
                    f.write(html)


    def generate_configfile(self):
        pass


    def generate_blog(self, blogname):
        """Search the given path for files, and generate a static blog in output,
        using the given theme.
        """
        if not os.path.exists(blogname):
            os.mkdir(blogname)
            os.mkdir(output_path)
            self.generate_static_content()
            self.generate_configfile()

        else:
            print('{} exists'.format(blogname))


    def generate_output(self, path=None, settings=None):
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


