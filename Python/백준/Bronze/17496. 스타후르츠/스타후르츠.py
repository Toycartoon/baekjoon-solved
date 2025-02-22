n, t, c, p = map(int, input().split())

ans = 0
for i in range(1, n-t+1, t):
    ans += c

print(ans * p)
