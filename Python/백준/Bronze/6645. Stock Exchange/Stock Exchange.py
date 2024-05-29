while True:
    n, d = input().split()

    if n == "0" and d == "END":
        break

    l = []
    for i in range(int(n)):
        name, bs, p = input().split()

        l.append((name, bs, float(p)))

    print(d)
    for i in range(int(n)):
        ans = []
        for j in range(int(n)):
            if i == j:
                continue

            if l[i][1] == "buy":
                if l[j][1] == "sell" and l[i][2] >= l[j][2]:
                    ans.append(l[j][0])
            elif l[i][1] == "sell":
                if l[j][1] == "buy" and l[i][2] <= l[j][2]:
                    ans.append(l[j][0])

        print(f"{l[i][0]}:", " ".join(ans if len(ans) != 0 else ["NO-ONE"]))
