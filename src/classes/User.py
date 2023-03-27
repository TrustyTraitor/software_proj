from classes.Course import Section
from classes.Course import Course


class User:
	def __init__(self, 
	      id, f_name, l_name, 
			ssn, password, u_type):
		self.id = id
		self.first_name = f_name
		self.last_name = l_name
		self.ssn = ssn
		self.password = password
		self.u_type = u_type

		self.__sections = [] # __ means this variable is private
	
	def add_section(self, course:Course, section:Section):
		"""
			Requires a Course object and Section object
			Appends to the __sections member a dictionary in the form of\n
			{
				'Course': course_obj,
				'Section': section_obj
			}
		"""
		self.__sections.append(
			{
				"Course": course, 
    			"Section":section
			}
		)
	
	def get_sections(self):
		"""
			Returns a dictionary in the form of\n
			{
				'Course': course_obj,
				'Section': section_obj
			}
		"""
		return self.__sections
	
	def print_registered_sections(self):
		for c in self.__sections:
			print(f'{c["Course"].subject_code}-{c["Course"].course_number}-{c["Section"].section}')
