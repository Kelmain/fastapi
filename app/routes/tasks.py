from fastapi import APIRouter, HTTPException
from typing import List, Optional
from app.schemas import Task, TaskCreate, TaskUpdate
from app.database import tasks

router = APIRouter()

def get_next_id():
    return max([task.id for task in tasks], default=0) + 1

@router.get("/tasks/", response_model=List[Task])
def list_tasks(sort_by: Optional[str] = None, completed: Optional[bool] = None):
    filtered = tasks
    if completed is not None:
        filtered = [task for task in filtered if task.completed == completed]
    if sort_by == "title":
        filtered = sorted(filtered, key=lambda t: t.title.lower())
    elif sort_by == "completed":
        filtered = sorted(filtered, key=lambda t: t.completed)
    return filtered

@router.post("/tasks/", response_model=Task)
def create_task(task: TaskCreate):
    new_task = Task(id=get_next_id(), title=task.title, description=task.description, completed=False)
    tasks.append(new_task)
    return new_task

@router.put("/tasks/{id}", response_model=Task)
def update_task(id: int, task: TaskUpdate):
    for t in tasks:
        if t.id == id:
            t.title = task.title or t.title
            t.description = task.description if task.description is not None else t.description
            if task.completed is not None:
                t.completed = task.completed
            return t
    raise HTTPException(status_code=404, detail="Task not found")

@router.delete("/tasks/{id}")
def delete_task(id: int):
    for i, t in enumerate(tasks):
        if t.id == id:
            del tasks[i]
            return {"message": "Task deleted"}
    raise HTTPException(status_code=404, detail="Task not found")

@router.patch("/tasks/{id}/complete", response_model=Task)
def complete_task(id: int):
    for t in tasks:
        if t.id == id:
            t.completed = True
            return t
    raise HTTPException(status_code=404, detail="Task not found")
