import sys

input = sys.stdin.readline

n, m, k = map(int, input().split())

g = []
for i in range(k):
    f, d = map(int, input().split())
    g.append((abs(f-1) + abs(d-(m+1)), i+1))

g.sort()
print(g[0][1])
