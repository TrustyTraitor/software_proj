from classes.User import User

from typing import List


class StudentList:
    def list_students(users: List[User]):
        for user in users:
            if user.u_type == 'student':
                user.print()
