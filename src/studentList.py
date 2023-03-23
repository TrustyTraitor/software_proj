import json

#open the file
with open('./data/users.json', 'r') as file:
    #read the file
    users = json.load(file)

#create an empty list
students = []

#loop through the users
for user in users:
    #if the user is a student, append the user's name to the students list
    if user['type'] == 'student':
        students.append(user['first_name'] + ' ' + user['last_name'])

#print the list of students
print(students)

