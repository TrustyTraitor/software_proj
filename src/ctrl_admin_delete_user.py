from typing import List
from Entities.User import User

class ctrl_Admin_Delete_User:
    def delete_user(users: List[User]):
        for u in users:
            u.print()
            
        user_id = input("Enter the user id: ")
        User.admin_delete_user(users, user_id)
