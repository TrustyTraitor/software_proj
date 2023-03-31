from classes.Course import Course, get_courses, print_all_courses
from student_list import StudentList
from classes.User import User, get_users
from LogIn import login

from typing import List


def main():
    # init lists that will be passed to functions later
    users: List[User] = []  # This is the list of all users
    courses: List[Course] = []  # this is the list of all courses

    users = get_users()
    courses = get_courses()

    current_user = 0
    while not current_user:
        id, password = input("Enter ID and Password: ").split(' ')
        current_user = login(users, id, password)

    print("Current Logged in user Info: ")
    current_user.print()

    print_all_courses(courses)
    StudentList.list_students(users)

    # main program loop is here (so like 99% of the code)
    selection = 0
    while True:
        pass


if __name__ == '__main__':
    main()
