from sqlalchemy.orm import Session
from app.models import Task
from app.database import SessionLocal

# Optional helper for CLI or apps that need a session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Function to add a task
def add_task(db: Session, title: str) -> Task:
    task = Task(title=title)
    db.add(task)
    db.commit()
    db.refresh(task)
    return task

# Function to list all tasks
def list_tasks(db: Session) -> list[Task]:
    return db.query(Task).order_by(Task.id).all()

# Function to mark a task as completed
def mark_task_done(db: Session, task_id: int) -> bool:
    task = db.get(Task, task_id)
    if not task:
        return False
    task.done = True
    db.commit()
    return True

# Function to delete a task
def delete_task(db: Session, task_id: int) -> bool:
    task = db.get(Task, task_id)
    if not task:
        return False
    db.delete(task)
    db.commit()
    return True