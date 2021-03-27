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
    		raise HTTPError(status_code=400, log_message='No such user')
    	self.write(user.json())


class RegisterHandler(RequestHandler):

	@staticmethod
	def get_mapping():
		return "/user.register"

	def data_revecived(self, chunk):
		pass

	def get(self):
		email = self.get_argument("email")
		user = db_helper.get_user_by_email(email)
		if user != None:
			raise HTTPError(status_code=409, log_message="User already exists")
		pwd = self.get_argument("pwd")
		name = self.get_argument("name")
		surname = self.get_argument("surname")
		age = self.get_argument("age")

		db_helper.insert_user(User(-1, name, surname, email, age))
		self.write(db_helper.get_user_by_email(email).json())

		

