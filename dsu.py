
class DSU:

    def __init__(self):
        self.parent = {}
        self.rank = {}
        self.universe = []

    def make_set(self):
        for i in self.universe:
            self.parent[i] = i
            self.rank[i] = 0

    def find(self, k):
        if self.parent[k] != k:
            self.parent[k] = self.find(self.parent[k])
        return self.parent[k]

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
        #print(self.result)
        self.listSet = []

        self.listSet.append(self.result)

        print(self.listSet)
        return self.listSet



if __name__ == '__main__':
    pass
