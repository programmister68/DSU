class DSU:

    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.universe = []
        self.result = []
        self.listSet = []

    def make_set(self):
        for i in self.universe:
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, k):
        try:
            if self.parent[k] != k:
                self.parent[k] = self.find(self.parent[k])
            return self.parent[k]
        except LookupError:
            return False

    def union(self, a, b):
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
        self.universe.append(item)

    def print_sets(self):
        self.result = [self.find(i) for i in self.universe]
        self.listSet = []

        self.listSet.append(self.result)

        print(self.listSet)
        return self.listSet


if __name__ == '__main__':
    # ds = DSU()
    # ds.push(6)
    # ds.push(8)
    # ds.push(1)
    # ds.make_set()
    # print('____BEFORE________')
    # ds.print_sets()
    # ds.union(8, 6)
    # print('____AFTER_________')
    # ds.print_sets()
    # print(' ')
    # print('PARENTS OF 8 and 6:')
    # print(ds.find(8))
    # print(ds.find(6))
    pass