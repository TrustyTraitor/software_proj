import json

class StudentReporter:
    def __init__(self):
        # Load the user data from the JSON file
        with open('./data/users.json', 'r') as file:
            self.users = json.load(file)

        # Create a list of student objects
        self.students = []
        for user in self.users:
            if user['type'] == 'student':
                self.students.append(user)

    def generate_report(self, student):
        # Generate a report for a single student
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
        # Generate a report for each student in the students list
        for student in self.students:
            report = self.generate_report(student)
            print(report)

if __name__ == '__main__':
    # Create an instance of the StudentReporter class and call the generate_reports method
    student_reporter = StudentReporter()
    student_reporter.generate_reports()
