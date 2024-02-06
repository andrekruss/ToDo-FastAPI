from src.infra.database.config.db_config import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(100), nullable=False)
    is_active = Column(Boolean, default=True)

    boards = relationship('Board', back_populates='user')
    
class Board(Base):
    __tablename__ = 'boards'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    title = Column(String(100), nullable=False)
    description = Column(String(255))
    is_active = Column(Boolean, default=True)

    user = relationship('User', back_populates='boards')
    