import sys
from math import lcm

input = sys.stdin.readline

k, n = map(int, input().split())
l = []
a = set()

for i in range(k):
    x = input().strip()
    l.append(x)
    a.add(len(x))

l.sort(key=lambda x: int(x))
u = l
for i in range(n-k):
    u.append(l[-1])

c = lcm(*a)
u = sorted(u, key=lambda x: (c * x), reverse=True)

for i in u:
    print(i, end="")
