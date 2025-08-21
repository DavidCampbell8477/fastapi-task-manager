from uuid import UUID
from typing import Dict, List
from .schemas import Task, TaskCreate, TaskUpdate

tasks: Dict[UUID, Task] = {}


def create_task(task_create: TaskCreate) -> Task:
    task = Task(**task_create.dict())
    tasks[task.uuid] = task
    return task


def get_task(task_uuid: UUID) -> Task:
    return tasks.get(task_uuid)


def get_tasks() -> List[Task]:
    return list(tasks.values())


def update_task(task_uuid: UUID, task_update: TaskUpdate) -> Task:
    task = tasks.get(task_uuid)
    if not task:
        return None
    updated_data = task_update.dict(exclude_unset=True)
    for key, value in updated_data.items():
        setattr(task, key, value)
    tasks[task_uuid] = task
    return task


def delete_task(task_uuid: UUID) -> bool:
    return tasks.pop(task_uuid, None) is not None
