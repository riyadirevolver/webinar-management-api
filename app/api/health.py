from fastapi import APIRouter, Depends
from sqlalchemy import text
from sqlalchemy.orm import Session

from app.database.session import get_db

router = APIRouter(
    prefix="/health",
    tags=["Health"],
)


@router.get("/database")
def database_health(
    db: Session = Depends(get_db),
):
    """
    Database Health Check
    """

    try:

        db.execute(text("SELECT 1"))

        return {
            "status": "healthy",
            "database": "connected",
        }

    except Exception as e:

        return {
            "status": "unhealthy",
            "database": "disconnected",
            "error": str(e),
        }
