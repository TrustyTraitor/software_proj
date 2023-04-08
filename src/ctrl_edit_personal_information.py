from Entities.User import User


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
            ctrl_Edit_Personal_Information.EditPassword(u)
        elif selection == 4:
            return 0

    def EditLastName(u: User):
        u.last_name = input("Enter new last name: ").capitalize()

    def EditFirstName(u: User):
        u.first_name = (input("Enter new first name: ").capitalize())

    def EditPassword(u: User):
        passwordAttempt = input("Enter your current password: ")
        if passwordAttempt == u.password:
            newPasswordFirst = input("Enter new password: ")
            newPasswordSecond = input("Please confirm your new password: ")
            if newPasswordFirst == newPasswordSecond:
                u.password = newPasswordFirst
        else:
            print("Incorrect password")
            ctrl_Edit_Personal_Information.pickEdit(u)


        return 0
