import json

class CourseRemover:
    def __init__(self):
        # Load the course data from the JSON file
        with open('./data/courses.json', 'r') as file:
            self.courses = json.load(file)

        # Prompt the user to enter a course name
        self.course_name = input("Which course do you want to remove a student from? ")

    def remove_student(self):
        for course in self.courses:
            if course['name'] == self.course_name:
                print("The following students are in " + self.course_name + ":")
                for student in course['students']:
                    print("- " + student)
                # Prompt the user to enter a student name to remove
                student_name = input("Which student do you want to remove from " + self.course_name + "? ")
                # If the student is in the course, remove them and print a message
                if student_name in course['students']:
                    course['students'].remove(student_name)
                    print(student_name + " has been removed from " + self.course_name)
                    with open('./data/courses.json', 'w') as file:
                        json.dump(self.courses, file)
                    break
                # If the student is not in the course, print a message indicating that they could not be removed
                else:
                    print(student_name + " is not in " + self.course_name)
                    break
        # If no course with the matching name is found, print a message
        else:
            print(self.course_name + " does not exist")

if __name__ == '__main__':
    course_remover = CourseRemover()
    course_remover.remove_student()
