from typing import List
from Entities.Course import Course

class ctrl_Admin_Remove_Faculty:
    def remove_faculty(course: Course, section: str) -> None:
        course.admin_remove_faculty(section)
