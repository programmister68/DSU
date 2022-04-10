import logging
import sys

from DataBase import DataBase

from dsu import DSU


class Facade:
    """
    Класс фасада (шаблона проектирования)
    """
    def __init__(self, name='Tree_data.db'):
        """
        создание объекта базы данных, структуры данных и запись элементов из БД в структуру данных (функция build_tree).
        data_wait_for_save - False, если нет данных для сохранения, True, если есть данные для сохранения
        :param name: имя базы данных
        """
        sys.setrecursionlimit(31)    # максимальное кол-во рекурсий 2147483647
        self.data_wait_for_save = False
        self.dictionary = DSU()  # тут будет первый элемент
        self.DB = DataBase(name)
        self.build_tree()

    def build_tree(self):
        """
        запись элементов из БД в структуру данных
        :return: None
        """
        data = self.DB.get_from_db()
        if data != []:
            for a in data:
                self.dictionary.insert(a[0], a[1])

    def insert_value(self, key, data):
        """
        Вставка элементов в структуру данных
        :param key: ключ для вставки
        :param data: данные для вставки
        :return: None
        """
        self.data_wait_for_save = True
        self.dictionary.insert(key, data)

    def delete_value(self, key):
        """
        Удаление данных из структуры данных
        :param key: ключ, по которому нужно найти объект и удалить его
        :return: None
        """
        self.data_wait_for_save = True
        self.dictionary = self.dictionary.delete(key)

    def search_element_in_tree(self, key):
        """
        Поиск объекта в структуре данных
        :param key: ключ, по которому нужно найти объект
        :return: возвращает None если такого элемента нет или возвращает ссылку на объект с искомым ключом (key)
        """
        return self.dictionary.search_element(key)

    def bypass_tree(self):
        """
        Вызывает функцию обхода дерева
        :return: возвращает путь обхода, а на первом месте максимальная глубина дерева
        """
        return self.dictionary.bypass(0, [0])

    def save_data(self):
        """
        Если есть несохраненные данные (data_wait_for_save==True), тогда в БД записываются новые данные
        :return: None
        """
        if self.data_wait_for_save:
            self.data_wait_for_save = False
            path = self.dictionary.bypass(0, [0])
            path.pop(0)
            self.DB.save_all(path)
            logging.log(logging.INFO, ' данные добавлены в бд')
        else:
            logging.log(logging.INFO, ' нет несохраненных данных')

    def del_all_from_bst(self):
        """
        если в дереве есть хоть один ключ, тогда все данные в дереве удаляются
        :return: None
        """
        if self.dictionary.key is not None:
            self.data_wait_for_save = True
            self.dictionary = DSU()