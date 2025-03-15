import sys
from collections import deque

input = sys.stdin.readline

q = deque()
def bfs(i):
    visited[i] = True
    q.append(i)

    while q:
        x = q.popleft()

        for i in g[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)


t = 1
while True:
    n, m = map(int, input().split())
    g = [[] for _ in range(n+1)]
    visited = [False for _ in range(n+1)]

    if n == m == 0:
        break

    for x in range(m):
        i, j = map(int, input().split())
        g[i].append(j)
        g[j].append(i)

    ans = 0
    for i in range(1, n+1):
        if not visited[i]:
            bfs(i)
            ans += 1

    print(f"Case {t}: {ans}")
    t += 1
