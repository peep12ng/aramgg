from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy.model import Model, DefaultMeta
from flask_migrate import Migrate
from sqlalchemy import orm
from sqlalchemy.inspection import inspect

from typing import Tuple

# def my_declarative_constructor(self, **kwargs):
#     orm.decl_base._declarative_constructor(self, **kwargs)

def my_declarative_constructor(self, **kwargs):
    cls_ = type(self)
    for k in kwargs:
        if hasattr(cls_, k):
            setattr(self, k, kwargs[k])

class ModelObject(Model):

    serialize_only: Tuple[str, ...] = None
    serialize_rules: Tuple[str, ...] = None
    update_only: Tuple[str, ...] = None

    def serialize(self):

        result = {}

        _columns = self.__table__.columns.keys()
        columns = []
        if self.serialize_only!=None:
            columns = list(self.serialize_only)
        elif self.serialize_rules!=None:
            columns = list(set(_columns)-set(self.serialize_rules))
        else:
            columns = list(_columns)
        
        for c in columns:
            result[c] = getattr(self, c)

        return result
    
    @property
    def pk_value(self):
        return getattr(self, self.pk_name)
    
    @property
    def pk_name(self):
        return inspect(self.__class__).primary_key[0].name

Base = orm.declarative_base(
    constructor=my_declarative_constructor, metaclass=DefaultMeta, cls=ModelObject
)

db = SQLAlchemy(model_class=Base)
migrate = Migrate()

# db = SQLAlchemy()
# migrate = Migrate()

# 기존의 _declarative_constructor는
# kwargs를 대상으로 for문을 돌기 때문에
# poro에서 속성을 지워주어야함
# -> 모델 클래스 속성과 poro Ghost 클래스 속성을 1:1로 일치시켜야 한다는 뜻
# -> 대신 onupdate이나 default 값이 있는 속성을 자동으로 처리해주는 것으로 예상
# 1. columns를 대상으로 도는 base를 구현하거나
# 2. poro에서 속성들을 수정해야함
#  -> 하나의 row를 insert 할 때마다 columns만큼 for문을 돌아야 하기 때문에
#  -> poro 딴에서 필요한 속성들만 솎아주는게 성능이 더 좋을 듯?
#  -> 이러면 하나의 서비스라고 봐도 무방 ㅇㅇ
#  -> 문제점:continent, match_history
#  -> 이러나 저러나 columns따라 반복문 돌리는건 매한가지??