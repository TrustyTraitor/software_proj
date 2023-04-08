from typing import List
from Entities.Course import Course, Section

class ctrl_Admin_Assign_Faculty:
    def assign_faculty(course: Course, section: str, faculty: str) -> None:
        course.assign_faculty(section, faculty)
