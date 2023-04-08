from typing import List
from Entities.Course import Course, Section

class ctrl_Admin_Add_Course:
    def add_course(roster: List[Course], subj_code: str, number: str, title: str, desc: str, sections: List[Section]) -> None:
        Course.admin_add_course(roster, subj_code, number, title, desc, sections)
