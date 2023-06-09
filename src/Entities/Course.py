from Errors.Errors import Errors
from Entities.User import User
from typing import List, Tuple, Dict
import json

import Entities.User

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

    def generate_student_registration_report(self) -> List[str]:
        """
        Generates a list of strings containing the registration information of students
        """
        for section in self.sections:
            print(f'{self.subject_code}-{self.course_number}-{section.section}:')
            for student in section.get_all_students():
                print(f'\t{student.first_name} {student.last_name} ({student.id})')

    def faculty_add_materials(self, faculty: User, course_code: str, section_number: str, new_material: str) -> Errors:
        if self.subject_code + '-' + self.course_number == course_code:
            for section in self.sections:
                if section.section == section_number:
                    if section.professor == faculty:
                        section.add_material(new_material)
                        return Errors.SUCCESS
                    else:
                        return Errors.NOT_AUTHORIZED
        return Errors.FAILED_TO_LOCATE


class Section:
    """
    Section contains the rest of information required for a class
    It also includes a list of students who are enrolled in the course
    """

    def __init__(self,
                 section: str, seats: int,
                 building: str, room: str,
                 days: str, start_time: str, end_time: str,
                 books: List[str], materials: List[str]):
        # Section Number
        self.section: str = section
        self.parent_course: Course = {}

        self.professor = {}
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
        self.books.append(book)

    def add_student(self, student) -> Errors:
        if self.available_seats > 0:
            self.__students.append(student)
            self.available_seats -= 1
            return Errors.SUCCESS
        else:
            return Errors.SECTION_FULL
    
    def remove_student(self, student) -> Errors:
        try: 
            self.__students.remove(student)
            student.remove_section(self.parent_course,self)
            self.available_seats += 1
            return Errors.SUCCESS
        except:
            return Errors.FAILED_TO_LOCATE

    def remove_faculty(self) -> Errors:
        """
        Removes faculty from a section in the course
        """
        if type(self.professor) == User:
            self.professor.remove_section(self.parent_course, self)

        if self.professor == "":
            return Errors.NONE_ASSIGNED
        
        self.professor = ""
        return Errors.SUCCESS
        
    def assign_faculty(self, faculty: User) -> Errors:
        """
        Assigns a faculty to a section in the course
        """
        self.professor = faculty
        return Errors.SUCCESS

    def print(self, course: Course) -> None:
        """
        Run Course.print() before running this or output will look goofy
        """
        print(f'\n{course.title}')
        print(f'{course.subject_code}-{course.course_number}-{self.section}')
        print(f'{course.description}')
        print(f'\t{self.building}, {self.room}')
        print(f'\t{self.days} {self.start_time} - {self.end_time}')
        if type(self.professor) == Entities.User:
            print(f'\t{self.professor.first_name} {self.professor.last_name}')
        else:
            print("\tNo Professor Assigned")
        print(f'\tBooks:{self.books}')
        print(f'\tMaterials:{self.materials}')

    def get_student(self, student: int) -> User:
        return(self._Section__students[student])

    def get_all_students(self):
        return self.__students


"""
These are all helper functions that are not part of either class
"""

def load_courses(users: List[User]) -> List[Course]:
    """
    This will read courses from the data/courses.json\n
    returns a list of courses \n
    See the classes module for info about Course object
    """
    courses: Course = []

    with open("src/data/courses.json", 'r') as file:
        data = json.load(file)

    for subj in data.keys():
        for idx, code in enumerate(data[subj].keys()):
            title = data[subj][code]["title"]
            desc = data[subj][code]["description"]

            course = Course(subj, code, title, desc)
            courses.append(course)
            for sect in data[subj][code]["Sections"]:
                section = data[subj][code]["Sections"][sect]
                professor_id = str(section["Professor"])

                temp = Section(sect, section["Seats"],
                            section["Building"], section["Room"],
                            section["MeetingDays"], section["StartTime"], section["EndTime"],
                            section["Books"], section["Materials"]
                            )
                
                temp.parent_course = course

                professor: User = {}
                for acc in users:
                    if acc.get_id() == professor_id:
                        professor = acc
                        professor.add_section(course,temp)
                        break

                temp.assign_faculty(professor)

                courses[idx].sections.append(temp)

    return courses


def print_all_courses(courses: List[Course]) -> None:
    """
        Prints all sections and some of their information
    """
    for c in courses:
        for s in c.sections:
            s.print(c)

def print_all_sections_teaching(prof: User, courses: List[Course]) -> None:
    """
        Prints all sections and some of their information
    """
    i = 1
    for c in courses:
        for s in c.sections:
            if s.professor == prof:
                print(f'{i}. {c.subject_code}-{c.course_number}-{s.section}')
                i += 1

def print_students_in_sections_teaching(prof: User, courses: List[Course]) -> None:
    """
        Prints all sections and some of their information
    """
    i = 1
    j = 1
    for c in courses:
        for s in c.sections:
            if s.professor == prof:
                print(f'{i}. {c.subject_code}-{c.course_number}-{s.section}')
                for student in s._Section__students:
                    print(f'\t{j}. {student.first_name} {student.last_name}')
                    j += 1
                i += 1



def section_search(courses: List[Course], query: str) -> Tuple[Course, Section]:
    """
        Takes in list of courses and a string describing the course to be located\n
        The query string should be in the form\n
        \tCSC-1710-01\n
        \tDEPT-CODE-SECTION

        returns a tuple of (course,section) if found or (Errors.FAILED_TO_LOCATE, Errors.FAILED_TO_LOCATE)
    """
    while True: # tbh idk why this is here but im scared to remove it so

        dept, code, sect = query.upper().split('-')
        section: Section = Errors.FAILED_TO_LOCATE
        course: Course = Errors.FAILED_TO_LOCATE

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

# def admin_add_course(roster: List[Course], subj_code: str, number: str, title: str, desc: str, sections: List[Section]) -> None:
#     """
#     Adds a new course to the roster
#     """
#     course = Course(subj_code, number, title, desc)
#     for section in sections:
#         course.add_section(section)
#     roster.append(course)

# def admin_remove_course(roster: List[Course], subj_code: str, number: str) -> bool:
#     """
#     Removes a course from the roster based on subject code and course number
#     """
#     for i, course in enumerate(roster):
#         if course.subject_code == subj_code and course.course_number == number:
#             roster.pop(i)
#             return True
#     return False

