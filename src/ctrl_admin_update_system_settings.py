from Errors.Errors import Errors

class ctrl_Update_System_Settings:
    def updateSystemSettings(enrollmentAvailable: bool):
        if enrollmentAvailable:
            print("Enrollment is currently available")
            input("Would you like to disable enrollment? (y/n): ")
            if input == "y":
                enrollmentAvailable = False
                return Errors.SUCCESS
            elif input == "n":
                return Errors.SUCCESS
            else:
                return Errors.FAIL
        else:
            print("Enrollment is currently unavailable")
            input("Would you like to enable enrollment? (y/n): ")
            if input == "y":
                enrollmentAvailable = True
                return Errors.SUCCESS
            elif input == "n":
                return Errors.SUCCESS
            else:
                return Errors.FAIL