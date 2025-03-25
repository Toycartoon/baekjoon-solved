n, k = map(int, input().split())
a = []
for i in range(n):
    a.append(int(input()))

visited = [False for _ in range(n)]
ans = 0

x = 0
f = False
while not visited[x]:
    if x == k:
        f = True
        break
    visited[x] = True

    x = a[x]
    ans += 1

if f:
    print(ans)
else:
    print(-1)
