from typing import List
from Entities.Course import Course

class ctrl_Admin_Generate_Registration_Report:
    def generate_registration_report(courses: List[Course]) -> List[str]:
        for course in courses:
            course.generate_student_registration_report()
