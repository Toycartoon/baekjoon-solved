for t in range(int(input())):
    g = int(input())
    a = []
    for i in range(g):
        a.append(int(input()))

    ans = 1
    while True:
        x = set()
        for i in a:
            x.add(i % ans)

        if len(x) == g:
            print(ans)
            break

        ans += 1