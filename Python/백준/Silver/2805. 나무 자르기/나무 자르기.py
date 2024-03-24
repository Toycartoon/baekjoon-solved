n, m = map(int, input().split())
h = list(map(int, input().split()))

l = -1
r = 1000000001
while l + 1 < r:
    mid = (l + r) // 2

    a = 0
    for i in h:
        if i > mid:
            a += i - mid

    if a >= m:
        l = mid
    else:
        r = mid


print(l)