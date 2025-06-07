import sys

input = sys.stdin.readline

g = []
for i in range(int(input())):
    c, r, s, d = input().split()
    g.append((2 * int(r) + 3 * int(s) + int(d), c))

g.sort(key=lambda x: (-x[0], x[1]))
if len(g) >= 1:
    print(g[0][1])

if len(g) >= 2:
    print(g[1][1])
