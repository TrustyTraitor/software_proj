from Entities.User import User

class ctrl_Logout:	
	def Logout(u: User):
		print(f'Goodbye {u.first_name.capitalize()}!')
		return 0
