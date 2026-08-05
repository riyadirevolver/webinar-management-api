from sqlalchemy.orm import Session

from app.models.user import User
from app.models.webinar import Webinar
from app.models.enrollment import Enrollment
from app.models.attendance import Attendance


class DashboardRepository:

    def __init__(self, db: Session):
        self.db = db

    def total_users(self):
        return self.db.query(User).count()

    def total_webinars(self):
        return self.db.query(Webinar).count()

    def total_enrollments(self):
        return self.db.query(Enrollment).count()

    def total_attendances(self):
        return self.db.query(Attendance).count()
