# coding: utf-8
#!/usr/bin/env python
from setuptools import setup

setup(
    name='pblog',
    version='1.0.0.dev1',
    description='A simple weblog generator python project',
    url='https://github.com/caoziyao/pblog',
    author='CXZY',
    author_email='wycsyao@163.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    keywords='weblog frame python',
    packages=['pblog'],
)


# name为项目名称，和顶层目录名称一致;
# version是项目当前的版本，1.0.0.dev1表示1.0.0版，目前还处于开发阶段
# description是包的简单描述，这个包是做什么的
# url为项目访问地址，我的项目放在github上。
# author为项目开发人员名称
# author_email为项目开发人员联系邮件
# license为本项目遵循的授权许可
# classifiers有很多设置，具体内容可以参考官方文档
# keywords是本项目的关键词，理解为标签
# packages是本项目包含哪些包,我这里只有一个名词为hive的包
