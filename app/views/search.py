from flask import request, make_response
from .common import ViewObject
from ..services import SearchSvc, UpdateSvc
import json

class SearchView(ViewObject):

    __search_svc__ = SearchSvc()
    __update_svc__ = UpdateSvc()

    def __init__(self):
        super().__init__("search", __name__, "/")
        bp = self.bp

        @bp.route("/search", methods=["GET"])
        def search():
            if request.method=="GET":
                # request.args.get("name")
                region = "kr"
                name = "여자맨"
                self.__update_svc__.update(region, name=name)
                result = self.__search_svc__.search(region, name)
                result = json.dumps(result, ensure_ascii=False)
                res = make_response(result)

                return res