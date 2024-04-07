# Special Thanks : ohwphil

n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

dp = [0 for _ in range(10001)]
for k in range(n):
    for i in range(10000-c[k], -1, -1):
        dp[i+c[k]] = max(dp[i+c[k]], dp[i] + a[k])


for ans in range(10001):
    if dp[ans] >= m:
        print(ans)
        break
