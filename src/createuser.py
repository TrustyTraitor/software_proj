import json

# Get the user input
name = input('Please enter name: ')
id = input('Please enter the ID: ')

# Create the user object
user = {
  'id': id,
  'name': name,
#  'password': password,
#  'user_type': user_type
}

# Save the user to the JSON file
with open('./data/users.json', 'r') as file:
  users = json.load(file)

users.append(user)

with open('./data/users.json', 'w') as file:
  json.dump(users, file)

# Display the Success Message
print('User has been created successfully!')
