from collections import deque


n = int(input())

g = {}
for i in range(n):
    a, _, b = input().split()

    if a not in g:
        g[a] = []
    if b not in g:
        g[b] = []

    g[a].append(b)

q = deque()
def bfs(x, e):
    q.append(x)

    while q:
        x = q.popleft()

        if e in g[x]:
            return "T"

        for i in g[x]:
            q.append(i)

    return "F"


for m in range(int(input())):
    a, _, b = input().split()

    print(bfs(a, b))
