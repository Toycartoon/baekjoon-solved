from math import inf, trunc

n = int(input())
ans = inf

for i in range(n):
    a, b = map(int, input().split())
    ans = min(ans, trunc(b / a))

print(ans)
