from ..repositories import *
from ..services import *

from .search import SearchView


def get_blueprints():
    return [SearchView().bp]

# def get_blueprints():
#     return [CustomizeModelTestView().bp]