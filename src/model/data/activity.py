from sqlalchemy.orm import relationship
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model.base.database import Base
from model.data.page import Page


class Activity(Base):
    __tablename__ = 'activity'

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, nullable=False)
    image = Column(String, unique=True, nullable=False)
    description = Column(String)

    page = relationship(Page)
