n, m = map(int, input().split())
a = list(map(int, input().split()))

l = 0
r = 0
mx = 0
s = 0
while r <= n:
    if s > m:
        s -= a[l]
        l += 1
    elif s > mx:
        mx = s
    else:
        try:
            s += a[r]
            r += 1
        except IndexError:
            break

print(mx)