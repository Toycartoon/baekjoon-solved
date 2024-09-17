from collections import deque
from math import trunc

q = deque()
def bfs(n, k):
    q.append((0, 0))
    visited[0] = True

    while q:
        x, c = q.popleft()

        if c > k:
            continue
        if x == n and c <= k:
            return True

        if x + 1 <= n and not visited[x + 1]:
            visited[x + 1] = True
            q.append((x + 1, c + 1))
        if x + trunc(x / 2) <= n and not visited[x + trunc(x / 2)]:
            visited[x + trunc(x / 2)] = True
            q.append((x + trunc(x / 2), c + 1))

    return False


n, k = map(int, input().split())
visited = [False] * (n + 1)
if bfs(n, k):
    print("minigimbob")
else:
    print("water")
