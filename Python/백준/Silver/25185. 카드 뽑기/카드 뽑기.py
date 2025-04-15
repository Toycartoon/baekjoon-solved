for t in range(int(input())):
    x = input().split()

    if len(set(x)) <= 2:
        print(":)")
        continue

    x.sort(key=lambda v: v[0])
    pos = [(0, 1, 2), (0, 1, 3), (1, 2, 3), (0, 2, 3)]
    f = False
    for a, b, c in pos:
        if x[a][1] == x[b][1] == x[c][1] and int(x[a][0]) == int(x[b][0]) - 1 == int(x[c][0]) - 2:
            f = True
            break

    if f:
        print(":)")
    else:
        print(":(")
