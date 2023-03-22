from sqlalchemy import Column, Integer, String, Boolean, Identity

from app.shared.infra.sqlalchemy.orm import Base

class Note(Base):
  __tablename__ = 'notes'

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  completed = Column(Boolean, default=False)
  order = Column(Integer, autoincrement=True, default=0)
