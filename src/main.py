"""
Heres how I imagine we will structure our project:

- Use this main file to call all other use case functions
- The TUI (terminal user interface) code will be mostly in here
- Each use case where applicable should return lists of 
objects to ensure data coherence (see view_courses.py)

"""

"""
	Also check out the classes in the classes folder
    I will be adding utility functions as I run into the need for them 
    and in general the object classes are located there
"""

from classes.Course import Course
from classes.Course import Section
from classes.User import User

from view_courses import View_Courses


def main():
    # init objects that will be passed to functions later
    users: User = []
    courses: Course = []

    courses = View_Courses.get_courses()

	# main program loop is here (so like 99% of the code)
    while True:
        pass


if __name__ == '__main__':
    main()
