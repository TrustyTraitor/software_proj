from classes.Course import Course, Section, course_search, get_courses
from classes.User import User
from view_courses import View_Courses

from typing import List


class Register:
    def register(courses: List[Course], user: User, query: str):
        """
            Returns False if failed to register for class
        """
        cour, sect = course_search(courses, query)

        if sect == -1:
            print("Failed to locate specified class, please try again")
        else:
            if sect.available_seats > 0:
                user.add_section(cour, sect)
                sect.available_seats -= 1
                print("Successfully registered for class!")
                return True
            else:
                print("Section Full! Cannot register")
                
        return False


if __name__ == '__main__':
    courses = get_courses()
    user = User(101, 'michael', 'gain', 123456789, 'best_password', 'student')

    valid = False
    while not valid:
        View_Courses.print_courses(courses)
        query = input("\n\nPlease input the section string (example CSC-1720-01): ")
        valid = Register.register(courses, user, query)
    
	# Register.register(courses, user)
    # Register.register(courses, user)
    user.print_registered_sections()
