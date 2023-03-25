import json

def generate_student_report(student):
    report = ''
    report += 'Name: ' + student['first_name'] + ' ' + student['last_name'] + '\n'
    report += 'Email: ' + student['email'] + '\n'
    report += 'Courses:\n'
    for course in student['courses']:
        report += '- ' + course['name'] + '\n'
        report += '  Teacher: ' + course['teacher'] + '\n'
        report += '  Grade: ' + str(course['grade']) + '\n'
    return report

with open('./data/users.json', 'r') as file:
    users = json.load(file)

# create a list of students
students = []
for user in users:
    if user['type'] == 'student':
        students.append(user)

# generate a report for each student
for student in students:
    report = generate_student_report(student)
    print(report)
