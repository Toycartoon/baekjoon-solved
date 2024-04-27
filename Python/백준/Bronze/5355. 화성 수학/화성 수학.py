for _ in range(int(input())):
    n, *p = input().split()

    n = float(n)
    for i in p:
        if i == "@":
            n *= 3.0
        elif i == "%":
            n += 5.0
        elif i == "#":
            n -= 7.0

    print("{:.02f}".format(n))