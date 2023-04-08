from typing import List
from Entities.Course import Course

class ctrl_Admin_Generate_Registration_Report:
    def generate_registration_report(course: Course) -> List[str]:
        return course.generate_student_registration_report()
