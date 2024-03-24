n = int(input())
a = list(map(int, input().split()))

dp = [0 for _ in range(n)]
for i in range(n-1, -1, -1):
    dp[i] = 1
    for j in range(n-1, i-1, -1):
        if a[i] > a[j]:
            dp[i] = max(dp[i], dp[j] + 1)


print(max(dp))
