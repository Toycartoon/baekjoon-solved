for t in range(int(input())):
    a, b = map(int, input().split())
    m, n = a, b

    while m % n != 0:
        if m < n:
            m, n = n, m
        else:
            t = m % n
            m = n
            n = t

    print(n)