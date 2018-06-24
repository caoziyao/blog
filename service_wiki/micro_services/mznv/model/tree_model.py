# coding: utf-8

# from .base_model import BaseModel
from app.database import Base

class NodeModel(object):

    def __init__(self, data=None):
        super(NodeModel, self).__init__()
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class TreeModel(object):

    def __init__(self, root):
        super(TreeModel, self).__init__()
        """
        root: NodeModel()
        :param root:
        """
        self.root = root

    def traverse(self, root):
        res = []
        for child in root.children:
            child_data = child.data
            child_data['children'] = []
            child_data['children'].extend(self.traverse(child))
            res.append(child_data)
        return res

    def format_dict(self):
        """
        var data = {
            name: 'notebook',
            isFolder: true,
            children: [{
                    name: 'hell',
                    isFolder: false,
                },{
                    name: 'abccd',
                    isFolder: true,
                    children: [],
                },
            ],
        };
        :return:
        """
        res = {}
        root = self.root
        root_data = self.root.data
        res.update(root_data)
        res['children'] = []
        res['children'].extend(self.traverse(root))
        return res