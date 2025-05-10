def check(g, n):
    f = False
    for y in range(3):
        if g[y].count(n) == 3:
            f = True

    for i in zip(*g):
        if i.count(n) == 3:
            f = True

    arr = []
    for i in range(3):
        arr.append(g[i][i])

    if arr.count(n) == 3:
        f = True

    arr = []
    for i in range(3):
        arr.append(g[i][2-i])

    if arr.count(n) == 3:
        f = True

    return f


for t in range(1, int(input())+1):
    g = [[*input()] for _ in range(3)]
    n = input()

    f = False
    for y in range(3):
        for x in range(3):
            if g[y][x] == "-":
                g[y][x] = n
                if check(g, n):
                    f = True
                    break
                else:
                    g[y][x] = "-"

        if f:
            break

    print(f"Case {t}:")
    for v in g:
        print("".join(v))
