n, k = map(int, input().split())
dp = [0] * (n+1)
for _ in range(k):
    i, t = map(int, input().split())
    for x in range(n, -1, -1):
        dp[x] = max(dp[x], dp[x-t] + i if x-t >= 0 else 0)

print(dp[n])
