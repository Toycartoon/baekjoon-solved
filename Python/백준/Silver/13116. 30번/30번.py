import sys
from math import floor

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

t = [[] for _ in range(1024)]
for i in range(2, 1024):
    t[i].append(floor(i / 2))
    t[floor(i / 2)].append(i)


for i in range(int(input())):
    a, b = map(int, input().split())

    pa, pb = set(), set()
    x = a
    while x != 1:
        pa.add(x)
        x = min(t[x])

    x = b
    while x != 1:
        pb.add(x)
        x = min(t[x])

    pa.add(1)
    pb.add(1)

    print(max(pa & pb) * 10)
