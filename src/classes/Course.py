class Course:
	"""
	Course contains subject code, course number, title, description and a list of sections
	"""
	def __init__(self, 
	      subj_code, number, 
			title, desc):

		self.subject_code :str = subj_code
		self.course_number :str = number
		self.title :str = title
		self.description :str = desc

		self.sections :Section = []
	
	def print(self):
		"""
		Prints subject code and course number
		"""
		print(f'\n{self.subject_code}-{self.course_number}-', end='')


class Section:
	"""
	Section contains the rest of information required for a class
	It also includes a list of students who are enrolled in the course
	"""
	def __init__(self, 
	      section, prof, seats,
			building, room,
			days, start_time, end_time):
		# Section Number
		self.section :str = section

		self.professor :str = prof
		self.available_seats :int = seats
		
		self.building :str = building
		self.room :str = room
		self.days :str = days
		self.start_time :str = start_time
		self.end_time :str = end_time

		self.students = []
	
	def print(self):
		"""
		Run Course.print() before running this or output will look goofy
		"""
		print(f'{self.section}')
		print(f'\t{self.building}, {self.room}')
		print(f'\t{self.days} {self.start_time} - {self.end_time}')
		print(f'\t{self.professor}')

