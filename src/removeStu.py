import json

class CourseRemover:
    def __init__(self):
        with open('./data/courses.json', 'r') as file:
            self.courses = json.load(file)
        self.course_name = input("Which course do you want to remove a student from? ")

    def remove_student(self):
        for course in self.courses:
            if course['name'] == self.course_name:
                print("The following students are in " + self.course_name + ":")
                for student in course['students']:
                    print("- " + student)
                student_name = input("Which student do you want to remove from " + self.course_name + "? ")
                if student_name in course['students']:
                    course['students'].remove(student_name)
                    print(student_name + " has been removed from " + self.course_name)
                    with open('./data/courses.json', 'w') as file:
                        json.dump(self.courses, file)
                    break
                else:
                    print(student_name + " is not in " + self.course_name)
                    break
        else:
            print(self.course_name + " does not exist")

if __name__ == '__main__':
    course_remover = CourseRemover()
    course_remover.remove_student()

