from flask import Blueprint

class ViewObject:

    __service__ = None

    def __init__(self, name, import_name, url_prefix):
        self._bp = Blueprint(name=name, import_name=import_name, url_prefix=url_prefix)

    @property
    def bp(self):
        return self._bp