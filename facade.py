from DataBase import DataBase
from dsu import DSU


class Facade:

    def __init__(self, name='dsu_DB.db'):
        self.DB = DataBase(name)
        self.dsu = DSU()

    def make_set(self): #Создаёт множество
        self.dsu.make_set()

    def union(self, a, b): #Объединяет элементы
        self.dsu.union(a, b)

    def find(self, k): #Создаёт множество
        self.dsu.find(k)

    def push(self, item): #Создаёт множество
        self.dsu.push(item)

    def print_sets(self): #Создаёт множество
        self.dsu.print_sets()

    def saveDB(self): #Создаёт множество
        value = self.dsu.print_sets()
        self.DB.insert(value)

if __name__ == '__main__':
    facade = Facade()
    facade.push(6)
    facade.push(1)
    facade.push(8)
    facade.push(3)
    facade.make_set()
    facade.print_sets()

    facade.union(6, 1)

    facade.print_sets()

    facade.union(8, 3)
