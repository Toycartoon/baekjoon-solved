n, m = map(int, input().split())
v = list(map(int, input().split()))

l, r = 0, m+1
v.sort(reverse=True)

while l + 1 < r:
    mid = (l + r) // 2

    x = 0
    for i in range(min(n, (m-mid) // mid)):
        x += v[i]

    if sum(v)-x > x:
        r = mid
    else:
        l = mid

print(l)
