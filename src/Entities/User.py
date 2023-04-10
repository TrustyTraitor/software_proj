from typing import List, Tuple

import json


class User:
    def __init__(self,
                 id: int, f_name: str, l_name: str,
                 ssn: str, password: str, u_type: str):
        self.id: int = id
        self.first_name: str = f_name
        self.last_name: str = l_name
        self.ssn: str = ssn
        self.password: str = password
        self.u_type: str = u_type

        # __ means this variable is private
        self.__sections = []

    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_first_name(self, fn):
        self.first_name = fn

    def get_first_name(self):
        return self.first_name

    def set_last_name(self, ln):
        self.last_name = ln

    def get_last_name(self):
        return self.last_name

    def set_ssn(self, ssn):
        self.ssn = ssn

    def get_ssn(self):
        return self.ssn

    def set_password(self, pw):
        self.password = pw

    def get_password(self):
        return self.password

    def set_utype(self, ut):
        self.u_type = ut

    def get_utype(self):
        return self.u_type

    def add_section(self, course, section) -> None:
        """
                Requires a Course object and Section object
                Appends to the __sections member a tuple in the form of\n
                (Course,Section)
        """
        self.__sections.append(
            (course, section)
        )

    def get_sections(self):
        """
                Returns a tuple in the form of\n
                (course,section)
        """
        return self.__sections

    def print_sections(self):
        abc = self.get_sections()
        for a in abc:
            c, s = a
            c.print()
            s.print()

    def print(self) -> None:
        """
        Prints out a user's id, name, and permission level
        """
        print(
            f'Id: {self.id}\nName: {self.first_name} {self.last_name}\nPermission Level: {self.u_type}'
        )

    def admin_delete_user(users: List['User'], user_id: int) -> bool:
        """
        Removes a user from the system based on their id
        """
        for i, user in enumerate(users):
            if user.id == user_id:
                users.pop(i)
                return True
        return False
"""
Helper functions not part of User class
"""


def load_users() -> List[User]:
    """
        Reads the 'database' to get the list of users
    """
    users: List[User] = []

    with open("./data/users.json", 'r') as file:
        data = json.load(file)

    for u in data:
        id = str(u['id'])
        f_name = u['first_name']
        l_name = u['last_name']
        ssn = u['SSN']
        password = u['password']
        u_type = u['type']

        users.append(User(id, f_name, l_name, ssn, password, u_type))

    return users
