from pydantic import BaseModel


class AdminDashboardResponse(BaseModel):
    total_users: int
    total_webinars: int
    total_enrollments: int
    total_attendances: int
