# ctrl_Faculty_Add_Materials.py

from typing import List
from Entities.Course import Course, faculty_add_materials
from Entities.User import User
from Errors.Errors import Errors

class ctrl_Faculty_Add_Materials:
    def add_materials(faculty: User, courses: List[Course], course_code: str, section_number: str, new_material: str) -> Errors:
        return faculty_add_materials(faculty, courses, course_code, section_number, new_material)
