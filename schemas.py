from pydantic import BaseModel, Field
from typing import Literal
import uuid
from datetime import datetime

class TaskCreateSchema(BaseModel):
    title: str = Field(..., min_length=1, max_length=255)  # Title validation

class TaskResponseSchema(BaseModel):
    id: str
    title: str
    status: Literal["pending", "approved", "failed"]
    created_at: datetime
