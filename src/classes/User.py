from classes.Course import Section
from classes.Course import Course

from typing import List, Tuple

import json

class User:
    def __init__(self,
                 id, f_name, l_name,
                 ssn, password, u_type):
        self.id = id
        self.first_name = f_name
        self.last_name = l_name
        self.ssn = ssn
        self.password = password
        self.u_type = u_type

        # __ means this variable is private
        self.__sections: List[Tuple[Course, Section]] = []

    def add_section(self, course: Course, section: Section) -> None:
        """
			Requires a Course object and Section object
			Appends to the __sections member a tuple in the form of\n
			(Course,Section)
        """
        self.__sections.append(
            (course, section)
        )

    def get_sections(self) -> Tuple[Course, Section]:
        """
			Returns a tuple in the form of\n
			(course,section)
        """
        return self.__sections

    def print(self) -> None:
        """
        
        """
        print(
            f'Id: {self.id}\nName: {self.first_name} {self.last_name}\nPermission Level: {self.u_type}'
            )

    def print_registered_sections(self) -> None:
        for c in self.__sections:
            print(
                f'{c[0].subject_code}-{c[0].course_number}-{c[1].section}')


def get_users() -> List[User]:
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
        
        users.append(User(id, f_name, l_name, ssn, password,u_type))

    return users
