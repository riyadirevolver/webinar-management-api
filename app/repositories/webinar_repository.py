from sqlalchemy.orm import Session

from app.models.webinar import Webinar
from app.schemas.webinar_schema import WebinarCreate


class WebinarRepository:

    def __init__(self, db: Session):
        self.db = db

    def get_all(self):
        return self.db.query(Webinar).all()

    def get_by_id(self, webinar_id: str):
        return (
            self.db.query(Webinar)
            .filter(Webinar.id == webinar_id)
            .first()
        )

    def create(
        self,
        webinar: WebinarCreate,
    ):
        db_webinar = Webinar(
            **webinar.model_dump()
        )

        self.db.add(db_webinar)
        self.db.commit()
        self.db.refresh(db_webinar)

        return db_webinar
