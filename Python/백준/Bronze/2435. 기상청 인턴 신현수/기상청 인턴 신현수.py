from math import inf

n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = -inf
for i in range(k, n+1):
    ans = max(ans, sum(a[i-k:i]))

print(ans)
