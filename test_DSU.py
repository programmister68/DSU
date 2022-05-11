import unittest

from dsu import DSU


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        self.dsu = DSU()
        self.dsu.push(1)
        self.dsu.push(6)
        self.dsu.push(10)
        self.dsu.make_set()

    def test_union(self):
        self.dsu.union(6, 1)
        self.assertEqual({1:1, 6:1, 10:10}, self.dsu.parent)

    def test_find(self):
        self.dsu.find(6)
        self.assertEqual(self.dsu.parent[6], 6)

    def test_parent_is_equal(self):
        self.dsu.union(6, 1)
        self.assertEqual(self.dsu.parent[1], self.dsu.parent[6])

    def test_find_error(self):
        self.dsu.find(4)
        self.assertRaises(LookupError)
