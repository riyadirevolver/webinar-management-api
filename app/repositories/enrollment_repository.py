from sqlalchemy.orm import Session

from app.models.enrollment import Enrollment


class EnrollmentRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        enrollment: Enrollment,
    ):
        self.db.add(enrollment)
        self.db.commit()
        self.db.refresh(enrollment)

        return enrollment

    def get_by_user_and_webinar(
        self,
        user_id: str,
        webinar_id: str,
    ):
        return (
            self.db.query(Enrollment)
            .filter(
                Enrollment.user_id == user_id,
                Enrollment.webinar_id == webinar_id,
            )
            .first()
        )

    def get_by_user(
        self,
        user_id: str,
    ):
        return (
            self.db.query(Enrollment)
            .filter(
                Enrollment.user_id == user_id,
            )
            .all()
        )

    def get_by_webinar(
        self,
        webinar_id: str,
    ):
        return (
            self.db.query(Enrollment)
            .filter(
                Enrollment.webinar_id == webinar_id,
            )
            .all()
        )

    def count_participants(
        self,
        webinar_id: str,
    ):
        return (
            self.db.query(Enrollment)
            .filter(
                Enrollment.webinar_id == webinar_id,
            )
            .count()
        )

    def delete(
        self,
        enrollment: Enrollment,
    ):
        self.db.delete(enrollment)
        self.db.commit()
