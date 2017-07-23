import datetime
from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
    String,
    Datetime,
)

from .meta import Base


class MyModel(Base): #TODO: Remove
    __tablename__ = 'models'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    value = Column(Integer)

class request_log(Base):
    __tablename__ = 'request_log'
    id = Column(Integer, primary_key=True)
    ip = Column(String)
    values = Column(String)
    date = Column(Datetime, default=datetime.now)

class access_log(Base):
    __tablename__ = 'access_log'
    id = Column(Integer, primary_key=True)
    ip = Column(String)
    requests = Column(Integer)
    last_request = Column(Datetime)
    ban_count = column(Integer)

class banlist(Base):
    __tablename__ = 'banlist'
    id = Column(Integer, primary_key=True)
    ip = Column(String)
    ban_time = Column(Datetime)
    expire = Column(Datetime)
    
Index('my_index', MyModel.name, unique=True, mysql_length=255)
