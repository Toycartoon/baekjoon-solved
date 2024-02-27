n = int(input())
a = list(map(int, input().split()))
dp = [0 for _ in range(n)]

for k in range(n):
    dp[k] = 1
    for i in range(k):
        if a[i] < a[k]:
            dp[k] = max(dp[k], dp[i] + 1)


print(max(dp))
