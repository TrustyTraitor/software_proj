import json

class CourseAssigner:
    def __init__(self):
        with open('./data/users.json', 'r') as file:
            self.users = json.load(file)
        self.students = []
        for user in self.users:
            if user['type'] == 'student':
                self.students.append(user['first_name'] + ' ' + user['last_name'])
        self.course = input('What course would you like to assign students to? ')

    def assign_students(self):
        for student in self.students:
            assign = input(f'Would you like to assign {student} to {self.course}? (y/n) ')
            if assign == 'y':
                print(f'{student} has been assigned to {self.course}')

if __name__ == '__main__':
    course_assigner = CourseAssigner()
    course_assigner.assign_students()

    
