from fastapi import FastAPI, HTTPException
from uuid import UUID
from .schemas import TaskCreate, TaskUpdate, Task
from .crud import create_task, get_task, get_tasks, update_task, delete_task

app = FastAPI(title="Task Manager API")


@app.post("/tasks/", response_model=Task)
def api_create_task(task: TaskCreate):
    return create_task(task)


@app.get("/tasks/{task_uuid}", response_model=Task)
def api_get_task(task_uuid: UUID):
    task = get_task(task_uuid)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.get("/tasks/", response_model=list[Task])
def api_get_tasks():
    return get_tasks()


@app.put("/tasks/{task_uuid}", response_model=Task)
def api_update_task(task_uuid: UUID, task_update: TaskUpdate):
    task = update_task(task_uuid, task_update)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task


@app.delete("/tasks/{task_uuid}")
def api_delete_task(task_uuid: UUID):
    if not delete_task(task_uuid):
        raise HTTPException(status_code=404, detail="Task not found")
    return {"detail": "Task deleted successfully"}
