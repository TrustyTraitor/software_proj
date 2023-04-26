from typing import List
from Entities.Course import Course
from Entities.Course import Section


# subj_code: str, number: str,
# title: str, desc: str):

# section: str, seats: int,
# building: str, room: str,
# days: str, start_time: str, end_time: str,
# books: List[str], materials: List[str])

class ctrl_Admin_Add_Course:
    def add_course(courses_list: List[Course]):
        dept = input("Please Enter the Subject Code: (i.e. CSC, PSY)")
        code = input("Enter the course code: (i.e. 1710)")
        title = input("Enter the title: (i.e. Intro To Programming)")
        desc = input("Enter the description: ")
        
        section = "01"
        seats = int(input("Enter the number of seats: "))
        building = input("Enter the building: ")
        room = input("Enter the room number: ")
        days = input("Enter the days the class meets: ")
        start_time = input("Enter the start time: ")
        end_time = input("Enter the end time: ")
        books = []
        materials = []
        
        new_course = Course(dept,code,title,desc)
        new_section = Section(section, seats, building, room, days, start_time, end_time, books, materials)
        
        new_course.sections.append(new_section)
        
        courses_list.append(new_course)
        
