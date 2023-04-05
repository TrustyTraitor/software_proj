# Type imports (and some specific functions)
from Entities.Course import Course, load_courses
from Entities.User import User, load_users

# Boundary and Control Classes
from ctrl_login import ctrl_Login
from ctrl_view_students import ctrl_Admin_View_Students
from ctrl_view_courses import ctrl_View_Courses
from ctrl_register_classes import ctrl_Student_Register

# stdlib imports
from typing import List

def main():
    # init lists that will be passed to functions later
    users: List[User] = []  # This is the list of all users
    courses: List[Course] = []  # this is the list of all courses

    users = load_users()
    courses = load_courses()

    current_user = 0
    while not current_user:
        id, password = input("Enter ID and Password: ").split(' ')
        current_user = ctrl_Login.Login(users, id, password)

    print(f'Welcome {current_user.first_name.capitalize()}!')

    selection = 0
    while True:
        print("\n\n\n")
        print("1. View Courses")
        print("2. Register for course")
        print("3. View Registered Classes")
        print("4. View Students")
        selection = int(input("Enter a selection: "))
        if selection == 1:
            ctrl_View_Courses.view(courses)
        elif selection == 2:
            ctrl_Student_Register(courses,current_user)
        elif selection == 3:
            current_user.print_sections()
        elif selection == 4:
            ctrl_Admin_View_Students.view(users)

        selection = 0


if __name__ == '__main__':
    main()
