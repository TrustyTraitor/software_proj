import json

from classes.Course import Course
from classes.Course import Section
from classes.Course import search
from classes.User import User

from view_courses import View_Courses


class Register:
    def register(courses: Course, user: User):
        section_located = False
        while not section_located:
            View_Courses.print_courses(courses)

            section_str = input(
                "Please enter the section name to add to registry\n(for example CSC-1720-01) -> ")
            cour, sect = search(courses, section_str)

            if sect == -1:
                print("Failed to locate specified class, please try again")
            else:
                if sect.available_seats > 0:
                    user.add_section(cour, sect)
                    sect.available_seats -= 1
                    print("Successfully registered for class!")
                    section_located = True
                else:
                    print("Section Full! Cannot register")


if __name__ == '__main__':
    courses = View_Courses.get_courses()
    user = User(101, 'michael', 'gain', 123456789, 'best_password', 'student')

    Register.register(courses, user)
    # Register.register(courses, user)
    # Register.register(courses, user)
    user.print_registered_sections()
