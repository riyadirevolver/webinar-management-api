from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.dependencies import get_current_user, get_db
from app.models.user import User

from app.repositories.enrollment_repository import EnrollmentRepository
from app.repositories.webinar_repository import WebinarRepository

from app.schemas.enrollment_schema import (
    EnrollmentCreate,
    EnrollmentResponse,
)

from app.services.enrollment_service import EnrollmentService

router = APIRouter(
    prefix="/enrollments",
    tags=["Enrollments"],
)


@router.post(
    "",
    response_model=EnrollmentResponse,
    status_code=status.HTTP_201_CREATED,
)
def register_webinar(
    enrollment: EnrollmentCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repository = EnrollmentRepository(db)

    webinar_repository = WebinarRepository(db)

    service = EnrollmentService(
        repository,
        webinar_repository,
    )

    try:
        return service.register(
            current_user,
            enrollment,
        )

    except Exception as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "/me",
    response_model=list[EnrollmentResponse],
)
def my_webinars(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db),
):
    repository = EnrollmentRepository(db)

    webinar_repository = WebinarRepository(db)

    service = EnrollmentService(
        repository,
        webinar_repository,
    )

    return service.get_my_webinars(
        current_user,
    )
