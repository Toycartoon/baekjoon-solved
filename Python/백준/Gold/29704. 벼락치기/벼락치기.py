import sys

input = sys.stdin.readline

n, t = map(int, input().split())
dp = [0 for _ in range(t+1)]
l = []

for _ in range(n):
    d, m = map(int, input().split())
    l.append(m)
    
    for i in range(t, -1, -1):
        dp[i] = max(dp[i], dp[i-d] + m if i - d >= 0 else 0)


print(sum(l) - dp[t])
