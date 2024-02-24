n, k = map(int, input().split())
dp = [0 for _ in range(k+1)]
for _ in range(n):
    w, v = map(int, input().split())
    for i in range(k, -1, -1):
        dp[i] = max(dp[i], dp[i-w] + v if i-w >= 0 else 0)

print(dp[k])
