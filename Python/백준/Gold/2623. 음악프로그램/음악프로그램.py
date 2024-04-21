import sys
from collections import deque


input = sys.stdin.readline

n, m = map(int, input().split())
degree = [0] * (n + 1)
g = [[] for _ in range(n+1)]

q = deque()
for _ in range(m):
    sn, *t = map(int, input().split())
    for i in range(sn-1):
        g[t[i]].append(t[i+1])
        degree[t[i+1]] += 1


for i in range(1, n+1):
    if degree[i] == 0:
        q.append(i)


ans = []
while q:
    cur = q.popleft()
    ans.append(cur)
    for nxt in g[cur]:
        degree[nxt] -= 1
        if degree[nxt] == 0:
            q.append(nxt)


if len(ans) != n:
    print(0)
    exit()

for i in ans:
    print(i)
