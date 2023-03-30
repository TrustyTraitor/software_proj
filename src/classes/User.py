from classes.Course import Section
from classes.Course import Course

from typing import List,Tuple

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

        self.__sections: List[Tuple[Course,Section]] = []  # __ means this variable is private

    def add_section(self, course: Course, section: Section) -> None:
        """
                Requires a Course object and Section object
                Appends to the __sections member a tuple in the form of\n
                (Course,Section)
        """
        self.__sections.append(
            (course,section)
        )

    def get_sections(self) -> Tuple[Course,Section]:
        """
                Returns a tuple in the form of\n
                (course,section)
        """
        return self.__sections

    def print_registered_sections(self) -> None:
        for c in self.__sections:
            print(
                f'{c[0].subject_code}-{c[0].course_number}-{c[1].section}')


def get_users() -> List[User]:
    pass
