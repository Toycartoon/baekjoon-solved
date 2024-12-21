from itertools import permutations as p

n = int(input())

for i in p(range(1, n+1), n):
    print(*i)
