from Entities.User import User
from Entities.Course import Course, Section
from Entities.Course import print_students_in_sections_teaching

from typing import List


class ctrl_Faculty_Request_Drop_Student:
    def view_students(user: User, courses: List[Course]):
        print_students_in_sections_teaching(user, courses)
        print("Enter the section number")
        selection = int(input("Enter a selection: "))
        section = courses[selection - 1].sections[0]
        print("Enter the student number")
        selection = int(input("Enter a selection: "))
        selection = selection - 1
        student = Section.get_student(section, selection)
        ctrl_Faculty_Request_Drop_Student.request_drop(student, section)

    def request_drop(user: User, section: Section):
        print(f'Request to drop {user.first_name} from {section.section}')
        #whoever does the admin stuff will need to add a function to the admin class to approve/deny this request


