n, t = map(int, input().split())
dp = [0] * (t+1)
for _ in range(n):
    k, s = map(int, input().split())
    for i in range(t, -1, -1):
        dp[i] = max(dp[i], dp[i-k] + s if i-k >= 0 else 0)

print(dp[t])
