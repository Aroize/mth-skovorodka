import os
import pandas as pd
import sqlite3

achivements_names = {
    "Новичок": 1,
    "Воспитанник": 2,
    "Последователь": 3,
    "Адепт": 4,
    "Ученик физ-мат Лицея": 5,
    "Подмастерье": 7,
    "Любитель": 10,
    "Мастер": 15,
    "Гранд-Мастер": 20,
    "Гений": 25,
    "Илон Маск": 27,
    "Стивен Хоккинг": 30
}


def extract_themes_and_tags():
    path = "./md/Word/"
    themes = os.listdir(path)
    paper_to_label = {}
    label_to_theme = {}

    labels_count = 0

    for theme_id, theme in enumerate(themes, 0):
        for label in os.listdir(os.path.join(path, theme)):
            label_to_theme[labels_count] = theme_id

            papers_path = os.path.join(path, theme, label)
            for paper in os.listdir(papers_path):
                csv_name = os.path.join(theme, label, paper) + ".docx"
                csv_kek = os.path.join(theme, label, paper) + " .docx"
                paper_to_label[csv_name] = labels_count
                paper_to_label[csv_kek] = labels_count

            labels_count += 1

    ids = pd.read_csv('ids.csv').values
    paper_id_to_dif = {}
    paper_id_to_label_id = {}
    for id, name, dif in ids:
        name = name.replace('й', 'й')
        name = name.replace('Й', 'Й')
        name = name.replace('ё', 'ё')
        name = name.strip()
        label_id = paper_to_label[name]
        paper_id_to_label_id[id] = label_id
        paper_id_to_dif[id] = dif

    cursor = db_helper.db.cursor()

    cursor.execute("""
    	DROP TABLE IF EXISTS paper_dif
    	""")

    cursor.execute("""
    	CREATE TABLE paper_dif ( p_id INTEGER NOT NULL, diff FLOAT NOT NULL )
    	""")
    sql = "INSERT INTO paper_dif ( p_id, diff ) VALUES {}"
    for row in paper_id_to_dif.items():
        cursor.execute(sql.format(row))
    db_helper.db.commit()

    cursor.execute("""
		DROP TABLE IF EXISTS paper_to_label
		"""
                   )
    cursor.execute("""
		CREATE TABLE paper_to_label ( p_id INTEGER NOT NULL, l_id INTEGER NOT NULL )
		"""
                   )
    sql = "INSERT INTO paper_to_label ( p_id, l_id ) VALUES {}"
    for row in paper_id_to_label_id.items():
        cursor.execute(sql.format(row))

    db_helper.db.commit()

    cursor.execute("""
		DROP TABLE IF EXISTS label_to_theme
		"""
                   )
    cursor.execute("""
		CREATE TABLE label_to_theme ( l_id INTEGER NOT NULL, t_id INTEGER NOT NULL )
		"""
                   )

    sql = "INSERT INTO label_to_theme ( l_id, t_id ) VALUES {}"

    for row in label_to_theme.items():
        cursor.execute(sql.format(row))
    db_helper.db.commit()

    print("Themes are fetched")


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
        self.db = sqlite3.connect("skovorodka_1_1.db")
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
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS achievements
                (
                  user_id INTEGER NOT NULL,
                  universe INTEGER NOT NULL,
                  movements INTEGER NOT NULL,
                  substance INTEGER NOT NULL,
                  brain INTEGER NOT NULL,
                  energy INTEGER NOT NULL,
                  it INTEGER NOT NULL,
                  materials INTEGER NOT NULL,
                  medicine INTEGER NOT NULL,
                  science INTEGER NOT NULL,
                  languages INTEGER NOT NULL
                  )
                  """
                           )
            # Jojo code
            cursor.execute("""
                            CREATE TABLE IF NOT EXISTS already_read
                            (
                                u_id INTEGER NOT NULL,
                                p_id INTEGER NOT NULL
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

    def add_user_to_friend(self, id):
        cursor = self.db.cursor()
        try:
            sql = "SELECT * FROM users WHERE id=?"
            name = cursor.execute(sql, (id,))
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

    def get_achievements(self, user_id, col_name):
        cursor = self.db.cursor()
        try:
            sql = "SELECT {} FROM achievements WHERE user_id=?".format(col_name)
            result = cursor.execute(sql, (user_id,)).fetchone()
            return jsonify(achivements_names[result])
        finally:
            cursor.close()

    def get_diff_range(self, u_id, r=6):
        cursor = self.db.cursor()
        try:
            sql = "SELECT t_id FROM user_themes WHERE u_id = ?"
            t_ids = cursor.execute(sql, (u_id,)).fetchall()

            labels = []
            sql = "SELECT l_id FROM label_to_theme WHERE t_id = ?"
            for t_id in t_ids:
                l_ids = cursor.execute(sql, (t_id,)).fetchall()
                labels.extend(l_ids)
            labels = set(labels)
            sql = "SELECT p_id FROM paper_to_label WHERE l_id = ?"
            papers = []
            for l_id in labels:
                p_ids = cursor.execute(sql, (l_id,)).fetchall()
                papers.extend(p_ids)
            papers = set(papers)

            sql = "SELECT p_id FROM paper_dif WHERE diff - {} < 3 OR {} - diff < 3".format(r, r)
            return cursor.execute(sql).fetchall()
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()

    def get_diff(self, p_id):
        cursor = self.db.cursor()
        try:
            sql = "SELECT diff FROM paper_dif WHERE p_id=?"
            result = cursor.execute(sql, (p_id,)).fetchone()
            return result
        finally:
            cursor.close()

    def insert_already_read(self, u_id, p_id):
        cursor = self.db.cursor()
        try:
            check_sql = "SELECT * FROM already_read WHERE u_id=? and p_id=?"
            args = (u_id, p_id)
            result = cursor.execute(check_sql, args).fetchall()
            if len(result) == 0:
                sql = "INSERT INTO already_read (u_id, p_id) VALUES {}"
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

    def clicked_on_paper(self, u_id, p_id):
        self.insert_already_read(u_id, p_id)
        cursor = self.db.cursor()
        try:
            sql = "SELECT * FROM paper_to_label WHERE p_id=?"
            args = (p_id,)
            path = cursor.execute(sql, args).fetchall()
            if len(path) != 0:
                return path
            else:
                print("Could not find paper with id", p_id)
                return None
        except Exception as e:
            print(e)
            return None
        finally:
            cursor.close()


db_helper = DBOpenHelper()

extract_themes_and_tags()
