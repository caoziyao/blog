# coding: utf-8
#!/usr/bin/python

import argparse
import os


from pblog.generator import generate_output


parser = argparse.ArgumentParser(description="some information here")


parser.add_argument('-p', '--path', dest='path',
    help='Path where to find the content files (default is "content").')


parser.add_argument('-init', dest='projectName',
    help='the settings of the application. Default to None.')

parser.add_argument('-setting', dest='settings',
    help='the settings of the application. Default to None.')

parser.add_argument('-new', dest='articleName',
    help='the settings of the application. Default to None.')

# 当指定--generate时程序就显示一些东西，没指定的时候就不显示
parser.add_argument( '-g', '--generate', action="store_true",
    help='the settings of the application. Default to None.')

parser.add_argument( '-s', '--server', action="store_true",
    help='the settings of the application. Default to None.')


if __name__ == '__main__':
    args = parser.parse_args()
    files = []
    # 例子
    # 输入 python3 pblog.py -init hello
    # args.projectName 值为 hello
    if args.projectName is not None:
        print('init project {}'.format(args.projectName))
        args.projectName = 'testblog'    # 调试默认为 testblog
        generate_output(args.projectName, settings=args.settings)

    # 渲染生成 html 文件
    if args.generate is True:
        pass

    # 启动服务
    if args.server is True:
        pass
