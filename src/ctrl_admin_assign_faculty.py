from typing import List
from Entities.Course import Course, Section

class ctrl_Admin_Assign_Faculty:
    def assign_faculty(section: Section, faculty: str) -> None:
        section.assign_faculty(section, faculty)
