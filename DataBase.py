import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)


class DataBase:

    def __init__(self, name):
        self.db = sqlite3.connect(f"{name}")
        sql = self.db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS dsu ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            sets INTEGER
        )""")
        self.db.commit()
        sql.close()

    def get_from_db(self):
        sql = self.db.cursor()
        data = [value for value in sql.execute(f"SELECT * FROM dsu")]
        if not data:
            logging.log(logging.INFO, ' база данных пуста')
        sql.close()
        return data

    def del_all(self):
        cur = self.db.cursor()
        cur.execute("DELETE from dsu")
        self.db.commit()

    def insert(self, data):
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO dsu (sets) VALUES ('{data}')""")
        self.db.commit()
        cur.close()

    def load_last(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT sets FROM dsu WHERE id = (SELECT MAX(id) FROM dsu)')
        value = cursor.fetchone()
        cursor.close()
        return value
