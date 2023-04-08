from typing import List
from Entities.Course import Course, Section, section_search
from Entities.Errors import Errors

class ctrl_Admin_Remove_Faculty:
    def remove_faculty(courses: List[Course], section_name: str) -> None:
        _, section = section_search(courses, section_name)

        if section == Errors.FAILED_TO_LOCATE:
            return Errors.FAILED_TO_LOCATE
        
        section.remove_faculty(section)
