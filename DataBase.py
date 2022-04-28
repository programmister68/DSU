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

    def insert(self, data):
        self.del_all()
        cur = self.db.cursor()
        a = list(map(str, data[0]))  # преобразуем список интов в список строк
        # print(a)
        # print('вы вставили: ', ', '.join(a)) # преобразуем список в одну строку
        cur.execute(f"""INSERT INTO dsu (sets) VALUES ('{', '.join(a)}')""")
        self.db.commit()
        cur.close()

    def load_last(self):
        cursor = self.db.cursor()
        cursor.execute('SELECT sets FROM dsu WHERE id = (SELECT MAX(id) FROM dsu)')
        value = cursor.fetchone()
        cursor.close()
        return value

    def get_from_db(self):
        """
        Возвращает все значения из базы данных в переменной data
        :return: data
        """
        sql = self.db.cursor()
        data = [value for value in sql.execute(f"SELECT sets FROM dsu")]
        if not data:
            return None
        else:
            data = data[0][0]
        sql.close()
        return data

    def del_all(self):
        cur = self.db.cursor()
        cur.execute("DELETE from dsu")
        self.db.commit()
