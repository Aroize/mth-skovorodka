import mysql.connector
import json

class User:

	def __init__(self, id, email, pwd, name, surname, age):
		self.id = id
		self.name = name
		self.surname = surname
		self.email = email
		self.pwd = pwd
		self.age = age

	def args(self):
		if (self.id == -1):
			return (self.email, self.pwd, self.name, self.surname, self.age)
		return (self.id, self.email, self.pwd, self.name, self.surname, self.age)

	def json(self):
		return json.dumps({
			"id": self.id,
			"name": self.name,
			"surname": self.surname,
			"email": self.email,
			"age": self.age
		})




class DBOpenHelper:

	def __init__(self):
		self.connection = mysql.connector.connect(host='localhost',database='kgraph',user='root',password='root')


	def get_user_by_id(self, uid):
		cursor = self.connection.cursor()
		sql = "SELECT * FROM users WHERE id = %s"
		args = (str(uid), )
		cursor.execute(sql, args)
		result = cursor.fetchone()
		if result != None:
			return User(*result)
		return None


	def get_user_by_email(self, email):
		cursor = self.connection.cursor()
		sql = "SELECT * FROM users WHERE email = %s"
		args = (email, )
		cursor.execute(sql, args)
		result = cursor.fetchone()
		if result != None:
			return User(*result)
		return None


	def insert_user(self, user):
		sql = "INSERT INTO users (email, pwd, name, surname, age) VALUES (%s, %s, %s, %s, %s)"
		args = user.args()
		cursor = self.connection.cursor()
		cursor.execute(sql, args)
		self.connection.commit()

	def close(self):
		self.connection.close()


db_helper = DBOpenHelper()