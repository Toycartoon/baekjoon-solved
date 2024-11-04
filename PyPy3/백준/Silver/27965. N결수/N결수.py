n, k = map(int, input().split())
dp = [0 for _ in range(n+1)]

if k == 1:
    print(0)
    exit()

for i in range(1, n+1):
    dp[i] = (dp[i-1] * (10 ** len(str(i))) + i) % k

print(dp[-1])