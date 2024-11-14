for t in range(int(input())):
    l = list(map(float, input().split()))

    p1, p2 = 0, 0

    for i in range(0, 6, 2):
        d = ((l[i] ** 2 + l[i+1] ** 2)) ** 0.5

        if d <= 3.0:
            p1 += 100
        elif d <= 6.0:
            p1 += 80
        elif d <= 9.0:
            p1 += 60
        elif d <= 12.0:
            p1 += 40
        elif d <= 15.0:
            p1 += 20

    for i in range(6, 11, 2):
        d = ((l[i] ** 2 + l[i+1] ** 2)) ** 0.5

        if d <= 3.0:
            p2 += 100
        elif d <= 6.0:
            p2 += 80
        elif d <= 9.0:
            p2 += 60
        elif d <= 12.0:
            p2 += 40
        elif d <= 15.0:
            p2 += 20

    if p1 > p2:
        print(f"SCORE: {p1} to {p2}, PLAYER 1 WINS.")
    elif p1 < p2:
        print(f"SCORE: {p1} to {p2}, PLAYER 2 WINS.")
    else:
        print(f"SCORE: {p1} to {p2}, TIE.")
