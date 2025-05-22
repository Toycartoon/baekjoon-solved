import sys
from collections import deque

input = sys.stdin.readline

g = [i for i in range(10001)]
g[1] = 0

for i in range(2, int(len(g) ** 0.5) + 1):
    if g[i] == 0:
        continue

    for j in range(i * i, len(g), i):
        g[j] = 0

q = deque()
def bfs(_x):
    q.append((_x, 0))
    visited[int(_x)] = True

    while q:
        x, c = q.popleft()

        if x == b:
            return c

        for i in range(4):
            for j in range(10):
                s = x[:i] + str(j) + x[i+1:]
                if 1000 <= int(s) == g[int(s)] and not visited[int(s)]:
                    visited[int(s)] = True
                    q.append((s, c+1))

    return "Impossible"


for t in range(int(input())):
    a, b = input().strip().split()
    visited = [False for _ in range(10001)]

    print(bfs(a))
    q.clear()
