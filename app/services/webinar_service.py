from app.repositories.webinar_repository import WebinarRepository
from app.schemas.webinar_schema import WebinarCreate


class WebinarService:

    def __init__(
        self,
        repository: WebinarRepository,
    ):
        self.repository = repository

    def get_all_webinars(self):
        return self.repository.get_all()

    def create_webinar(
        self,
        webinar: WebinarCreate,
    ):
        return self.repository.create(webinar)
