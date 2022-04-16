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

    def save_all(self, path):
        self.del_all()
        for val in path:
            if val[1] is not None:
                self.insert(val[0])
