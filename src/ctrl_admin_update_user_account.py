from Entities.User import User
from Errors.Errors import Errors
from ctrl_edit_personal_information import ctrl_Edit_Personal_Information

class ctrl_Edit_User_Account:
    def pickUserToEdit(userlist: list[User]):
        print("Enter the ID of the user you would like to edit")
        user_id = int(input("Enter a selection: "))
        if user_id < 0 or user_id >= len(userlist):
            return Errors.FAILED_TO_LOCATE
        user = userlist[user_id]
        ctrl_Edit_Personal_Information.pickEdit(user)
        return Errors.SUCCESS