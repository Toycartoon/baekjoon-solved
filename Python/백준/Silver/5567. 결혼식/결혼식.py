from collections import deque
from math import inf
import sys

input = sys.stdin.readline
q = deque()

n = int(input())
m = int(input())
g = [[] for _ in range(n)]
visited = [inf for _ in range(n)]


def bfs(s):
    visited[s] = 0
    q.append(s)

    while q:
        x = q.popleft()

        for i in g[x]:
            if visited[i] > visited[x] + 1:
                visited[i] = visited[x] + 1
                q.append(i)


for i in range(m):
    a, b = map(int, input().split())

    g[a-1].append(b-1)
    g[b-1].append(a-1)


bfs(0)
ans = 0
for i in range(1, n):
    if visited[i] <= 2:
        ans += 1

print(ans)
