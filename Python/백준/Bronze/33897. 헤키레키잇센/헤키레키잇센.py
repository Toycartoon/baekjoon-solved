n = int(input())
a = list(map(int, input().split()))

mx = 1
ans = 1
x = 1
for i in range(1, n):
    if a[i-1] <= a[i]:
        x += 1
    else:
        mx = max(mx, x)
        x = 1
        ans += 1

mx = max(mx, x)
print(ans, mx)
