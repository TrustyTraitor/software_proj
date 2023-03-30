# This code opens a JSON file, reads the data from it, creates a User and Login class,
# creates an instance of the Login class, and then uses the authenticate method to check
# if the user's name and id match with the data from the JSON file. If so, the authentication
# will be successful and will return true. Otherwise, it will return false.

# import json

from classes.User import User

from typing import List


class Login:
    def login(users: List[User], id: str, password: str):
        for u in users:
            if u.id != id:
                continue
            if u.password != password:
                continue
            
            return u
        return 0
            

# Opening JSON file
# f = open('./data/users.json')


#
# class User:
#     def __init__(self, id: int, password: str):
#         self.password = password
#         self.id = id
#         self.type = str()
#         self.first_name = str()
#         self.last_name = str()
#         self.SSN = str()



# class Login:
#     def __init__(self, password: str, id: int):
#         self.password = password
#         self.id = id

#     def authenticate(self) -> bool:
#         try:
#             return self.password == data[self.id].get("password") and self.id == data[self.id].get("id")
#         except:            
#             return False
#     def populateUser(self, user: User):
#         user.id = data[self.id].get("id")
#         user.password = data[self.id].get("password")
#         user.type = data[self.id].get("type")
#         user.first_name = data[self.id].get("first_name")
#         user.last_name = data[self.id].get("last_name")
#         user.SSN = data[self.id].get("SSN")

# 	def login(user: User):
# 		# returns JSON object as a dictionary
# 		data = json.load(f)
                
# 		id = int(input("Enter your id: "))
# 		password = str(input("Enter your password: "))

# 		currentUser = User(id=id, password=password)

# 		currentLogin = Login(id=currentUser.id, password=currentUser.password)

# 		is_authenticated = currentLogin.authenticate()
# 		print(is_authenticated)  
# 		if is_authenticated:
# 			currentLogin.populateUser(currentUser)
# 			print(currentUser.first_name)
# 			print(currentUser.last_name)
# 			print(currentUser.SSN)
# 			print(currentUser.type)
			


# 		#close JSON file
# 		f.close()

