import sys

input = sys.stdin.readline

n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

dp = [[0, 0] for _ in range(n)]
dp[0][0] = a[0]
dp[0][1] = a[0]
for i in range(1, n):
    dp[i][0] = max(dp[i-2][0], dp[i-2][1]) + a[i]
    dp[i][1] = dp[i-1][0] + a[i]

print(max(dp[-1]))
