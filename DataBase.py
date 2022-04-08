from sqlite3 import connect


class DataBase:
    def __init__(self, name):
        self.conn = connect(f"{name}")
        cursor = self.conn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXIST unions (id INTEGER PRIMARY KEY AUTOINCREMENT, unions TEXT)")
        self.conn.commit()
        cursor.close()

    def insert(self, data):
        if data == 'None':
            data = None
        cursor = self.conn.cursor()
        cursor.execute(f"""INSERT INTO unions (unions) VALUES ('{data}')""")
        self.conn.commit()
        cursor.close()

    def get_id(self):
        cursor = self.conn.cursor()
        list_id = [str(i)[1:-2] for i in cursor.execute("SELECT id FROM unions")]
        cursor.close()
        return list_id

    def delete_unions(self):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM unions")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name = 'unions'")
        cursor.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'unions'")
        self.conn.commit()
        cursor.close()