# This code opens a JSON file, reads the data from it, creates a User and Login class,
# creates an instance of the Login class, and then uses the authenticate method to check
# if the user's name and id match with the data from the JSON file. If so, the authentication
# will be successful and will return true. Otherwise, it will return false.

# import json

from classes.User import User

from typing import List


def login(users: List[User], id: str, password: str):
	for u in users:
		if u.id != id:
			continue
		if u.password != password:
			continue
		
		return u
	return 0
