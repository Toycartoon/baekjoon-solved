import sys, collections

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

n = int(input())
g = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]
q = collections.deque()
ans = []


def bfs(r, d):
    q.append(r)
    while len(q) != 0:
        v = q.popleft()
        dw = visited[v]
        for i in g[v]:
            if visited[i[0]] == 0:
                visited[i[0]] = dw + i[1]
                q.append(i[0])

    visited[r] = d


if n == 2:
    a, b, w = map(int, input().split())
    print(w)
    exit()

for _ in range(n-1):
    a, b, w = map(int, input().split())

    g[a].append((b, w))
    g[b].append((a, w))


bfs(1, 0)
ans.append(max(visited))

x = []
for i in range(n+1):
    if visited[i] == max(visited):
        x.append(i)

for y in x:
    visited = [0 for _ in range(n + 1)]
    bfs(y, 0)
    ans.append(max(visited))

print(sorted(ans)[-1])
