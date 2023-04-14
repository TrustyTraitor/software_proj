from Entities.Course import Course, Section, section_search
from Entities.User import User
from Errors.Errors import Errors

from ctrl_login import ctrl_Login
from ctrl_view_courses import ctrl_View_Courses

from typing import List


class ctrl_Student_Register_Class:	
	def __query_runner(courses: List[Course], user: User, query: str):
		"""
			Returns different values based on the Errors enum
		"""
		cour, sect = section_search(courses, query)

		if sect == Errors.FAILED_TO_LOCATE:
			return Errors.FAILED_TO_LOCATE
		else:
			if sect.add_student(user) == Errors.SUCCESS:
				user.add_section(cour, sect)
				return Errors.SUCCESS
			else:
				return Errors.SECTION_FULL

	def register_class(courses: List[Course], user: User):
		res = Errors.FAIL
		while (res != Errors.SUCCESS):
			if res == Errors.SECTION_FULL:
				print("Section full!")
			elif res == Errors.FAILED_TO_LOCATE:
				print("Failed to locate Section")

			ctrl_View_Courses.view_courses(courses)
			query = input("Enter the section name (ex. CSC-1710-01): ")
			res = ctrl_Student_Register_Class.__query_runner(courses, user, query)
		
		print("\n\nSuccessfully Registered for class!")


if __name__ == '__main__':
    pass
