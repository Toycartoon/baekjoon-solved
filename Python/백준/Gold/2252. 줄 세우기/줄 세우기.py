import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
degree = [0] * (n + 1)
g = [[] for _ in range(n+1)]

d = deque()
for _ in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    degree[b] += 1


for i in range(1, n+1):
    if degree[i] == 0:
        d.append(i)


ans = []
while d:
    cur = d.popleft()
    ans.append(cur)
    for nxt in g[cur]:
        degree[nxt] -= 1
        if degree[nxt] == 0:
            d.append(nxt)


for i in ans:
    print(i, end=" ")
