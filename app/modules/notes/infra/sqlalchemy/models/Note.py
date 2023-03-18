from sqlalchemy import Column, Integer, String

from app.shared.infra.sqlalchemy.orm import Base

class Note(Base):
  __tablename__ = "notes"

  id = Column(Integer, primary_key=True, index=True)
  title = Column(String)
  content = Column(String)
