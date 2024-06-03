import sys
from collections import deque

sys.setrecursionlimit(10 ** 6)

p, ns, t = map(int, input().split())
g = [[] for _ in range(p+1)]
visited = [False] * (p+1)

q = deque()
back = {}

for i in range(ns):
    n, b1, b2 = map(int, input().split())
    g[n].append(b1)
    g[n].append(b2)


def bfs(x):
    visited[x] = True

    q.append(x)
    while q:
        r = q.popleft()

        for i in g[r]:
            if not visited[i]:
                visited[i] = True
                back[i] = r
                q.append(i)


bfs(1)

ans = [t]
while back[t] != 1:
    ans.append(back[t])
    t = back[t]

ans.append(1)
print(len(ans))
for i in ans[::-1]:
    print(i)
