from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.orm import declarative_base

# 🔧 This sets up the base class for all ORM models
Base = declarative_base()

# ✅ This defines your Task model (a table in the database)
class Task(Base):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    done = Column(Boolean, default=False)

    def __repr__(self):
        return f"<Task(id={self.id}, title='{self.title}', done={self.done})>"
