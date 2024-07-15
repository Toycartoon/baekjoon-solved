n = int(input())
a = list(map(int, input().split()))
a.sort()

ans = 0
for i in range(n):
    x = a[i]
    l, r = 0, n-1

    f = False
    while l < r:
        if l == i:
            l += 1
            continue
        elif r == i:
            r -= 1
            continue
        
        m = a[l] + a[r]
        if m < x:
            l += 1
        elif m > x:
            r -= 1
        else:
            f = True
            break

    if f:
        ans += 1


print(ans)
