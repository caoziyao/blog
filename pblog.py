# coding: utf-8
#!/usr/bin/python

import argparse
import os


from pblog.generator import generate_output, generate_file, new_acticle, \
    generate_blog

from pblog.server import run_server


parser = argparse.ArgumentParser(description="some information here")

# 例子
# 输入 python3 pblog.py -init hello
# args.projectName 值为 hello
parser.add_argument('-p', '--path', dest='path',
    help='Path where to find the content files (default is "content").')


parser.add_argument('-init', dest='project_name',
    help='the settings of the application. Default to None.')

parser.add_argument('-setting', dest='settings',
    help='the settings of the application. Default to None.')

parser.add_argument('-new', dest='article_name',
    help='the settings of the application. Default to None.')

# 当指定--generate时程序就显示一些东西，没指定的时候就不显示
parser.add_argument( '-g', '--generate', action="store_true",
    help='the settings of the application. Default to None.')

parser.add_argument( '-s', '--server', action="store_true",
    help='the settings of the application. Default to None.')



def run(args):
    """
    程序入口
    :param args:
    :return:
    """
    if args.project_name is not None:
        print('init project {}'.format(args.project_name))
        args.project_name = 'testblog'    # 调试默认为 testblog
        # 生成空项目
        generate_output(args.project_name, settings=args.settings)

    if args.article_name is not None:
        # 生成文章
        new_acticle(args.article_name)

    # 渲染生成 html 文件
    if args.generate is True:
        generate_file()

    # 启动服务
    if args.server is True:
        run_server()

    print('Done!')


if __name__ == '__main__':
    args = parser.parse_args()
    try:
        run(args)
    except Exception as e:
        print('error !', e)
