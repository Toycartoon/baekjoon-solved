for t in range(int(input())):
    n = int(input())

    a = []
    for i in range(1, n):
        if n % i == 0:
            a.append(i)

    if sum(a) <= n:
        print("BOJ 2022")
        continue

    f = True
    for i in a:
        v = 0
        for x in range(1, i):
            if i % x == 0:
                v += x

        if v > i:
            f = False
            break

    if f:
        print("Good Bye")
    else:
        print("BOJ 2022")
