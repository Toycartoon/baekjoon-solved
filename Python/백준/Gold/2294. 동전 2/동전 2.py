from math import inf

n, k = map(int, input().split())
dp = [inf for _ in range(k+1)]

c = []
for i in range(n):
    a = int(input())
    c.append(a)
    
    if a <= k:
        dp[a] = 1

for i in range(1, len(dp)):
    for x in c:
        dp[i] = min(dp[i], dp[i-x]+1 if i-x > 0 else inf)

print(dp[-1] if dp[-1] != inf else -1)
