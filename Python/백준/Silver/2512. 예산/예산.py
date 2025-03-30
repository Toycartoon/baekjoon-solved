n = int(input())
a = list(map(int, input().split()))
x = int(input())

l, r = 0, max(a) + 1
while l + 1 < r:
    mid = (l + r) // 2

    v = 0
    for i in a:
        v += min(i, mid)

    if v <= x:
        l = mid
    else:
        r = mid


print(l)
