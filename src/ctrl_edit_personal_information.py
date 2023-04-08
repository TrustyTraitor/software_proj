from Entities.User import User
from Entities.Errors import Errors


class ctrl_Edit_Personal_Information:
    def pickEdit(u: User):
        selection = 0
        print("1. Edit First Name")
        print("2. Edit Last Name")
        print("3. Edit Password")
        print("4. Return to Main Menu")

        selection = int(input("Enter a selection: "))
        if selection == 1:
            ctrl_Edit_Personal_Information.EditFirstName(u)
        elif selection == 2:
            ctrl_Edit_Personal_Information.EditLastName(u)
        elif selection == 3:
            if (ctrl_Edit_Personal_Information.EditPassword(u) == Errors.WRONG_PASSWORD or ctrl_Edit_Personal_Information.EditPassword(u) == Errors.MISMATCHED_PASSWORDS):
                ctrl_Edit_Personal_Information.pickEdit(u)
        elif selection == 4:
            return Errors.SUCCESS

    def EditLastName(u: User):
        u.last_name = input("Enter new last name: ").capitalize()
        return Errors.SUCCESS

    def EditFirstName(u: User):
        u.first_name = (input("Enter new first name: ").capitalize())
        return Errors.SUCCESS

    def EditPassword(u: User):
        passwordAttempt = input("Enter your current password: ")
        if passwordAttempt == u.password:
            newPasswordFirst = input("Enter new password: ")
            newPasswordSecond = input("Please confirm your new password: ")
            if newPasswordFirst == newPasswordSecond:
                u.password = newPasswordFirst
                return Errors.SUCCESS
            else:
                print("Passwords do not match")
                return Errors.MISMATCHED_PASSWORDS
        else:
            print("Incorrect password")
            return Errors.WRONG_PASSWORD



