class DSU:
    """
    Структура данных система непересекающихся множеств.
    """
    def __init__(self):
        """
        Структура данных система непересекающихся множеств
        """
        self.parent = {}
        self.rank = {}
        self.universe = []
        self.result = []
        self.listSet = []

    def make_set(self):
        """
        Функция добавляющая введённые элементы в список
        :return: None
        """
        for i in self.universe:
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, k):
        """
        Функция, осуществляющая поиск представителя (родителя) элемента
        :param k: искомый элемент
        :return: parent[k]
        """
        try:
            if self.parent[k] != k:
                self.parent[k] = self.find(self.parent[k])
            return self.parent[k]
        except LookupError:
            return False

    def union(self, a, b):
        """
        Функция, объединяющее два элемента в одно единое множество
        :param a: первый объединяемый элемент
        :param b: первый объединяемый элемент
        :return: None
        """
        x = self.find(a)
        y = self.find(b)
        if x == y:
            return x == y
        if self.rank[x] > self.rank[y]:
            self.parent[y] = x
        elif self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[x] = y
            self.rank[y] = self.rank[y] + 1

    def push(self, item):
        """
        Функция, добавляющая элементы в структуру данных
        :param item: добавляемый элемент
        :return: None
        """
        self.universe.append(item)

    def print_sets(self):
        """
        Функция, выводящая список множеств
        :return: listSet
        """
        self.result = [self.find(i) for i in self.universe]
        self.listSet = []

        self.listSet.append(self.result)

        print(self.listSet)
        return self.listSet
