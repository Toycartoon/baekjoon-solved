p, n = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = 0
for i in range(n):
    if p >= 200:
        break
    p += a[i]
    ans += 1

print(ans)