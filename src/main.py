# Type imports (and some specific functions)
from Entities.Course import Course, load_courses
from Entities.User import User, load_users

# Boundary and Control Classes
from ctrl_login import ctrl_Login
from ctrl_logout import ctrl_Logout
from ctrl_edit_personal_information import ctrl_Edit_Personal_Information
from ctrl_view_students import ctrl_Admin_View_Students
from ctrl_view_courses import ctrl_View_Courses
from ctrl_register_class import ctrl_Student_Register_Class

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
        print("5. Logout")
        print("6. Edit Personal Information")
        selection = int(input("Enter a selection: "))
        if selection == 1:
            ctrl_View_Courses.view_courses(courses)
        elif selection == 2:
            ctrl_Student_Register_Class.register_class(courses,current_user)
        elif selection == 3:
            current_user.print_sections()
        elif selection == 4:
            ctrl_Admin_View_Students.view_students(users)
        elif selection == 5:
            ctrl_Logout.Logout(current_user)
            break
        elif selection == 6:
            ctrl_Edit_Personal_Information.pickEdit(current_user)
        selection = 0


if __name__ == '__main__':
    main()
