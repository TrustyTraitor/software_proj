import json

with open('./data/users.json', 'r') as file:
    users = json.load(file)

#create an empty list
students = []

for user in users:
    #if the user is a student, append the user's name to the students list
    if user['type'] == 'student':
        students.append(user['first_name'] + ' ' + user['last_name'])

#ask the user which course they want to assign students to
course = input('What course would you like to assign students to? ')

for student in students:
    #ask the user if they want to assign the student to the course
    assign = input('Would you like to assign ' + student + ' to ' + course + '? (y/n) ')
    
    #if they answer yes, assign the student to the course
    if assign == 'y':
        print(student + ' has been assigned to ' + course)