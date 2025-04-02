n, m = map(int, input().split())
a = list(map(int, input().split()))

g = [list(map(int, input().split())) for _ in range(n)]
ans = 0
b = a[0]
for i in range(1, m):
    ans += g[b-1][a[i]-1]
    b = a[i]

print(ans)
