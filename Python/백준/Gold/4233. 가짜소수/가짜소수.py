while True:
    p, a = map(int, input().split())

    if a == p == 0:
        break

    if a > p:
        p, a = a, p

    f = False
    for i in range(2, int(p ** 0.5)):
        if p % i == 0:
            f = True
            break

    if f:
        if pow(a, p, p) == a:
            print("yes")
        else:
            print("no")
    else:
        print("no")