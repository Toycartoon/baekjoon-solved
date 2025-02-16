import sys

input = sys.stdin.readline

g = []
n = int(input())
for i in range(n):
    g.append(int(input()))


dp = [0 for _ in range(n)]
for i in range(n):
    dp[i] = max(g[i], g[i] + dp[i-1])


print(max(dp))
