from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel

app = FastAPI(title="Task API")

tasks = [
    {"id": 1, "title": "Estudar Python", "completed": False},
]
next_task_id = 2


class TaskCreate(BaseModel):
    title: str


class TaskUpdate(BaseModel):
    title: str | None = None
    completed: bool | None = None


@app.get("/tasks")
def list_tasks():
    return tasks


@app.post("/tasks", status_code=status.HTTP_201_CREATED)
def create_task(task: TaskCreate):
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    pass


@app.patch("/tasks/{task_id}")
def update_task(task_id: int, updates: TaskUpdate):
    pass


@app.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(task_id: int):
    pass
