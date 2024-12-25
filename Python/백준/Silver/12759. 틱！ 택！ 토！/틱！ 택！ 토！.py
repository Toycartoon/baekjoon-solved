def check(g):
    for i in range(3):
        if g[i].count(1) == 3 or g[i].count(2) == 3:
            return g[i][0]


    for i in range(3):
        f = True
        x = g[0][i] if g[0][i] != 0 else -1
        for j in range(3):
            if g[j][i] != x:
                f = False
                break

        if f:
            return x


    f = True
    x = g[0][0] if g[0][0] != 0 else -1
    for i in range(3):
        if g[i][i] != x:
            f = False
            break

    if f:
        return x


    f = True
    x = g[2][0] if g[2][0] != 0 else -1
    for i in range(3):
        if g[2-i][i] != x:
            f = False
            break

    if f:
        return x

    return 0


p = int(input())
g = [[0 for _ in range(3)] for __ in range(3)]

for i in range(9):
    y, x = map(int, input().split())
    g[y-1][x-1] = p

    if p == 2:
        p = 1
    else:
        p = 2

    ans = check(g)
    if ans != 0:
        print(ans)
        exit()


print(0)
