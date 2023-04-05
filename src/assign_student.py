from classes.Course import Section
from classes.User import User

class ctrl_Admin_Assign_Student:
	def assign_student(section: Section, user: User):
		section.add_student(user)
