from classes.Course import Course
from classes.Course import print_all_courses

import json
from typing import List


class View_Courses:
    def view(courses: List[Course]):
    	print_all_courses(courses)


if __name__ == '__main__':
    pass
    # courses: Course = View_Courses.get_courses()
    # View_Courses.print_courses(courses)
