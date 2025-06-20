while True:
    c, w, l, p = map(int, input().split())

    if c == w == l == p == 0:
        break

    print(c ** (w * l * p))
