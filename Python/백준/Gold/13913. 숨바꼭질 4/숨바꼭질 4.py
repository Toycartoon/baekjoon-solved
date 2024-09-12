from collections import deque

visited = [-1] * 100001
n, k = map(int, input().split())

q = deque()

def bfs(r):
    visited[r] = r
    q.append((r, 0))
    while q:
        x, c = q.popleft()
        if x == k:
            return c
        if x + 1 <= 100000:
            if visited[x+1] == -1:
                visited[x+1] = x
                q.append((x+1, c+1))
        if x - 1 >= 0 and visited[x-1] == -1:
            visited[x-1] = x
            q.append((x-1, c+1))
        if 2 * x <= 100000:
            if visited[2*x] == -1:
                visited[x * 2] = x
                q.append((x*2, c+1))


print(bfs(n))
ptr = k
ans = []
while ptr != n:
    ans.append(ptr)
    ptr = visited[ptr]


ans.append(n)
print(*ans[::-1])
