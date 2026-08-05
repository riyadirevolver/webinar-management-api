from app.repositories.dashboard_repository import DashboardRepository


class DashboardService:

    def __init__(
        self,
        repository: DashboardRepository,
    ):
        self.repository = repository

    def admin_dashboard(self):

        return {
            "total_users": self.repository.total_users(),
            "total_webinars": self.repository.total_webinars(),
            "total_enrollments": self.repository.total_enrollments(),
            "total_attendances": self.repository.total_attendances(),
        }
