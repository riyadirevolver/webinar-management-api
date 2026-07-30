from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user_schema import UserCreate


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self) -> list[User]:
        return self.db.query(User).all()

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
