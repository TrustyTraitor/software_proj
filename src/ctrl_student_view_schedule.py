from Errors.Errors import Errors
from Entities.Course import Course, section_search
from Entities.User import User

from typing import List

class ctrl_student_view_schedule:
    def view_schedule(user: User):
        print("Your schedule: ")
        
        for cour,sect in user.get_sections():
            print(f'{cour.subject_code}-{cour.course_number}-{sect.section}')
            print(f'\t{sect.days}: {sect.start_time}-{sect.end_time}')