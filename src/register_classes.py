from classes.Course import Course, Section, course_search
from classes.User import User
from classes.Errors import Errors

from view_courses import View_Courses

from typing import List


class ctrl_Student_Register:	
	def __query_runner(courses: List[Course], user: User, query: str):
		"""
			Returns different values based on the Errors enum
		"""
		cour, sect = course_search(courses, query)

		if sect == -1:
			return Errors.FAILED_TO_LOCATE
		else:
			if sect.add_student(user) == Errors.SUCCESS:
				user.add_section(cour, sect)
				return Errors.SUCCESS
			else:
				return Errors.SECTION_FULL

	def register(courses: List[Course], user: User):
		res = Errors.FAIL
		while (res != Errors.SUCCESS):
			if res == Errors.SECTION_FULL:
				print("Section full!")
			elif res == Errors.FAILED_TO_LOCATE:
				print("Failed to locate Section")

			View_Courses.view(courses)
			query = input("Enter the section name (ex. CSC-1710-01): ")
			res = ctrl_Student_Register.__query_runner(courses, user, query)
		
		print("\n\nSuccessfully Registered for class!")


if __name__ == '__main__':
    pass
