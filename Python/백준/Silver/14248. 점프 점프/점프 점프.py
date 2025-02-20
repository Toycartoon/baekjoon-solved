from collections import deque

n = int(input())
a = list(map(int, input().split()))
s = int(input())

q = deque()
visited = [False for _ in range(n)]
def bfs(x):
    q.append(x)
    visited[x] = True

    while q:
        i = q.popleft()

        if 0 <= i + a[i] < n:
            if not visited[i+a[i]]:
                visited[i+a[i]] = True
                q.append(i+a[i])
        if 0 <= i - a[i] < n:
            if not visited[i-a[i]]:
                visited[i-a[i]] = True
                q.append(i-a[i])


bfs(s-1)
print(visited.count(True))
