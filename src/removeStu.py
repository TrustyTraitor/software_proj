import json

with open('./data/courses.json', 'r') as file:
    courses = json.load(file)

course_name = input("Which course do you want to remove a student from? ")

for course in courses:
    if course['name'] == course_name:
        print("The following students are in " + course_name + ":")
        for student in course['students']:
            print("- " + student)
        student_name = input("Which student do you want to remove from " + course_name + "? ")
        if student_name in course['students']:
            course['students'].remove(student_name)
            print(student_name + " has been removed from " + course_name)
            # update the courses.json file
            with open('./data/courses.json', 'w') as file:
                json.dump(courses, file)
            break
        else:
            print(student_name + " is not in " + course_name)
            break
else:
    print(course_name + " does not exist")
