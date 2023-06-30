from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model.base.database import Base


class Endpoint(Base):
    __tablename__ = "endpoint"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    activity_id = Column(ForeignKey("activity.id"), nullable=False)
    provider_id = Column(ForeignKey("provider.id"), nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    status = Column(Integer, nullable=False, default=200)
