from classes.Course import Course, get_courses, print_all_courses
from student_list import StudentList
from classes.User import User, load_users
from LogIn import login
from register_classes import Register
from view_courses import View_Courses

from typing import List

def main():
    # init lists that will be passed to functions later
    users: List[User] = []  # This is the list of all users
    courses: List[Course] = []  # this is the list of all courses

    users = load_users()
    courses = get_courses()

    current_user = 0
    while not current_user:
        id, password = input("Enter ID and Password: ").split(' ')
        current_user = login(users, id, password)

    print(f'Welcome {current_user.first_name.capitalize()}!')

    # print("Current Logged in user Info: ")
    # current_user.print()

    # print_all_courses(courses)
    # StudentList.list_students(users)

    # main program loop is here (so like 99% of the code)
    selection = 0
    while True:
        print("\n\n\n")
        print("1. View Courses")
        print("2. Register for course")
        print("3. View Registered Classes")
        selection = int(input("Enter a selection: "))
        if selection == 1:
            View_Courses.view(courses)
        elif selection == 2:
            Register.register(courses,current_user)
        elif selection == 3:
            current_user.print_sections()

        selection = 0


if __name__ == '__main__':
    main()
