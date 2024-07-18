from collections import deque

visited = [0] * 100001
n, k = map(int, input().split())
way, count = 0, 0

q = deque()

def bfs(r):
    global count, way
    visited[r] = True
    q.append((r, 0))
    while q:
        x, c = q.popleft()

        if x == k:
            way = c
            count += 1
            continue
        if x + 1 <= 100000:
            if visited[x+1] == 0 or visited[x+1] == visited[x] + 1:
                visited[x+1] = visited[x] + 1
                q.append((x+1, c+1))
        if x - 1 >= 0 and (visited[x-1] == 0 or visited[x-1] == visited[x] + 1):
            visited[x-1] = visited[x] + 1
            q.append((x-1, c+1))
        if 2 * x <= 100000:
            if visited[2*x] == 0 or visited[2*x] == visited[x] + 1:
                visited[x * 2] = visited[x] + 1
                q.append((x*2, c+1))


bfs(n)
print(way)
print(count)
