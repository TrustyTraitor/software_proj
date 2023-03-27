import json

class StudentLister:
    def __init__(self):
        # Load the user data from the JSON file
        with open('./data/users.json', 'r') as file:
            self.users = json.load(file)

        # Create an empty list to store the students
        self.students = []

    def list_students(self):
        # Loop through the users and add any students to the students list
        for user in self.users:
            if user['type'] == 'student':
                self.students.append(user['first_name'] + ' ' + user['last_name'])
        # Print the list of students
        print(self.students)

if __name__ == '__main__':
    # Create an instance of the StudentLister class and call the list_students method
    student_lister = StudentLister()
    student_lister.list_students()


