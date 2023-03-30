class CourseAssign:
    def __init__(self, users):
        self.users = users
        self.students = [f'{user.first_name} {user.last_name}' for user in self.users if user.u_type == 'student']
        self.course = input('What course would you like to assign students to? ')

    def assign_students(self):
        for student in self.students:
            assign = input(f'Would you like to assign {student} to {self.course}? (y/n) ')
            if assign == 'y':
                print(f'{student} has been assigned to {self.course}')

if __name__ == '__main__':
    # Create an instance of the CourseAssign class and call the assign_students method
    course_assign = CourseAssign()
    course_assign.assign_students()


