from classes.Course import Course, Section, get_courses
from view_courses import View_Courses
from student_list import StudentList
from classes.User import User, get_users
from LogIn import Login

from typing import List


def main():
    # init objects that will be passed to functions later
    users: List[User] = []
    courses: List[Course] = []

    users = get_users()
    courses = get_courses()

    user = 0
    while not user:
        id, password = input("Enter ID and Password: ").split(' ')
        user = Login.login(users, id, password)

    View_Courses.print_courses(courses)
    StudentList.list_students(users)

    # main program loop is here (so like 99% of the code)
    # while True:
    #     pass


if __name__ == '__main__':
    main()
