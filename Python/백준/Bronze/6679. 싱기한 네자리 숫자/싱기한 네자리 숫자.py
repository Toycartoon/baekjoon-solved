for n in range(1000, 10000):
    d = 0
    t = 0
    h = 0

    i = n
    while i > 0:
        t += i % 12
        i //= 12

    i = n
    while i > 0:
        h += i % 16
        i //= 16

    i = n
    while i > 0:
        d += i % 10
        i //= 10
    
    if d == t == h:
        print(n)
