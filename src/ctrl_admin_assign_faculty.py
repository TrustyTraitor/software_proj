from typing import List
from Entities.Course import Course, Section, section_search
from Entities.User import User
from Errors.Errors import Errors
from ctrl_view_courses import ctrl_View_Courses

class ctrl_Admin_Assign_Faculty:
	def __query_runner(courses: List[Course], user: User, query: str):
		"""
			Returns different values based on the Errors enum
		"""
		_, sect = section_search(courses, query)

		if sect == Errors.FAILED_TO_LOCATE:
			return Errors.FAILED_TO_LOCATE
		else:
			sect.assign_faculty(user)
			return Errors.SUCCESS

	def __find_section(courses: List[Course], user: User):
		res = Errors.FAIL
		while (res != Errors.SUCCESS):
			if res == Errors.FAILED_TO_LOCATE:
				print("Failed to locate Section")

			ctrl_View_Courses.view_courses(courses)
			query = input("Enter the section name (ex. CSC-1710-01): ")
			res = ctrl_Admin_Assign_Faculty.__query_runner(courses, user, query)
		
		print("\n\nSuccessfully assigned to class!")

	def assign_faculty(courses: List[Course], users: List[User]) -> None:
		faculty_id = -1
		found_user = -1
		while found_user == -1:

			for u in users:
				if u.u_type == "faculty":
					u.print()

			faculty_id = str(input("Enter the ID of the Faculty: "))
			for u in users:
				if u.id == faculty_id:
					found_user = u

			if found_user == -1:
				print("Error: Faculty not found, try again")
		
		ctrl_Admin_Assign_Faculty.__find_section(courses, found_user)
			
		

		
