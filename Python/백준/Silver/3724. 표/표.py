for t in range(int(input())):
    m, n = map(int, input().split())
    g = []

    for i in range(n):
        g.append(list(map(int, input().split())))

    ans = {}
    for x in range(m):
        idx = 1
        for y in range(n):
            idx *= g[y][x]

        ans[idx] = x + 1

    print(ans[max(ans)])
