n = int(input())
v = list(map(int, input().split()))

s = sum(v)
ans = s - v[0]
for i in range(n):
    ans = min(ans, s-v[i])

print(ans)
