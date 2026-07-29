from sqlalchemy import create_engine

from app.core.config import settings


DATABASE_URL = (
    f"mysql+pymysql://"
    f"{settings.db_user}:"
    f"{settings.db_password}@"
    f"{settings.db_host}:"
    f"{settings.db_port}/"
    f"{settings.db_name}"
)

engine = create_engine(
    DATABASE_URL,
    echo=settings.debug,
    pool_pre_ping=True,
)
