for t in range(int(input())):
    s = {}
    for n in range(int(input())):
        name, type = input().split()
        try:
            s[type] += 1
        except KeyError:
            s[type] = 1

    ans = 1
    for i in s.values():
        ans *= (i + 1)

    print(ans - 1)
