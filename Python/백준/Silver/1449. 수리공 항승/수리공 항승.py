n, l = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
ans = 1

x = a[0]
for i in range(1, n):
    if a[i] - x > l-1:
        ans += 1
        x = a[i]

print(ans)
