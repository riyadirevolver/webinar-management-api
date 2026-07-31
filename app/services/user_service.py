from app.core.security import hash_password, verify_password
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

    def authenticate_user(
        self,
        email: str,
        password: str,
    ) -> User | None:

        user = self.repository.get_by_email(email)

        if user is None:
            return None

        if not verify_password(
            password,
            user.password,
        ):
            return None

        return user
