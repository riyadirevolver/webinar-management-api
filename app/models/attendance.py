from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Attendance(BaseModel):
    __tablename__ = "attendances"

    enrollment_id: Mapped[str] = mapped_column(
        ForeignKey("enrollments.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="present",
    )

    enrollment: Mapped["Enrollment"] = relationship(
        back_populates="attendance",
    )