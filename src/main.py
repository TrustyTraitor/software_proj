# Type imports (and some specific functions)
from Entities.Course import Course, load_courses
from Entities.User import User, load_users

# Boundary and Control Classes
from ctrl_login import ctrl_Login
from ctrl_logout import ctrl_Logout
from ctrl_edit_personal_information import ctrl_Edit_Personal_Information
from ctrl_student_view_schedule import ctrl_student_view_schedule
from ctrl_view_students import ctrl_Admin_View_Students
from ctrl_view_courses import ctrl_View_Courses
from ctrl_register_class import ctrl_Student_Register_Class
from ctrl_view_sections_teaching import ctrl_View_Sections_Teaching
from ctrl_admin_assign_faculty import ctrl_Admin_Assign_Faculty
from ctrl_faculty_view_course_information import ctrl_Faculty_View_Course_Information
from ctrl_faculty_request_drop_student import ctrl_Faculty_Request_Drop_Student
from ctrl_admin_update_user_account import ctrl_Edit_User_Account
from ctrl_admin_create_user import ctrl_Create_User_Account
from ctrl_admin_update_system_settings import ctrl_Update_System_Settings
from ctrl_student_drop_course import ctrl_student_drop_course
from ctrl_admin_remove_course import ctrl_Admin_Remove_Course
from ctrl_admin_remove_student import ctrl_Admin_Remove_Student
from ctrl_admin_remove_faculty import ctrl_Admin_Remove_Faculty
from ctrl_admin_delete_user import ctrl_Admin_Delete_User
from ctrl_admin_assign_student import ctrl_Admin_Assign_Student
from ctrl_admin_generate_regestration_report import ctrl_Admin_Generate_Registration_Report
from ctrl_admin_add_course import ctrl_Admin_Add_Course
from ctrl_admin_view_accounts import ctrl_Admin_View_Accounts




# stdlib imports
from typing import List

def main():
    # init lists that will be passed to functions later
    users: List[User] = []  # This is the list of all users
    courses: List[Course] = []  # this is the list of all courses
    enrollmentAvailable = True

    users = load_users()
    courses = load_courses(users)

    current_user = 0
    while not current_user:
        id, password = input("Enter ID and Password: ").split(' ')
        current_user = ctrl_Login.Login(users, id, password)

    print(f'Welcome {current_user.first_name.capitalize()}!')

    #for testing 
    # courses[0].sections[0].assign_faculty(current_user)
    # courses[0].sections[0].add_student(users[1])

    selection = 0
    while True:
        if current_user.u_type == 'admin':
            print("\n\n\n")
            print("1. View All Courses")
            print("2. View All Students")
            print("3. View All Accounts")
            print("4. Add Course")
            print("5. Assign Student to Course")
            print("6. Assign Faculty to Course")
            print("7. Remove Course")
            print("8. Remove Student from Course")
            print("9. Remove Faculty from Course")
            print("10. Generate Registration Report")
            print("11. Create User Account")
            print("12. Update User Account")
            print("13. Delete User Account")
            print("14. Update System Settings")
            print("15. Edit Personal Information")
            print("16. Logout")
            
            selection = int(input("Enter a selection: "))
            if selection == 1:
                ctrl_View_Courses.view_courses(courses)
            elif selection == 2:
                ctrl_Admin_View_Students.view_students(users)
            elif selection == 3:
                ctrl_Admin_View_Accounts.view_user(users)
            elif selection == 4:
                ctrl_Admin_Add_Course.add_course(courses)
            elif selection == 5:
                ctrl_Admin_Assign_Student.assign_student(courses,users)
            elif selection == 6:
                ctrl_Admin_Assign_Faculty.assign_faculty(courses,users)
            elif selection == 7:
                ctrl_Admin_Remove_Course.remove_course(courses)
            elif selection == 8:
                ctrl_Admin_Remove_Student.remove_student(users)
            elif selection == 9:
                ctrl_Admin_Remove_Faculty.remove_faculty(users)
            elif selection == 10:
                ctrl_Admin_Generate_Registration_Report.generate_registration_report(courses)
            elif selection == 11:
                ctrl_Create_User_Account.createUserAccount(users)
            elif selection == 12:
                ctrl_Edit_User_Account.pickUserToEdit(users)
            elif selection == 13:
                ctrl_Admin_Delete_User.delete_user(users)
            elif selection == 14:
                ctrl_Update_System_Settings.updateSystemSettings(enrollmentAvailable)
            elif selection == 15:
                ctrl_Edit_Personal_Information.pickEdit(current_user)
            elif selection == 16:
                ctrl_Logout.Logout(current_user)
                break
            selection = 0
            
        elif current_user.u_type == 'student':
            print("\n\n\n")
            print("1. View All Courses")
            print("2. View Schedule")
            print("3. View Registered Classes")
            print("4. Register for course")
            print("5. Drop Course")
            print("6. Edit Personal Information")
            print("7. Logout")
            
            selection = int(input("Enter a selection: "))
            if selection == 1:
                ctrl_View_Courses.view_courses(courses)
            elif selection == 2:
                ctrl_student_view_schedule.view_schedule(current_user)
            elif selection == 3:
                current_user.print_sections()
            elif selection == 4:
                ctrl_Student_Register_Class.register_class(courses,current_user)
            elif selection == 5:
                ctrl_student_drop_course.drop_course(courses,current_user)
            elif selection == 6:
                ctrl_Edit_Personal_Information.pickEdit(current_user)
            elif selection == 7:
                ctrl_Logout.Logout(current_user)
                break
            
            selection = 0

        elif current_user.u_type == 'faculty':
            print("\n\n\n")
            print("1. View All Courses")
            print("2. View Sections Teaching")
            print("3. View Course Information")
            print("4. View All Students")
            print("5. Request to drop a student")
            print("6. Edit Personal Information")
            print("7. Logout")
            
            selection = int(input("Enter a selection: "))
            if selection == 1:
                ctrl_View_Courses.view_courses(courses)          
            elif selection == 2:
                ctrl_View_Sections_Teaching.view_courses(current_user, courses)
            elif selection == 3:
                ctrl_Faculty_View_Course_Information.view_information(current_user, courses)            
            elif selection == 4:
                ctrl_Admin_View_Students.view_students(users)
            elif selection == 5:
                ctrl_Faculty_Request_Drop_Student.view_students(current_user, courses)
            elif selection == 6:
                ctrl_Edit_Personal_Information.pickEdit(current_user)
            elif selection == 7:
                ctrl_Logout.Logout(current_user)
                break

            selection = 0

if __name__ == '__main__':
    main()
