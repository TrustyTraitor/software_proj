import json

class StudentReporter:
    def __init__(self):
        with open('./data/users.json', 'r') as file:
            self.users = json.load(file)
        self.students = []
        for user in self.users:
            if user['type'] == 'student':
                self.students.append(user)

    def generate_report(self, student):
        report = ''
        report += 'Name: ' + student['first_name'] + ' ' + student['last_name'] + '\n'
        report += 'Email: ' + student['email'] + '\n'
        report += 'Courses:\n'
        for course in student['courses']:
            report += '- ' + course['name'] + '\n'
            report += '  Teacher: ' + course['teacher'] + '\n'
            report += '  Grade: ' + str(course['grade']) + '\n'
        return report

    def generate_reports(self):
        for student in self.students:
            report = self.generate_report(student)
            print(report)

if __name__ == '__main__':
    student_reporter = StudentReporter()
    student_reporter.generate_reports()

