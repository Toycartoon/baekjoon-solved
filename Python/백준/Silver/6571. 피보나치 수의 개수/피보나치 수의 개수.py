while True:
    a, b = map(int, input().split())

    if a == b == 0:
        break

    f, g = 1, 2
    ans = 0

    i = 1
    while f <= b or g <= b:
        if (a <= f <= b and i % 2 == 1) or (a <= g <= b and i % 2 == 0):
            ans += 1

        if i % 2 == 0:
            g += f
        else:
            f += g

        i += 1

    print(ans)
