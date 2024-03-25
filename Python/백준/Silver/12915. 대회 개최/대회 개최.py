e, em, m, mh, h = map(int, input().split())

a = 0
while True:
    if e > 0:
        e -= 1
    else:
        if em > 0:
            em -= 1
        else:
            break

    if h > 0:
        h -= 1
    else:
        if mh > 0:
            mh -= 1
        else:
            break

    if m > 0:
        m -= 1
    else:
        if em > 0 and em >= mh:
            em -= 1
        elif mh > 0 and mh > em:
            mh -= 1
        else:
            break

    a += 1

print(a)