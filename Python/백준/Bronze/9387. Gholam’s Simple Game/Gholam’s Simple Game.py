for _ in range(int(input())):
    m, n = map(int, input().split())

    a = list(map(int, input().split()))
    try:
        i = a.index(2)
        dx = 1
    except:
        i = a.index(3)
        dx = -1

    x = 0
    ans = 0
    while n > x:
        i += dx
        if i < 0:
            dx = 1
            i = 1
        elif i >= len(a):
            dx = -1
            i = len(a)-2

        if a[i] == 0:
            ans += 1

        x += 1

    print(ans)
