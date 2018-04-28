# coding: utf-8


class Node(object):

    def __init__(self, data=None):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class Tree(object):

    def __init__(self, root):
        """
        root: Node()
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