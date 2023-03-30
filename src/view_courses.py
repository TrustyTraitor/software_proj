import json

from classes.Course import Course
from classes.Course import Section

from typing import List

class View_Courses:

    def print_courses(courses: List[Course]):
        for c in courses:
            for s in c.sections:
                c.print()
                s.print()


if __name__ == '__main__':
    pass
    # courses: Course = View_Courses.get_courses()
    # View_Courses.print_courses(courses)
