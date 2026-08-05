from fastapi import APIRouter, Depends, status

from app.core.dependencies import (
    get_current_user,
    get_webinar_service,
)
from app.core.permissions import require_role
from app.models.user import User
from app.schemas.webinar_schema import (
    WebinarCreate,
    WebinarResponse,
)
from app.services.webinar_service import WebinarService

router = APIRouter(
    prefix="/webinars",
    tags=["Webinars"],
)


@router.get(
    "",
    response_model=list[WebinarResponse],
)
def get_webinars(
    current_user: User = Depends(get_current_user),
    service: WebinarService = Depends(get_webinar_service),
):
    return service.get_all_webinars()


@router.post(
    "",
    response_model=WebinarResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_webinar(
    webinar: WebinarCreate,
    current_user: User = Depends(require_role("admin")),
    service: WebinarService = Depends(get_webinar_service),
):
    return service.create_webinar(webinar)