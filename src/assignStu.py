import json

class CourseAssigner:
    def __init__(self):
        # Load the user data from the JSON file
        with open('./data/users.json', 'r') as file:
            self.users = json.load(file)

        # Create an empty list to store the students
        self.students = []
        for user in self.users:
            # If the user is a student, add their name to the students list
            if user['type'] == 'student':
                self.students.append(user['first_name'] + ' ' + user['last_name'])

        # Prompt the user to enter a course name
        self.course = input('What course would you like to assign students to? ')

    def assign_students(self):
        # Loop through the list of students and ask the user if they want to assign each student to the course
        for student in self.students:
            assign = input(f'Would you like to assign {student} to {self.course}? (y/n) ')
            
            # If the user answers yes, print a message indicating that the student has been assigned to the course
            if assign == 'y':
                print(f'{student} has been assigned to {self.course}')

if __name__ == '__main__':
    # Create an instance of the CourseAssigner class and call the assign_students method
    course_assigner = CourseAssigner()
    course_assigner.assign_students()


