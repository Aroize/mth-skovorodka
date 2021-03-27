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

achivements_naming = {
"Новичок":1,
 "Воспитанник":2,
 "Последователь":3,
 "Адепт":4,
 "Ученик физ-мат Лицея":5,
 "Подмастерье":7,
 "Любитель":10,
 "Мастер":15,
"Гранд-Мастер":20,
"Гений":25,
"Илон Маск":27,
"Стивен Хоккинг":30
}

class DBOpenHelper:

	def __init__(self):
		self.db = sqlite3.connect("skovorodka2.db")
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
					u_id INTEGER NOT NULL,
					p_id INTEGER NOT NULL,
					ts long NOT NULL,
					type STRING
				)
				"""
			# cursor.execute("""
			# 	CREATE TABLe IF NOT EXISTS achievements
			# 	(
			# 	  universe int not NULL,
			# 	  universe_name varchar(20),
			# 	  movements int not NULL,
			# 	  movements_name varchar(20),
			# 	  substance int not NULL,
			# 	  substance_name varchar(20),
			# 	  brain INT NOT NULL,
			# 	  brain_name varchar(20),
			# 	  energy INT NOT NULL,
			# 	  energy_name varchar(20),
			# 	  it int NOT NULL,
			# 	  it_name varchar(20),
			# 	  materials int not null,
			# 	  materials_name varchar(20),
			# 	  medicine int not null,
			# 	  medicine_name varchar(20),
			# 	  science int not null,
			# 	  science_name varchar(20),
			# 	  language int not null,
			# 	  language_name varchar(20)
			# 	  )
			# 	  """
			# )
			)
		except:
			pass
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
		except:
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
		except:
			return None
		finally:
			cursor.close()
		
			


db_helper = DBOpenHelper()

