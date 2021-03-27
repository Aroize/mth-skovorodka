from tornado.web import RequestHandler
from tornado.web import HTTPError
from db import *


class AuthHandler(RequestHandler):

    @staticmethod
    def get_mapping():
        return "/user.auth"

    def data_received(self, chunk):
        pass

    def get(self, *args, **kwargs):
    	email = self.get_argument("email")
    	user = db_helper.get_user_by_email(email)
    	
    	if user == None:
    		self.set_status(401)
    		self.write("{\"msg\": \"Wrong email\"}")
    		return
    	
    	pwd = self.get_argument("pwd")
    	if user.pwd != pwd:
    		self.set_status(401)
    		self.write("{\"msg\": \"Wrong password\"}")
    	
    	self.write(user.json())


class RegisterHandler(RequestHandler):

	@staticmethod
	def get_mapping():
		return "/user.register"

	def data_revecived(self, chunk):
		pass

	def get(self, *args, **kwargs):
		email = self.get_argument("email")
		user = db_helper.get_user_by_email(email)
		
		if user != None:
			self.set_status(409)
			self.write("{\"msg\": \"User with this email already exists\"}")
			return

		pwd = self.get_argument("pwd")

		if len(pwd) < 8:
			self.set_status(400)
			self.write("{\"msg\": \"Password must be 8 symbols length at least\"}")
			return			

		name = self.get_argument("name")
		surname = self.get_argument("surname")
		age = self.get_argument("age")

		db_helper.insert_user(User(-1, email, pwd, name, surname, age))
		self.write(db_helper.get_user_by_email(email).json())


class 




		

