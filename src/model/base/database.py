from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# 基础设置
path = "sqlite:///../database.db"
engine = create_engine(path, connect_args={"check_same_thread": False})

# 通用
DBsession = sessionmaker(autoflush=True, bind=engine)
Base = declarative_base()
