from Entities.Course import Course
from Entities.User import User
from Entities.Course import print_all_courses_teaching
from ctrl_view_sections_teaching import ctrl_View_Sections_Teaching

import json
from typing import List


class ctrl_Faculty_View_Course_Information:

    def view_information(user: User, courses: List[Course]):
        print_all_courses_teaching(user, courses)
        print("Enter the number of the course you would like to view information for")
        selection = int(input("Enter a selection: "))
        course = courses[selection - 1]
        print(course.description)


if __name__ == '__main__':
    pass

