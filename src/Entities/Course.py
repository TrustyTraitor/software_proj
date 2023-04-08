from Entities.Errors import Errors

from typing import List, Tuple
import json


class Course:
    """
    Course contains subject code, course number, title, description and a list of sections
    """

    def __init__(self,
                 subj_code: str, number: str,
                 title: str, desc: str):

        self.subject_code: str = subj_code
        self.course_number: str = number
        self.title: str = title
        self.description: str = desc

        self.sections = []

    def print(self) -> None:
        """
        Prints subject code and course number
        """
        print(f'\n{self.title}')
        print(f'{self.subject_code}-{self.course_number}-', end='')


class Section:
    """
    Section contains the rest of information required for a class
    It also includes a list of students who are enrolled in the course
    """

    def __init__(self,
                 section: str, prof: str, seats: int,
                 building: str, room: str,
                 days: str, start_time: str, end_time: str,
                 books: List[str], materials: List[str]):
        # Section Number
        self.section: str = section

        self.professor: str = prof
        self.available_seats: int = seats

        self.building: str = building
        self.room: str = room
        self.days: str = days
        self.start_time: str = start_time
        self.end_time: str = end_time

        self.books: List[str] = books
        self.materials: List[str] = materials

        self.__students = []

    def add_material(self, material: str) -> None:
        self.materials.append(material)

    def add_book(self, book: str) -> None:
        self.books.append(str)

    def add_student(self, student) -> None:
        if self.available_seats > 0:
            self.__students.append(student)
            self.available_seats -= 1
            return Errors.SUCCESS
        else:
            return Errors.SECTION_FULL

    def print(self) -> None:
        """
        Run Course.print() before running this or output will look goofy
        """
        print(f'{self.section}')
        print(f'\t{self.building}, {self.room}')
        print(f'\t{self.days} {self.start_time} - {self.end_time}')
        print(f'\t{self.professor}')
        print(f'\tBooks:{self.books}')
        print(f'\tMaterials:{self.materials}')


"""
These are all helper functions that are not part of either class
"""

def load_courses() -> List[Course]:
    """
    This will read courses from the data/courses.json\n
    returns a list of courses \n
    See the classes module for info about Course object
    """
    courses: Course = []

    with open("./data/courses.json", 'r') as file:
        data = json.load(file)

    for subj in data.keys():
        for idx, code in enumerate(data[subj].keys()):
            title = data[subj][code]["title"]
            desc = data[subj][code]["description"]

            courses.append(Course(subj, code, title, desc))
            for sect in data[subj][code]["Sections"]:
                section = data[subj][code]["Sections"][sect]

                courses[idx].sections.append(
                    Section(sect, section["Professor"], section["Seats"],
                            section["Building"], section["Room"],
                            section["MeetingDays"], section["StartTime"], section["EndTime"],
                            section["Books"], section["Materials"]
                            )
                )

    return courses


def print_all_courses(courses: List[Course]) -> None:
    """
        Prints all sections and their information
    """
    for c in courses:
        for s in c.sections:
            c.print()
            s.print()


def course_search(courses: List[Course], query: str) -> Tuple[Course, Section]:
    """
        Takes in list of courses and a string describing the course to be located\n
        The query string should be in the form\n
        \tCSC-1710-01\n
        \tDEPT-CODE-SECTION

        returns a tuple of (course,section) if found or (-1,-1) if not found
    """
    while True:

        dept, code, sect = query.upper().split('-')
        section: Section = -1
        course: Course = -1

        for c in courses:
            if c.subject_code != dept:
                continue

            if c.course_number != code:
                continue

            for s in c.sections:
                if s.section != sect:
                    continue

                section = s
                course = c

        return (course, section)