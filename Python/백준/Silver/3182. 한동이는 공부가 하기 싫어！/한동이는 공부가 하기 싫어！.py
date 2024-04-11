n = int(input())
l = []
for _ in range(n):
    l.append(int(input()))

ans = []
for i in range(n):
    visited = [False for _ in range(n)]
    x = i
    while not visited[x]:
        visited[x] = True
        x = l[x] - 1

    ans.append(visited.count(True))

print(ans.index(max(ans)) + 1)
