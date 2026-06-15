from sqlalchemy import Column, String, Integer
from database import Base


class TaskDB(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    status = Column(String, default="new", index=True)
    priority = Column(String, default="medium", index=True)