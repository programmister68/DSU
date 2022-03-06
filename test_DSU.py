import unittest
from dsu import DSU


class TestDSU(unittest.TestCase):
    def setUp(self):
        pass

    def test_find(self):
        self.assertEqual(self.parent[1], self.find(self.parent[1]))

# if __name__ == '__main__':
#     # main()
#     pass
