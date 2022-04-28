from DataBase import DataBase
from dsu import DSU


class Facade:

    def __init__(self, name='dsu_DB.db'):
        self.DB = DataBase(name)
        self.dsu = DSU()
        self.build()

    def build(self):
        data = self.DB.get_from_db()
        print('получил', data)
        if data is not None:
            data = data.split(', ')
            for i in data:
                i = int(i)
                self.dsu.push(i)
                self.dsu.make_set()
            print(data)

    def make_set(self):
        self.dsu.make_set()

    def union(self, a, b):
        self.dsu.union(a, b)

    def find(self, k):
        return self.dsu.find(k)

    def push(self, item):
        self.dsu.push(item)

    def print_sets(self):
        return self.dsu.print_sets()

    def saveDB(self):
        value = self.dsu.print_sets()
        self.DB.insert(value)

    def loadDB(self):
        self.DB.load_last()

    def deleteDB(self):
        self.DB.del_all()


if __name__ == '__main__':
    # facade = Facade()
    # facade.push(6)
    # facade.push(8)
    # facade.push(1)
    # facade.make_set()
    # facade.union(8, 6)
    # facade.saveDB()
    # print(facade.find(8))
    # print(facade.find(6))
    # print(facade.find(1))
    pass
