from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[] for _ in range(n+1)]

q = deque()
def bfs(x):
    if x not in l:
        q.append(x)

    while q:
        i = q.popleft()
        if len(g[i]) == 0:
            return "yes"

        for a in g[i]:
            if a not in l:
                q.append(a)

    return "Yes"


for i in range(m):
    u, v = map(int, input().split())
    g[u].append(v)

s = int(input())
l = set(map(int, input().split()))

print(bfs(1))
