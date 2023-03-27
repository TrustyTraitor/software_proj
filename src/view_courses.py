import json

from classes.Course import Course
from classes.Course import Section


class View_Courses:
    def get_courses() -> Course:
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
                                section["MeetingDays"], section["StartTime"], section["EndTime"]
                                )
                    )

        return courses

    def print_courses(courses: Course):
        for c in courses:
            for s in c.sections:
                c.print()
                s.print()


if __name__ == '__main__':
    courses: Course = View_Courses.get_courses()
    View_Courses.print_courses(courses)
