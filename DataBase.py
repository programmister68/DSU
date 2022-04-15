import sqlite3
import logging
logging.basicConfig(level=logging.INFO)
# logging.disable(logging.INFO)


class DataBase:
    """
    класс с функциями дли взаимодействия с базой данных
    """
    def __init__(self, name):
        """
        создает базу данных
        :param name: имя базы данных
        """
        self.db = sqlite3.connect(f"{name}")
        sql = self.db.cursor()
        sql.execute("""CREATE TABLE IF NOT EXISTS dsu ( 
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            sets INTEGER
        )""")
        self.db.commit()
        sql.close()

    def get_from_db(self):
        """
        Возвращает все значения из базы данных в переменной data
        :return: data
        """
        sql = self.db.cursor()
        data = [value for value in sql.execute(f"SELECT * FROM dsu")]
        if not data:
            logging.log(logging.INFO, ' база данных пуста')
        sql.close()
        return data

    def del_all(self):
        """
        Вспомогательная функция для save_all.
        Удаляет все данные в базе данных.
        :return: None
        """
        cur = self.db.cursor()
        cur.execute("DELETE from dsu")
        self.db.commit()

    def insert(self, data):
        """
        функция для вставки данных в базу данных
        :param key: ключ, который вставляем в базу данных
        :param data: данные, которые вставляем в базу данных
        :return: None
        """
        cur = self.db.cursor()
        cur.execute(f"""INSERT INTO dsu (sets) VALUES ('{data}')""")
        self.db.commit()
        cur.close()

    def save_all(self, path):
        """
        Переписывает все старые данные на новые - удаляет данные и записывает текущие
        :param path: путь обхода структуры данных
        :return: None
        """
        self.del_all()
        for val in path:
            if val[1] is not None:
                self.insert(val[0], val[1])
