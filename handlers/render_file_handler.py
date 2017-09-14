# coding: utf-8

import markdown
import os
import base64

class RenderFileHandler():

    def __init__(self, path):
        self.path = path

    def file_extension(self):
        """ 获取文件拓展名,如test.doc,返回.doc
        """
        path = self.path
        extent = os.path.splitext(path)[1]

        # file_type = extent[1:]
        # self.file_type = file_type

        return extent

    def content_from_file(self):
        """
        读取文件内容
        :return:
        """
        path = self.path
        if not os.path.exists(path):
            raise FileNotFoundError('文件找不到')

        if os.path.isfile(path):
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
                return content
        else:
            raise IsADirectoryError('不是文件')

    def bytes_from_file(self):
        """
        2进制 读取文件内容
        :return:
        """
        path = self.path
        if not os.path.exists(path):
            raise FileNotFoundError('文件找不到')

        if os.path.isfile(path):
            with open(path, 'rb') as f:
                content = f.read()
                return content
        else:
            raise IsADirectoryError('不是文件')


    def render_img(self):
        """
        图片格式
        :return: base64
        """
        data = self.bytes_from_file()
        data = base64.b64encode(data).decode('utf-8')

        extent = self.file_extension()
        file_type = extent[1:]
        data = 'data:image/{};base64,'.format(file_type) + data
        return data

    def render_file(self):
        """
        根据不同格式读取文件内容
        :return:
        """
        extent = self.file_extension()


        if extent == '.md':
            html = self.render_markdown()
        elif extent in ['.jpg', '.png', '.gif']:
            html = self.render_img()
        else:
            html = self.content_from_file()

        return html


    def render_markdown(self):
        """
        解读 md 格式
        :return:
        """
        content = self.content_from_file()
        html = markdown.markdown(content)

        return html