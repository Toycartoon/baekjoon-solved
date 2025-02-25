p = {}
ans = 0
s = set()

while True:
    m, *r = input().split()

    if m == "-1":
        break

    if r[1] == "wrong":
        if r[0] not in p:
            p[r[0]] = 1
        else:
            p[r[0]] += 1
    elif r[1] == "right":
        if r[0] not in s:
            if r[0] not in p:
                p[r[0]] = 0

            s.add(r[0])
            ans += int(m) + (p[r[0]] * 20)


print(len(s), ans)
