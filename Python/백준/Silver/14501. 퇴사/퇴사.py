n = int(input())
dp = [0 for _ in range(n+1)]
g = []
for i in range(n):
    t, p = map(int, input().split())
    g.append((t, p))

for i in range(n):
    for j in range(i+g[i][0], n+1):
        dp[j] = max(dp[j], dp[i] + g[i][1])

print(dp[-1])
