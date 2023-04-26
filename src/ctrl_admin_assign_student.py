from Entities.Course import Course, Section, section_search
from Entities.User import User
from Errors.Errors import Errors

from ctrl_register_class import ctrl_Student_Register_Class

from typing import List

class ctrl_Admin_Assign_Student:
	def assign_student(courses: List[Course], users: List[User]):
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

		ctrl_Student_Register_Class.register_class(courses, found_user)
