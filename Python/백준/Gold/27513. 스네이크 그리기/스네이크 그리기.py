n, m = map(int, input().split())

if (n * m) % 2 == 0:
    print(n * m)
    for y in range(1, m + 1):
        print(1, y)
    f = False
    if n % 2 == 1:
        for y in range(m, 0, -1):
            f = not f
            if f:
                for x in range(2, n + 1):
                    print(x, y)
            else:
                for x in range(n, 1, -1):
                    print(x, y)
    else:
        for x in range(2, n + 1):
            print(x, m)

        for x in range(n, 1, -1):
            f = not f
            if f:
                for y in range(m - 1, 0, -1):
                    print(x, y)
            else:
                for y in range(1, m):
                    print(x, y)
else:
    print((n * m) - 1)
    f = False
    for y in range(1, m + 1):
        print(1, y)
    for y in range(m, 2, -1):
        f = not f
        if f:
            for x in range(2, n + 1):
                print(x, y)
        else:
            for x in range(n, 1, -1):
                print(x, y)
    print(n, 2)
    f = False
    for x in range(n - 1, 1, -1):
        f = not f
        if f:
            for y in range(2, 0, -1):
                print(x, y)
        else:
            for y in range(1, 3):
                print(x, y)