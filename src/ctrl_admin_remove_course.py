from typing import List
from Entities.Course import Course

class ctrl_Admin_Remove_Course:
    def remove_course(roster: List[Course], course: Course) -> None:
        roster.remove(course)
