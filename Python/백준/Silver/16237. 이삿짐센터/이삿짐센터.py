a, b, c, d, e = map(int, input().split())
ans = e

ans += d
a -= d

while c > 0:
    if b > 0:
        ans += 1
        c -= 1
        b -= 1
    elif a > 0:
        c -= 1
        a -= 2
        ans += 1
    else:
        ans += c
        c = 0

while b > 0:
    if a > 0:
        if b >= 2:
            b -= 2
            a -= 1
            ans += 1
        else:
            b -= 1
            a -= 3
            ans += 1
    else:
        b -= 2
        ans += 1

while a > 0:
    a -= 5
    ans += 1

print(ans)