from __future__ import annotations

from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel


class Enrollment(BaseModel):
    __tablename__ = "enrollments"

    user_id: Mapped[str] = mapped_column(
        ForeignKey("users.id"),
        nullable=False,
    )

    webinar_id: Mapped[str] = mapped_column(
        ForeignKey("webinars.id"),
        nullable=False,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        default="registered",
    )

    user: Mapped["User"] = relationship(
        back_populates="enrollments",
    )

    webinar: Mapped["Webinar"] = relationship(
        back_populates="enrollments",
    )

    attendance = relationship(
        "Attendance",
        back_populates="enrollment",
        uselist=False,
    )