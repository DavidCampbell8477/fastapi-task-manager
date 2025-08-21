from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from enum import Enum
from typing import Optional


class StatusEnum(str, Enum):
    created = "created"
    in_progress = "in_progress"
    completed = "completed"


class TaskBase(BaseModel):
    name: str = Field(..., example="Finish project")
    description: Optional[str] = Field(None, example="Complete API implementation")
    status: StatusEnum = StatusEnum.created


class TaskCreate(TaskBase):
    pass


class TaskUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    status: Optional[StatusEnum] = None


class Task(TaskBase):
    uuid: UUID = Field(default_factory=uuid4)
