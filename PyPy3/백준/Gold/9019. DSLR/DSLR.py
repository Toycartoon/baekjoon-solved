import sys
from collections import deque

input = sys.stdin.readline
q = deque()


def search(r):
    q.appendleft((r, ""))
    visited = [False] * 10000

    while q:
        n, com = q.popleft()

        if visited[n]:
            continue

        visited[n] = True
        if n == b:
            return com
        else:
            q.append(((n * 2) % 10000, com + "D"))
            q.append((n - 1 if n > 0 else 9999, com + "S"))
            q.append(((n % 1000) * 10 + n // 1000, com + "L"))
            q.append(((n % 10) * 1000 + n // 10, com + "R"))


for t in range(int(input())):
    a, b = map(int, input().split())

    print(search(a))
    q.clear()
