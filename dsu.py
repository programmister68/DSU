class DSU:

    def __init__(self, n):  # Инициализация множества с n-числом данных
        self.rank = [1] * n
        self.parent = [i for i in range(n)]

    def find(self, x):  # Возвращает множество, в котором находится указанный элемент
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):  # Объединение множеств
        x_set = self.find(x)
        y_set = self.find(y)

        if x_set == y_set:
            return
        if self.rank[x_set] < self.rank[y_set]:
            self.parent[x_set] = y_set

        elif self.rank[x_set] > self.rank[y_set]:
            self.parent[y_set] = x_set

        else:
            self.parent[y_set] = x_set
            self.rank[x_set] = self.rank[x_set] + 1


class DataBase:
    pass


class GUI:
    pass


if __name__ == '__main__':
    set_dsu = DSU(10)  # set_dsu - переменная принимающее значения из класса DSU
    # set_dsu.union(1, 0)
    # set_dsu.union(1, 2)
    # set_dsu.union(5, 2)
    # set_dsu.union(7, 4)
    if set_dsu.find(1) == set_dsu.find(0):
        print('Тест 1. Значения', set_dsu.find(1), 'и', set_dsu.find(0), 'совпадают, множество уже объединено')
    else:
        print('Тест 1. Значения', set_dsu.find(1), 'и', set_dsu.find(0), 'не совпадают, объединяем')

        set_dsu.union(1, 0)

    if set_dsu.find(1) == set_dsu.find(0):
        print('Тест 1. Значения', set_dsu.find(1), 'и', set_dsu.find(0), 'совпадают, множество уже объединено')
    else:
        print('Тест 1. Значения', set_dsu.find(1), 'и', set_dsu.find(0), 'не совпадают, объединяем')

    if set_dsu.find(2) == set_dsu.find(5):
        print('Тест 2. Значения', set_dsu.find(2), 'и', set_dsu.find(5), 'совпадают, множество уже объединено')
    else:
        print('Тест 2. Значения', set_dsu.find(2), 'и', set_dsu.find(5), 'не совпадают, объединяем')

        set_dsu.union(2, 5)

    if set_dsu.find(2) == set_dsu.find(5):
        print('Тест 2. Значения', set_dsu.find(2), 'и', set_dsu.find(5), 'совпадают, множество уже объединено')
    else:
        print('Тест 2. Значения', set_dsu.find(2), 'и', set_dsu.find(5), 'не совпадают, объединяем')
