n = int(input())
a = list(map(int, input().split()))
dp = [1 for _ in range(n)]

for i in range(1, n):
    for j in range(i):
        if a[i] > a[j]:
            dp[i] += dp[j]
            dp[i] %= 998244353

print(*dp)
