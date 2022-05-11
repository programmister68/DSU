import sqlite3
import logging
logging.basicConfig(level=logging.INFO)


class DataBase:
    """
    Класс, содержащий функции взаимодействия с Базой Данных.
    """
    def __init__(self, name):
        """
        Создание базы данных.
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

    def insert(self, data):
        """
        Функция вставки данных в Базу Данных.
        :param data: данные, которые добавляются в БД
        :return: None
        """
        self.del_all()
        cur = self.db.cursor()
        a = list(map(str, data[0]))  # преобразуем список int в список str
        # print(a)
        # print('вы вставили: ', ', '.join(a)) преобразуем список в одну строку
        cur.execute(f"""INSERT INTO dsu (sets) VALUES ('{', '.join(a)}')""")
        self.db.commit()
        cur.close()

    def load_last(self):
        """
        Выгрузка последней сохранённой версии списка
        :return: value
        """
        cursor = self.db.cursor()
        cursor.execute('SELECT sets FROM dsu WHERE id = (SELECT MAX(id) FROM dsu)')
        value = cursor.fetchone()
        cursor.close()
        return value

    def get_data_db(self):
        """
        Функция, получающая все данные из БД
        :return:
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
        """
        Функция удаляющая все данные из Базы Данных
        :return:
        """
        cur = self.db.cursor()
        cur.execute("DELETE from dsu")
        self.db.commit()
