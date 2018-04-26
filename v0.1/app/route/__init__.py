# coding: utf-8

from .index import app as route_index
from .edit import app as route_edit
from .article import app as route_page
from .hot_spot import app as route_hot_spot
from .basis import app as route_basis


__all__ = [
    route_index,
    route_edit,
    route_page,
    route_hot_spot,
    route_basis,
]