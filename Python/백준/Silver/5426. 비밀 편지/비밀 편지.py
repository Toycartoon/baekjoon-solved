for _ in range(int(input())):
    s = input()
    l = []
    i = 0
    while True:
        if i >= len(s):
            break
        l.append(s[i:i + int(len(s) ** 0.5)])
        i += int(len(s) ** 0.5)

    res = ""
    for i in range(int(len(s) ** 0.5) - 1, -1, -1):
        for j in range(int(len(s) ** 0.5)):
            res += l[j][i]
    print(res)