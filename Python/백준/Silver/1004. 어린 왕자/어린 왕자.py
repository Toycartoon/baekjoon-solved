for t in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())
    a = 0
    for n in range(int(input())):
        cx, cy, r = map(int, input().split())

        d1 = ((cx - x1) ** 2 + (cy - y1) ** 2) ** 0.5
        d2 = ((cx - x2) ** 2 + (cy - y2) ** 2) ** 0.5

        if d1 < r and d2 > r:
            a += 1
        elif d2 < r and d1 > r:
            a += 1

    print(a)