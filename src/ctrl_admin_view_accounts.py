from typing import List
from Entities.User import User

class ctrl_admin_view_accounts:
    def view_user(cls, users: List[User], user_id: int):
        """
        Prints out a specific user's id, name, SSN, and permission level
        """
        for user in users:
            if user.id == user_id:
                user.admin_view_accounts(users, user_id)
                return

        print("User not found.")