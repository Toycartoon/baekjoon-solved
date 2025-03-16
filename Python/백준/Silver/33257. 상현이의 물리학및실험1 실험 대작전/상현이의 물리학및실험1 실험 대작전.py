n, e = map(int, input().split())
d = list(map(int, input().split()))
ans = 1

d.sort()
for i in range(1, n):
    if d[i] - d[i-1] >= e:
        ans += 1

print(ans)
