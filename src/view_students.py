from classes.User import User

from typing import List


class ctrl_Admin_View_Students:
    def view(users: List[User]):
        for user in users:
            if user.u_type == 'student':
                user.print()
