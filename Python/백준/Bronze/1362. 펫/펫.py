i = 0
while True:
    o, w = map(int, input().split())

    if o == w == 0:
        break

    i += 1
    d = False
    while True:
        r, n = input().split()

        if r == "E":
            w -= int(n)
            if w <= 0:
                print(f"{i} RIP")
                d = True
        elif r == "F" and not d:
            w += int(n)
        elif r == "#":
            if d:
                break
            if (o // 2) < w < (o * 2):
                print(f"{i} :-)")
                break
            else:
                print(f"{i} :-(")
                break