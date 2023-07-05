from flask import request, make_response
from .common import ViewObject
from ..services import SearchService, UpdateService
import json

class SearchView(ViewObject):

    _search_svc = SearchService()
    _update_svc = UpdateService()

    def __init__(self):
        super().__init__("search", __name__, "/")
        bp = self.bp

        @bp.route("/search", methods=["GET"])
        def search():
            if request.method=="GET":
                # request.args.get("name")
                region = "kr"
                name = "때리는걸잘해요"
                self._update_svc.update(region=region, name=name, start=0, count=3)
                result = self._search_svc.search(region, name, 0, 3)
                result = json.dumps(result, ensure_ascii=False)
                res = make_response(result)

                return res