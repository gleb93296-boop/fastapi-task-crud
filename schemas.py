from pydantic import BaseModel, Field


class TaskSchemas(BaseModel):
    id: int
    title: str
    description: str
    status: str
    priority: str

    model_config={"from_attributes": True}


class TaskCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=25)
    description: str = Field(..., min_length=15, max_length=100)


class TaskListResponse(BaseModel):
    status: str
    message: str
    card: list[TaskSchemas]


class SingleTaskResponse(BaseModel):
    status: str
    message: str
    card: TaskSchemas
