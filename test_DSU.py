import unittest
from main import DSU


class TestDSU(unittest.TestCase):
    def setUp(self, key=None):
        self.bst = DSU(key)


class TestAdd(TestDSU):
    def many_insert(self, a):
        for num in a:
            self.bst.insert(num)

    def test_create_object_with_key(self):
        link = DSU(10)
        self.assertEqual(link.key, 10)

    def test_insert_root(self):
        self.bst.insert(1)
        self.assertEqual(self.bst.key, 1)


class TestFind(TestDSU):
    def test_find_leader(self):
        link = DSU(10)
        self.assertEqual(link.key, 10)


class TestUnion(TestDSU):
    def test_union_elem(self):
        link = DSU(10)
        self.assertEqual(link.key, 10)

# if __name__ == '__main__':
#     # main()
#     pass
