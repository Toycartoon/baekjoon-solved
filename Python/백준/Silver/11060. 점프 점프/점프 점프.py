from collections import deque

n = int(input())
a = list(map(int, input().split()))
visited = [False] * n

q = deque()
def bfs(x):
    visited[x] = True
    q.append((x, 0))

    while q:
        x, c = q.popleft()

        if x == n-1:
            return c

        for i in range(1, a[x]+1):
            if x + i < n:
                if not visited[x+i]:
                    visited[x+i] = True
                    q.append((x+i, c+1))


    return -1


print(bfs(0))
