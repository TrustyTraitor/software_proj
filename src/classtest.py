import json

# Opening JSON file
f = open('./data/users.json')

# returns JSON object as a dictionary
data = json.load(f)

#
class User:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

class Login:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def authenticate(self) -> bool:
        try:
            return self.name == data[self.id].get("name") and self.id == data[self.id].get("id")
        except:
            return False

name = input("Enter your name: ")
id = int(input("Enter your id: "))
currentUser = User(name=name, id=id)

currentLogin = Login(name=currentUser.name, id=currentUser.id)

is_authenticated = currentLogin.authenticate()
print(is_authenticated)  



#close JSON file
f.close()

