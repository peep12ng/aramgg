from ..extensions import db, ModelObject

class RepoObject:
    __session__ = db.session
    __model__: ModelObject = None
    __updates__ = []
    _query = None

    @property
    def create_query(self):
        self._query = self.__model__.query
        return self

    def all(self):
        return self._query.all()
    
    def first(self) -> ModelObject:
        return self._query.first()
    
    def new(self, **kwargs:dict) -> ModelObject:
        return self.__model__(**kwargs)

    def get(self, id) -> ModelObject:
        return self.__model__.query.get(id)
    
    def insert(self, obj:ModelObject):
        self.__session__.add(obj)
        pk = obj.pk_value
        self.save()

        return self.get(pk)
    
    def save(self):
        self.__session__.commit()
        self.__session__.close()
    
    def delete(self, id):
        obj = self.get(id)
        self.__session__.delete(obj)
        self.save()

    def update(self, obj:ModelObject):
        pk = obj.pk_value
        self.create_query.find(**{obj.pk_name:pk})._update(obj)
        self.save()

        return self.get(pk)
    
    def _update(self, obj:ModelObject):
        self._query.update({k:getattr(obj, k) for k in obj.update_only})
    
    def find(self, **kwargs):
        self._query = self._query.filter_by(**kwargs)
        return self
    
    def select(self, columns:list[str]):
        self._query = self._query.with_entities(*[getattr(self.__model__, column) for column in columns])
        return self
    
    def slice(self, start, count):
        self._query = self._query.slice(start, count)
        return self
    
    def exists(self, id) -> bool:
        return bool(self.get(id))
    
    def order_by(self, columns:list[str]):
        self._query = self._query.order_by(*[getattr(self.__model__, column) for column in columns])
        return self
    
    def filter_in(self, column, values:list):
        self._query = self._query.filter(getattr(self.__model__, column).in_(values))
        return self
    
    @property
    def zeros(self):
        d = {}
        columns = self.__model__.__table__.columns

        for k, v in columns.items():
            if str(v.type).startswith("INTEGER"):
                d[k] = 0
            elif str(v.type).startswith("BOOLEAN"):
                d[k] = False
            else:
                d[k] = None

        return d