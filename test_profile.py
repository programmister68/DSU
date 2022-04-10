from dsu import DSU
import random

import logging
logging.disable(logging.INFO)


dsu = DSU
numbers = list(range(1000000))
random.shuffle(numbers)
for i in numbers:
    dsu.make_set(i)

random.shuffle(numbers)
for i in numbers:
    dsu = dsu.delete(i)

if __name__ == '__main__':
    pass
