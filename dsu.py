class DSU:
    parent = {}
    rank = {}

    def make_set(self, universe):
        for i in universe:
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

    def print_sets(self):
        print([self.find(i) for i in universe])


if __name__ == '__main__':
    pass
