from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.core.jwt import create_access_token
from app.database.session import get_db
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import LoginRequest, Token
from app.services.user_service import UserService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.post(
    "/login",
    response_model=Token,
)
def login(
    request: LoginRequest,
    db: Session = Depends(get_db),
):
    repository = UserRepository(db)
    service = UserService(repository)

    user = service.authenticate_user(
        request.email,
        request.password,
    )

    if user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid email or password",
        )

    access_token = create_access_token(
        {
            "sub": str(user.email),
        }
    )

    return {
        "access_token": access_token,
        "token_type": "bearer",
    }
