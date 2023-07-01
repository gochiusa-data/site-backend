from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import DateTime
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model.base.database import Base
from model.data.endpoint import Endpoint


class Page(Base):
    __tablename__ = "page"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    activity_id = Column(Integer, ForeignKey("activity.id"), nullable=False)
    name = Column(String, nullable=False)
    time = Column(DateTime, nullable=False)
    image = Column(String, unique=True, nullable=False)
    description = Column(String)

    endpoint = relationship(Endpoint)