n = int(input())
g = [True for _ in range(n+1)]
g[0] = False
g[1] = False

s = []
for i in range(int(n ** 0.5) + 1):
    if not g[i]:
        continue

    for j in range(i * 2, len(g), i):
        g[j] = False

for i in range(len(g)):
    if g[i]:
        s.append(i)

dp = [0 for _ in range(n+1)]
dp[0] = 1

for x in s:
    for i in range(len(dp)):
        if i-x >= 0:
            dp[i] += dp[i-x] % 123456789


print(dp[-1] % 123456789)
