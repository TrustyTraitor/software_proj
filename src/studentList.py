class StudentList:

    def list_students(self, users):
        for user in self.users:
            if user.u_type == 'student':
                print(user.print)

if __name__ == '__main__':
    # Create an instance of the StudentLister class and call the list_students method
    student_list = StudentList()
    student_list.list_students()


