from sqlalchemy import (
    Column,
    Index,
    Integer,
    Text,
)

from .meta import Base


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text)
    username = Column(Text)
    password = Column(Text)
    role = Column(Text)
    

