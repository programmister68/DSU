import logging
import sys

from DataBase import DataBase

from dsu import DSU


class Facade:
    """
    Класс фасада (шаблона проектирования)
    """
    def __init__(self, name='dsu_DB.db'):
        sys.setrecursionlimit(31)    # максимальное кол-во рекурсий 2147483647
        self.DB = DataBase(name)
        universe = []

        self.ds = DSU()

    def save(self):
        data = self.dsu.print_sets()
        self.DB.insert(data)
        self.dsu.make_set()

