from typing import List
from Entities.Course import Course
from Entities.User import User

class ctrl_Admin_Remove_Course:
	def remove_course(courses: List[Course], users: List[User]):
		found = 0
		while found == 0:
			subj = str(input("Enter the subject code (i.e. CSC): ")).upper()
			number = str(input("Enter the course code (i.e. 1710): "))

			for c in courses:
				if c.subject_code == subj and c.course_number == number:
					for s in c.sections:
						for u in users:
							s.remove_student(u)
						s.remove_faculty()
					found = 1
			
			if found == 0:
				print("Course not found, try again")
		
		print("Course removed!")


