import unittest
from dsu import DSU


class TestDisjointSet(unittest.TestCase):
    def setUp(self):
        self.dsu = DSU(10)

    def test_find(self):
        for i in range(10):
            self.assertEqual(self.dsu.find(i), i)

    def test_negative_num(self):
        self.dsu2 = DSU(-10)
        self.assertEqual(self.dsu2.parent, [])


if __name__ == 'main':
    pass
