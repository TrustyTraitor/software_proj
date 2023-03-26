import json

from classes.Course import Course
from classes.Course import Section
from classes.User import User

from view_courses import View_Courses


class Register:
	def register(courses: Course, user:User):
		while True:
			View_Courses.print_courses(courses)

			dept, code, sect = input("Please enter the section name to add to registry\n(for example CSC-1720-01) -> ").upper().split('-')
			
			section_found = False
			for c in courses:
				if c.subject_code != dept:
					continue

				if c.course_number != code:
					continue

				for s in c.sections:
					if s.section != sect:
						continue

					section_found = True
					if s.available_seats > 0:
						user.add_section(c,s)
						s.available_seats -= 1
					else:
						print("Section Full! Cannot register")
				
			if not section_found:
				print("Failed to locate specified class, please try again")
			else:
				print("Successfully registered for class!")
				break



if __name__ == '__main__':
	courses = View_Courses.get_courses()
	user = User(101,'michael','gain',123456789,'best_password','student')

	Register.register(courses,user)
	Register.register(courses,user)
	Register.register(courses,user)
	user.print_registered_sections()