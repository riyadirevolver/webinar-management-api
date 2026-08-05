from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.core.jwt import decode_access_token
from app.database.session import get_db

from app.repositories.user_repository import UserRepository
from app.repositories.webinar_repository import WebinarRepository

from app.services.user_service import UserService
from app.services.webinar_service import WebinarService


oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login",
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
):
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    email = payload.get("sub")

    if email is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
        )

    repository = UserRepository(db)

    user = repository.get_by_email(email)

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="User not found",
        )

    return user


def get_user_service(
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)
    return UserService(repository)


def get_webinar_service(
    db: Session = Depends(get_db),
):
    repository = WebinarRepository(db)
    return WebinarService(repository)