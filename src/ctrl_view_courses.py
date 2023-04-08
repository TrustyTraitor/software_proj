from Entities.Course import Course
from Entities.Course import print_all_courses

import json
from typing import List


class ctrl_View_Courses:
    def view_courses(courses: List[Course]):
    	print_all_courses(courses)


if __name__ == '__main__':
    pass
    # courses: Course = View_Courses.get_courses()
    # View_Courses.print_courses(courses)
