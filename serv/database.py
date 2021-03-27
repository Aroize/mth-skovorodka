import os
import pandas as pd
import sqlite3

def extract_themes_and_tags():

	path = "./md/Word/"
	themes = os.listdir(path)
	paper_to_theme = {}

	for theme_id, theme in enumerate(themes, 0):
		for label in os.listdir(os.path.join(path, theme)):
			papers_path = os.path.join(path, theme, label)
			for paper in os.listdir(papers_path):
				csv_name = os.path.join(theme, label, paper) + ".docx"
				csv_kek = os.path.join(theme, label, paper) + " .docx"
				print(csv_name)
				paper_to_theme[csv_name] = theme_id
				paper_to_theme[csv_kek] = theme_id
	ids = pd.read_csv('ids.csv').values[:, :2]
	paper_id_to_paper_theme_id = {}
	for id, name in ids:
		name = name.replace('й', 'й')
		name = name.replace('Й', 'Й')
		name = name.replace('ё', 'ё')
		name = name.strip()
		theme_id = paper_to_theme[str(name)]
		paper_id_to_paper_theme_id[id] = theme_id
	print(paper_id_to_paper_theme_id)



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
		self.db = sqlite3.connect("skovorodka4.db")
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
			cursor.execute("""
				CREATE TABLE IF NOT EXISTS friends
				(
				     f_id INTEGER NOT NULL,
				     f_name STRING NOT NULL
				)
			    """
            )
			cursor.execute("""
            	CREATE TABLE IF NOT EXISTS user_themes
            	(
            		u_id INTEGER NOT NULL,
            		t_id INTEGER NOT NULL
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
			if user is not None:
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

	def find_user_by_id(self, id):
		cursor = self.db.cursor()
		try:
			sql = "SELECT * FROM users WHERE id=?"
			result = cursor.execute(sql, (id,))
			user = result.fetchone()
			if user is not None:
				return jsonify(user)
			return None
		except Exception as e:
			print(e)
			return None
		finally:
			cursor.close()

	def add_user_to_friend(self,id):
		cursor = self.db.cursor()
		try:
			sql = "SELECT * FROM users WHERE id=?"
			name = cursor.execute(sql,(id,))
			sql = "INSERT INTO friends(id, name) VALUES {}"
			args = (id, name)
			cursor.execute(sql.format(args))
			self.db.commit()
		except:
			return None
		finally:
			cursor.close()

	def user_pick_themes(self, uid, themes):
		cursor = self.db.cursor()
		try:
			for t_id in themes:
				sql = "INSERT INTO user_themes (uid, t_id) VALUES {}"
				args = (uid, t_id)
				cursor.execute(sql.format(args))
				cursor.db.commit()
			return True
		except Exception as e:
			print(e)
			return None
			


db_helper = DBOpenHelper()


if __name__ == "__main__":
	extract_themes_and_tags()