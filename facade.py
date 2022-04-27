from DataBase import DataBase
from dsu import DSU


class Facade:

    def __init__(self, name='dsu_DB.db'):
        self.DB = DataBase(name)
        self.dsu = DSU()

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
