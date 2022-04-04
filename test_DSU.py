import unittest

from dsu import DSU


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        universe = [1, 6, 3, 4, 5]
        self.dsu = DSU()
        self.dsu.make_set(universe)

    def test_union(self):
        self.dsu.union(6, 1)
        self.assertEqual({1: 1, 3: 3, 4: 4, 5: 5, 6: 1}, self.dsu.parent)

    def test_find(self):
        self.dsu.union(6, 1)
        self.dsu.find(6)
        self.assertEqual(self.dsu.parent[1], self.dsu.parent[6])


if __name__ == 'main':
    pass
