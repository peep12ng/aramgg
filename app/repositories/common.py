from ..extensions import db
from sqlalchemy.inspection import inspect

class RepoObject:
    __session__ = db.session
    __model__ = None
    __updates__ = []

    def save(self):
        self.__session__.commit()
        self.__session__.close()
    
    def all(self):
        return self.__model__.query.all()
    
    def _first(self, query):
        return query.first()
    
    def _all(self, query):
        return query.all()
    
    def _find(self, **kwargs):
        return self.__model__.query.filter_by(**kwargs)
    
    def _slice(self, query, start, count):
        return query.slice(start, count)
    
    def _select(self, query, columns):
        return query.with_entities(*[getattr(self.__model__, column) for column in columns])
    
    def all_ids(self):
        ids = self.__model__.query.with_entities(getattr(self.__model__, self._pk_name)).all()
        return [id[0] for id in ids]
    
    def get(self, id):
        return self.__model__.query.get(id)
    
    def find(self, **kwargs):
        return self._all(self._find(**kwargs))
    
    def find_n(self, start, count, **kwargs):
        return self._find(**kwargs).paginate(page=start, per_page=count).all()
    
    def first(self, **kwargs):
        return self._find(**kwargs).first()
    
    def new(self, **kwargs):
        return self.__model__(**kwargs)

    def insert(self, obj):
        self.__session__.add(obj)
        self.save()

        return obj
    
    def updates_to_dict(self, obj):
        d = {}
        for c in self.__updates__:
            d[c] = getattr(obj, c)
        
        return d
    
    def update(self, obj):
        pk = self.get_pk(obj)
        d = self.updates_to_dict(obj)

        self.__model__.query.filter(getattr(self.__model__, self._pk_name)==pk).update(d)
        self.save()
        return self.get(pk)
    
    def delete(self, obj):
        self.__session__.delete(obj)
        self.save()
    
    def exists(self, id):
        if self.get(id):
            return True
        else:
            return False
        
    def get_pk(self, obj):
        return getattr(obj, self._pk_name)
    
    @property
    def _pk_name(self):
        return inspect(self.__model__).primary_key[0].name
    
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