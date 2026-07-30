from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user_schema import UserCreate


class UserService:
    def __init__(self, repository: UserRepository):
        self.repository = repository

    def get_all_users(self) -> list[User]:
        return self.repository.get_all()

    def create_user(self, user: UserCreate) -> User:
        user.password = hash_password(user.password)

        return self.repository.create(user)
