from math import inf


n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [inf for _ in range(m+1)]
for k in range(n):
    for i in range(m, -1, -1):
        dp[i] = min(dp[i], dp[i-a[k]] + c[k] if i-a[k] > 0 else c[k])

print(dp[m])
