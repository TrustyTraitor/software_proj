from Entities.Course import Course, section_search
from Entities.User import User
from Errors.Errors import Errors

from typing import List

class ctrl_Admin_Remove_Student:
    
	def __query_runner(courses: List[Course], user: User, query: str):
		"""
			Returns different values based on the Errors enum
		"""
		cour, sect = section_search(courses, query)
		print(f'{cour} {sect}')

		if sect == Errors.FAILED_TO_LOCATE:
			return Errors.FAILED_TO_LOCATE
		else:
			if sect.remove_student(user) == Errors.SUCCESS:
				# user.remove_section(cour,sect)
				return Errors.SUCCESS
			else:
				return Errors.FAIL
			
	def remove_student(admin:User, courses: List[Course], users: List[User]):
			student_id = -1
			found_user = -1
			while found_user == -1:
				
				for u in users:
					if u.u_type == "student":
						u.print()

				student_id = str(input("Enter the ID of the Student: "))
				for u in users:
					if u.id == student_id:
						found_user = u
				if found_user == -1:
					print("Error: Student not found, try again")
			
			res = Errors.FAIL
			while (res != Errors.SUCCESS):
				if res == Errors.FAILED_TO_LOCATE:
					print("Failed to locate Section")

				query = input("Enter the section name (ex. CSC-1710-01): ")
				res = ctrl_Admin_Remove_Student.__query_runner(courses, found_user, query)
			
			print("\n\nSuccessfully removed from section!")
