from typing import List
from Entities.User import User

class ctrl_Admin_Delete_User:
    def delete_user(users: List[User], user_id: int) -> bool:
        return User.admin_delete_user(users, user_id)
