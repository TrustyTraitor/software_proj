from typing import List
from Entities.Course import Course
from Entities.Course import Section

class ctrl_Admin_Remove_Faculty:
    def remove_faculty(section: Section) -> None:
        section.remove_faculty(section)
