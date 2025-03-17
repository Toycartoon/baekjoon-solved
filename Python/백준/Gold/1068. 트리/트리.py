n = int(input())
a = list(map(int, input().split()))

t = [[] for _ in range(n)]
visited = [False for _ in range(n)]
r = -1

q = []
def dfs(x):
    visited[x] = True
    q.append(x)
    ans = 0

    while q:
        x = q.pop()

        if len(t[x]) == 1:
            ans += 1
            continue

        for i in t[x]:
            if not visited[i]:
                visited[i] = True
                q.append(i)

    return ans


d = int(input())
for i in range(n):
    if a[i] == d or i == d:
        if a[i] == -1:
            r = i
        continue

    if a[i] != -1:
        t[i].append(a[i])
        t[a[i]].append(i)
    else:
        r = i
        t[i].append(i)

t[d].clear()
print(dfs(r))
