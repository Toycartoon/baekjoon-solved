n = int(input())
dp = [0 for _ in range(n+1)]
g = []
for i in range(n):
    t, p = map(int, input().split())
    g.append((t, p))

for i in range(n-1, -1, -1):
    if i + g[i][0] > n:
        dp[i] = dp[i+1]
    else:
        dp[i] = max(dp[i+1], dp[i+g[i][0]] + g[i][1])

print(dp[0])
