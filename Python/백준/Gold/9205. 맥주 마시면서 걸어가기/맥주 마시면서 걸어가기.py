import sys
from collections import deque

input = sys.stdin.readline

q = deque()
def bfs(_x, _y):
    visited[(_x, _y)] = True
    q.append((_x, _y))

    while q:
        x, y = q.popleft()

        for dx, dy in visited:
            if not visited[(dx, dy)] and abs(dx - x) + abs(dy - y) <= 1000:
                visited[(dx, dy)] = True
                q.append((dx, dy))


for t in range(int(input())):
    n = int(input())
    hx, hy = map(int, input().split())
    visited = {(hx, hy): False}

    g = []
    for i in range(n):
        x, y = map(int, input().split())
        g.append((x, y))
        visited[(x, y)] = False

    fx, fy = map(int, input().split())
    visited[(fx, fy)] = False

    bfs(hx, hy)
    print("happy" if visited[(fx, fy)] else "sad")
