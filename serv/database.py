import sqlite3

class User:

	def __init__(self, id, email, pwd, name, surname, age):
		self.id = id
		self.email = email
		self.pwd = pwd
		self.name = name
		self.surname = surname
		self.age = age

	def json(self):
		return {
			'id': self.id,
			'email': self.email,
			'name': self.name,
			'surname': self.surname,
			'age': self.age
		}

class DBOpenHelper:

	def __init__(self):
		self.db = sqlite3.connect("skovorodka3.db")
		cursor = self.db.cursor()
		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS users
				( 
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					email STRING NOT NULL,
					pwd STRING NOT NULL,
					name STRING NOT NULL,
					surname STRING NOT NULL,
					age INTEGER NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS papers
				(
					id INTEGER PRIMARY KEY AUTOINCREMENT,
					path STRING NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS favs
				(
					u_id INTEGER NOT NULL,
					p_id INTEGER NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS cosine
				(
					first INTEGER NOT NULL,
					second INTEGER NOT NULL,
					cosine FLOAT NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS stats
				(
					event_id INTEGER PRIMARY KEY AUTOINCREMENT,
					u_id INTEGER NOT NULL,
					p_id INTEGER NOT NULL,
					ts long NOT NULL,
					type STRING
				)
				"""
			)
		except Exception as e:
			print(e)
			return None
		finally:
			cursor.close()



	def user_by_email(self, email):
		cursor = self.db.cursor()
		try:
			sql = "SELECT * FROM users WHERE email=?"
			result = cursor.execute(sql, (email,))
			user = result.fetchone()
			if user != None:
				return User(*user)
			return None
		except Exception as e:
			print(e)
			return None
		finally:
			cursor.close()

	def insert_user(self, email, pwd, name, surname, age):
		cursor = self.db.cursor()
		try:
			sql = "INSERT INTO users (email, pwd, name, surname, age) VALUES {}"
			args = (email, pwd, name, surname, age)
			cursor.execute(sql.format(args))
			self.db.commit()
			id = cursor.lastrowid
			return User(id, email, pwd, name, surname, age)	
		except Exception as e:
			print(e)
			return None
		finally:
			cursor.close()


	def register_stat(self, uid, p_id, ts, event_type):
		cursor = self.db.cursor()
		try:
			sql = "INSERT INTO stats (u_id, p_id, ts, type) VALUES {}"
			args = (uid, p_id, ts, event_type)
			cursor.execute(sql.format(args))
			self.db.commit()
			return True
		except Exception as e:
			print(e)
			return None
		finally:
			cursor.close()

	def add_to_fave(self, uid, p_id):
		cursor = self.db.cursor()
		try:
			check_sql = "SELECT * FROM favs WHERE u_id=? and p_id=?"
			args = (uid, p_id)
			result = cursor.execute(check_sql, args).fetchall()
			if len(result) == 0:
				sql = "INSERT INTO favs (u_id, p_id) VALUES {}"
				cursor.execute(sql.format(args))
				self.db.commit()
				return True
			else:
				return False
		except Exception as e:
			print(e)
			return None
		finally:
			cursor.close()


	def remove_from_favs(self, uid, p_id):
		cursor = self.db.cursor()
		try:
			check_sql = "SELECT * FROM favs WHERE u_id=? and p_id=?"
			args = (uid, p_id)
			result = cursor.execute(check_sql, args).fetchall()
			if len(result) == 0:
				return False
			sql = "DELETE FROM favs WHERE u_id=? and p_id=?"
			cursor.execute(sql.format(args))
			self.db.commit()
			return True
		except Exception as e:
			print(e)
			return None


		
			


db_helper = DBOpenHelper()

