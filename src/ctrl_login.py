from Entities.User import User

from typing import List

class ctrl_Login:	
	def Login(users: List[User], id: str, password: str):
		for u in users:
			if u.id != id:
				continue
			if u.password != password:
				continue
			
			return u
		return 0
