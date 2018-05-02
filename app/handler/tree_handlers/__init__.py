# coding: utf-8


from .tree_handler import TreeHandler
from .tree_node_handler import TreeNodeLoadHandler
from .tree_node_save_handler import TreeNodeSaveHandler


handlers = [
    (r'/api/tree/get_tree_root', TreeHandler),
    (r'/api/tree/load_note', TreeNodeLoadHandler),
    (r'/api/tree/save_note', TreeNodeSaveHandler),
]


__all__ = [
    handlers,
]
