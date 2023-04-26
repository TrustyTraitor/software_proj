from typing import List
from Entities.User import User

class ctrl_Admin_View_Accounts:
    def view_user(users: List[User]):
        for user in users:
            user.print()