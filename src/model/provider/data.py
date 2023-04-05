from model.base.database import Base
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer

class Provider(Base):
    __tablename__ = 'provider'

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False, unique=True)
    avatar = Column(String, nullable=False, unique=True)
    url = Column(String, nullable=False, unique=True)
    description = Column(String, nullable=False)
