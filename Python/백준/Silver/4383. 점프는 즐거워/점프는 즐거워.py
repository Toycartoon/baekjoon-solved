while True:
    try:
        n, *l = map(int, input().split())
        v = [False for i in range(n)]
        v[0] = True

        for i in range(1, n):
            x = abs(l[i-1] - l[i])
            if 0 < x < n:
                v[x] = True

        if v.count(False) == 0:
            print("Jolly")
        else:
            print("Not jolly")
    except EOFError:
        break
