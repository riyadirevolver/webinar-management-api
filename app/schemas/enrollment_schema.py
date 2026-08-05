from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict


class EnrollmentCreate(BaseModel):
    webinar_id: str


class EnrollmentResponse(BaseModel):
    id: UUID
    user_id: UUID
    webinar_id: UUID
    status: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )
