from itertools import permutations as p

a, b, c = input().split()
x = input()

i = list(p(sorted([a, b, c]), 3))
print(i.index(tuple([*x])) + 1)