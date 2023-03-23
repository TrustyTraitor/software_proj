# This code opens a JSON file, reads the data from it, creates a User and Login class, 
# creates an instance of the Login class, and then uses the authenticate method to check 
# if the user's name and id match with the data from the JSON file. If so, the authentication 
# will be successful and will return true. Otherwise, it will return false.

import json

# Opening JSON file
f = open('./data/users.json')

# returns JSON object as a dictionary
data = json.load(f)

#
class User:
    def __init__(self, id: int, password: str):
        self.password = password
        self.id = id
        self.type = type

class Login:
    def __init__(self, password: str, id: int):
        self.password = password
        self.id = id

    def authenticate(self) -> bool:
        try:
            return self.password == data[self.id].get("password") and self.id == data[self.id].get("id")
        except:            
            return False
    def populateUser(self, user: User):
        user.id = data[self.id].get("id")
        user.password = data[self.id].get("password")
        user.type = data[self.id].get("type")


id = int(input("Enter your id: "))
password = str(input("Enter your password: "))

currentUser = User(id=id, password=password)

currentLogin = Login(id=currentUser.id, password=currentUser.password)

is_authenticated = currentLogin.authenticate()
print(is_authenticated)  
currentLogin.populateUser(currentUser)
print(currentUser.type)


#close JSON file
f.close()

