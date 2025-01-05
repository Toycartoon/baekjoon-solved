for _ in range(int(input())):
    a, b = map(int, input().split())

    e = int(str(a)[len(str(a)) - 1])
    if e in (1, 5, 6, 0):
        if not e:
            print(10)
        else:
            print(e)
    elif e == 2:
        print((6, 2, 4, 8)[b % 4])
    elif e == 3:
        print((1, 3, 9, 7)[b % 4])
    elif e == 4:
        print((6, 4)[b % 2])
    elif e == 7:
        print((1, 7, 9, 3)[b % 4])
    elif e == 8:
        print((6, 8, 4, 2)[b % 4])
    else:
        print((1, 9)[b % 2])