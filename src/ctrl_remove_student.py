class CourseAssign:
    def __init__(self, users):
        self.users = users
        self.students = [f'{user.first_name} {user.last_name}' for user in self.users if user.u_type == 'student']
        self.course = input('What course would you like to modify? ')

    def assign_students(self):
        for student in self.students:
            assign = input(f'Would you like to assign {student} to {self.course}? (y/n) ')
            if assign == 'y':
                print(f'{student} has been assigned to {self.course}')

    def remove_students(self):
        while True:
            remove_student = input('Enter the name of the student to remove: ')
            if remove_student not in self.students:
                print('Student not found in course.')
            else:
                confirm = input(f'Are you sure you want to remove {remove_student} from {self.course}? (y/n) ')
                if confirm == 'y':
                    self.students.remove(remove_student)
                    print(f'{remove_student} has been removed from {self.course}.')
                break

if __name__ == '__main__':
    # Create an instance of the CourseAssign class and call the assign_students and remove_students methods
    course_assign = CourseAssign()
    course_assign.assign_students()
    course_assign.remove_students()
