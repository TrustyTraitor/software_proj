from Errors.Errors import Errors
from Entities.Course import Course, section_search
from Entities.User import User

from typing import List

class ctrl_student_drop_course:
	def __query_runner(courses: List[Course], user: User, query: str):
		"""
			Returns different values based on the Errors enum
		"""
		cour, sect = section_search(courses, query)

		if sect == Errors.FAILED_TO_LOCATE:
			return Errors.FAILED_TO_LOCATE
		else:
			if sect.remove_student(user) == Errors.SUCCESS:
				user.remove_section(cour,sect)
				return Errors.SUCCESS
			else:
				return Errors.FAIL
			
	def drop_course(courses: List[Course], user: User):
			res = Errors.FAIL
			while (res != Errors.SUCCESS):
				if res == Errors.FAIL:
					print("Unknown Failure!")
				elif res == Errors.FAILED_TO_LOCATE:
					print("Failed to locate Section")

				user.print_sections()
				query = input("Enter the section name (ex. CSC-1710-01): ")
				res = ctrl_student_drop_course.__query_runner(courses, user, query)
			
			print("\n\nSuccessfully dropped section!")