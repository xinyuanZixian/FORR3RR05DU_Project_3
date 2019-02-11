import string
from itertools import combinations, permutations

lst = list(combinations(string.ascii_lowercase, 3))
print(len(lst))

