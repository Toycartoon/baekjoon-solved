for p in range(int(input())):
    t, *a = map(int, input().split())

    ans = 0
    for i in range(len(a)):
        for j in range(i, 0, -1):
            if a[j - 1] > a[j]:
                a[j - 1], a[j] = a[j], a[j - 1]
                ans += 1

    print(t, ans)
