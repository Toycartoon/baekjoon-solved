while True:
    a, b, c, d = list(map(int, input().split()))

    if a == b == c == d == 0:
        break

    if d == 0:
        d = a * b * c
    elif a == 0:
        a = d // (b * c)
    elif b == 0:
        b = d // (a * c)
    elif c == 0:
        c = d // (a * b)

    print(a, b, c, d)
