from random import randint

from dsu import DSU

dsu = DSU()
test_elem = randint(0, 10000)

for i in range(10000):
    dsu.push(test_elem)

for j in range(10000):
    dsu.make_set()

for k in range(10000):
    dsu.find(test_elem)

for h in range(1000000):
    dsu.union(test_elem, test_elem)
