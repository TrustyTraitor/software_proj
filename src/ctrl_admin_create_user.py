from Entities.User import User
from Errors.Errors import Errors


class ctrl_Create_User_Account:
    def createUserAccount(userlist: list[User]):
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        #promp for user type. 1 for student, 2 for faculty, 3 for admin
        u_type = ""  # initialize u_type as an empty string
        while u_type != "1" and u_type != "2" and u_type != "3":
            print("Enter user type: \n1. Student\n2. Faculty\n3. Admin")
            u_type = input("Enter selection: ")
        if u_type == "1":
            u_type = "student"
        elif u_type == "2":
            u_type = "faculty"
        elif u_type == "3":
            u_type = "admin"
        else:
            print(u_type)

        #prompt for ssn
        while len(ssn) != 11:
            ssn = input("Enter SSN in the format xxx-xx-xxxx: ")
        password = input("Enter password: ")
        password_confirm = input("Confirm password: ")
        if password != password_confirm:
            return Errors.MISMATCHED_PASSWORDS
        id = len(userlist)
        user = User(id, first_name, last_name, ssn, password, u_type)


        #add user to userlist, simulates adding to database
        userlist.append(user)
        return Errors.SUCCESS
    

