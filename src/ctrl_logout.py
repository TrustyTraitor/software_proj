from Entities.User import User
from Entities.Errors import Errors

class ctrl_Logout:	
	def Logout(u: User):
		print(f'Goodbye, {u.first_name} {u.last_name}!')
		return Errors.SUCCESS
