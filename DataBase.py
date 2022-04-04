import sqlite3


class DataBase:
    def save_db(self, data, name):
        conn = sqlite3.connect(name)
        cur = conn.cursor()
        cur.execute("""DROP TABLE IF EXISTS array;""")
        cur.execute("""CREATE TABLE array(
           id INT PRIMARY KEY,
           pos REAL,
           elem TEXT,
           next REAL)
        """)
        conn.commit()
        for rw in range(data.length()):
            p = rw*2
            cur.execute("""INSERT INTO array(id, pos, elem, next) 
            VALUES('{ids}', '{poss}', '{elems}', '{nexts}');""".format(ids=rw, poss=p, elems=data.arr[p], nexts=data.arr[p+1]))
            conn.commit()

    def load_db(self, path):
        conn = sqlite3.connect(path)
        cur = conn.cursor()
        cur.execute("SELECT * FROM array;")
        return cur
