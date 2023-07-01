from sqlalchemy.orm import relationship
from sqlalchemy import ForeignKey
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy import Integer
from model.base.database import Base
from model.data.provider import Provider


class Endpoint(Base):
    __tablename__ = "endpoint"

    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True, nullable=False)
    provider_id = Column(Integer, ForeignKey("provider.id"), nullable=False)
    page_id = Column(Integer, ForeignKey("page.id"), nullable=False)
    name = Column(String, nullable=False)
    url = Column(String, nullable=False)
    status = Column(Integer, nullable=False, default=200)

    provider = relationship(Provider)
