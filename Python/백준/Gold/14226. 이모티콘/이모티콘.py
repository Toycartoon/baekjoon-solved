from collections import deque

q = deque()
visited = set()
def bfs(e):
    q.append((1, 0, 0))
    visited.add((1, 0, 0))

    while q:
        x, c, t = q.popleft()
        visited.discard((x, c, t))

        if x == e:
            return t

        if (x, x, t+1) not in visited:
            q.append((x, x, t+1))
            visited.add((x, x, t+1))
        if x + c <= e and (x+c, c, t+1) not in visited:
            q.append((x+c, c, t+1))
            visited.add((x+c, c, t+1))
        if 0 < x - 1 and (x-1, c, t+1) not in visited:
            q.append((x-1, c, t+1))
            visited.add((x-1, c, t+1))


s = int(input())
print(bfs(s))
