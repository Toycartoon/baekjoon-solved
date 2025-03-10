from itertools import permutations as p

n = int(input())
k = int(input())

g = []
for i in range(n):
    g.append(input())

ans = set()
for i in p(g, k):
    ans.add("".join(i))

print(len(ans))
