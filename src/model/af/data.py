from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model.base.database import Base
from model.provider.data import Provider


class Endpoint(Base):
    __tablename__ = "af_endpoint"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    activity_id = Column(Integer, ForeignKey('af_activity.id'), nullable=False)
    provider_id = Column(Integer, ForeignKey('provider.id'), nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, unique=True, nullable=False)
    status = Column(Integer, nullable=False, default=200)

    provider = relationship(Provider)


class Activity(Base):
    __tablename__ = 'af_activity'

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    name = Column(String, unique=True, nullable=False)
    time = Column(DateTime, unique=True, nullable=False)
    image = Column(String, unique=True, nullable=False)
    description = Column(String)
