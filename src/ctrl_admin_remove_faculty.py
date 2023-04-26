from typing import List
from Entities.Course import Course, Section, section_search
from Entities.User import User
from Errors.Errors import Errors
from ctrl_view_courses import ctrl_View_Courses

class ctrl_Admin_Remove_Faculty:
	def __query_runner(courses: List[Course], query: str):
		"""
			Returns different values based on the Errors enum
		"""
		_, sect = section_search(courses, query)

		if sect == Errors.FAILED_TO_LOCATE:
			return Errors.FAILED_TO_LOCATE
		else:
			sect.remove_faculty()
			return Errors.SUCCESS

	def remove_faculty(courses: List[Course], users: List[User]) -> None:
		
		res = Errors.FAIL
		while (res != Errors.SUCCESS):
			if res == Errors.FAILED_TO_LOCATE:
				print("Failed to locate Section")

			ctrl_View_Courses.view_courses(courses)
			query = input("Enter the section name (ex. CSC-1710-01): ")
			res = ctrl_Admin_Remove_Faculty.__query_runner(courses, query)
		
		print("\n\nSuccessfully removed from class!")
			
		

		
