from app.models.enrollment import Enrollment
from app.models.user import User
from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.webinar_repository import WebinarRepository
from app.schemas.enrollment_schema import EnrollmentCreate


class EnrollmentService:

    def __init__(
        self,
        repository: EnrollmentRepository,
        webinar_repository: WebinarRepository,
    ):
        self.repository = repository
        self.webinar_repository = webinar_repository

    def register(
        self,
        user: User,
        data: EnrollmentCreate,
    ):

        webinar = self.webinar_repository.get_by_id(
            data.webinar_id,
        )

        if webinar is None:
            raise Exception("Webinar not found")

        existing = self.repository.get_by_user_and_webinar(
            str(user.id),
            data.webinar_id,
        )

        if existing:
            raise Exception(
                "Already registered",
            )

        participant_count = (
            self.repository.count_participants(
                data.webinar_id,
            )
        )

        if participant_count >= webinar.capacity:
            raise Exception(
                "Webinar is full",
            )

        enrollment = Enrollment(
            user_id=str(user.id),
            webinar_id=data.webinar_id,
        )

        return self.repository.create(
            enrollment,
        )

    def get_my_webinars(
        self,
        user: User,
    ):
        return self.repository.get_by_user(
            str(user.id),
        )
