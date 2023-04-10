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
from ctrl_view_sections_teaching import ctrl_View_Sections_Teaching
from ctrl_admin_assign_faculty import ctrl_Admin_Assign_Faculty
from ctrl_faculty_view_course_information import ctrl_Faculty_View_Course_Information

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
    courses[0].sections[0].assign_faculty(current_user)
    selection = 0
    while True:
        if current_user.u_type == 'admin':
            print("\n\n\n")
            print("1. View All Courses")
            print("2. View All Students")
            print("3. Logout")
            print("4. Edit Personal Information")
            selection = int(input("Enter a selection: "))
            if selection == 1:
                ctrl_View_Courses.view_courses(courses)
            elif selection == 2:
                ctrl_Admin_View_Students.view_students(users)
            elif selection == 3:
                ctrl_Logout.Logout(current_user)
                break
            elif selection == 4:
                ctrl_Edit_Personal_Information.pickEdit(current_user)
            selection = 0
            
        elif current_user.u_type == 'student':
            print("\n\n\n")
            print("1. View All Courses")
            print("2. Register for course")
            print("3. View Registered Classes")
            print("4. Logout")
            print("5. Edit Personal Information")
            selection = int(input("Enter a selection: "))
            if selection == 1:
                ctrl_View_Courses.view_courses(courses)
            elif selection == 2:
                ctrl_Student_Register_Class.register_class(courses,current_user)
            elif selection == 3:
                current_user.print_sections()
            elif selection == 4:
                ctrl_Logout.Logout(current_user)
                break
            elif selection == 5:
                ctrl_Edit_Personal_Information.pickEdit(current_user)
            selection = 0

        elif current_user.u_type == 'faculty':
            print("\n\n\n")
            print("1. View All Courses")
            print("2. View All Students")
            print("3. Logout")
            print("4. Edit Personal Information")
            print("5. View Sections Teaching")
            print("6. View Course Information")
            selection = int(input("Enter a selection: "))
            if selection == 1:
                ctrl_View_Courses.view_courses(courses)
            elif selection == 2:
                ctrl_Admin_View_Students.view_students(users)
            elif selection == 3:
                ctrl_Logout.Logout(current_user)
                break
            elif selection == 4:
                ctrl_Edit_Personal_Information.pickEdit(current_user)
            elif selection == 5:
                ctrl_View_Sections_Teaching.view_courses(current_user, courses)
            elif selection == 6:
                ctrl_Faculty_View_Course_Information.view_information(current_user, courses)
            selection = 0


if __name__ == '__main__':
    main()
