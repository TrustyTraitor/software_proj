from Entities.Course import Course
from Entities.User import User
from Entities.Course import print_all_courses_teaching

import json
from typing import List


class ctrl_View_Sections_Teaching:

    def view_courses(user: User, courses: List[Course]):
        print_all_courses_teaching(user, courses)


if __name__ == '__main__':
    pass

