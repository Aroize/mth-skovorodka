import sqlite3

class DBOpenHelper:

	def __init__(self):
		self.db = sqlite3.connect("skovorodka.db")
		cursor = self.db.cursor()
		try:
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS users
				( 
					id int AUTO_INCREMENT PRIMARY KEY,
					email varchar(50) NOT NULL,
					pwd varchar(50) NOT NULL,
					name varchar(30) NOT NULL,
					surname varchar(30) NOT NULL,
					age int NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS papers
				(
					id int AUTO_INCREMENT PRIMARY KEY,
					path varchar(200) NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS favs
				(
					u_id int NOT NULL,
					p_id int NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS cosine
				(
					first int NOT NULL,
					second int NOT NULL,
					cosine float NOT NULL
				)
				"""
			)
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS stats
				(
					u_id int NOT NULL,
					p_id int NOT NULL,
					ts long NOT NULL,
					type varchar(20)
				)
				"""
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
				pass
			return None
		except:
			return None
		finally:
			cursor.close()


db_helper = DBOpenHelper()

