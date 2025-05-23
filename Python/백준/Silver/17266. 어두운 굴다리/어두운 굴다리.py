n = int(input())
m = int(input())
x = list(map(int, input().split()))

l, r = 0, n+1

while l + 1 < r:
    mid = (l + r) // 2

    f = True
    b = 0
    for i in x:
        if b < i - mid:
            f = False
            break

        b = i + mid

    if b < n:
        f = False

    if f:
        r = mid
    else:
        l = mid

print(r)
