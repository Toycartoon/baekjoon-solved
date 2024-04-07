for _ in range(int(input())):
    n = int(input())
    if n < 2:
        print(2)
        continue

    while True:
        f = True
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                f = not f
                break

        if f:
            print(n)
            break

        n += 1
