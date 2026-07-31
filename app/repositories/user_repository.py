from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        statement = select(User)

        return list(self.db.scalars(statement).all())

    def get_by_email(self, email: str) -> User | None:
        statement = select(User).where(User.email == email)

        return self.db.scalar(statement)

    def create(self, user: UserCreate) -> User:
        db_user = User(
            name=user.name,
            email=user.email,
            password=user.password,
        )

        self.db.add(db_user)
        self.db.commit()
        self.db.refresh(db_user)

        return db_user
