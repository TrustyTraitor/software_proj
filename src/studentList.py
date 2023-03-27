import json

class StudentLister:
    def __init__(self):
        with open('./data/users.json', 'r') as file:
            self.users = json.load(file)
        self.students = []

    def list_students(self):
        for user in self.users:
            if user['type'] == 'student':
                self.students.append(user['first_name'] + ' ' + user['last_name'])
        print(self.students)

if __name__ == '__main__':
    student_lister = StudentLister()
    student_lister.list_students()


