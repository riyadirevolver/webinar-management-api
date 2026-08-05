from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class WebinarCreate(BaseModel):
    title: str
    description: str
    speaker: str
    start_time: datetime
    end_time: datetime
    capacity: int


class WebinarResponse(BaseModel):
    id: UUID
    title: str
    description: str
    speaker: str
    start_time: datetime
    end_time: datetime
    capacity: int
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True
    )
