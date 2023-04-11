from Entities.Course import Course, Section, section_search
from Entities.User import User
from Errors.Errors import Errors

from typing import List

class ctrl_Admin_Assign_Student:
	def assign_student(courses: List[Course], section_name: str, user: User):
		_, section = section_search(courses, section_name)

		if section == Errors.FAILED_TO_LOCATE:
			return Errors.FAILED_TO_LOCATE

		section.add_student(user)
