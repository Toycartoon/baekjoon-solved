l = []
for i in range(int(input())):
    s = input()
    n = 0
    for j in s:
        if j.isnumeric():
            n += int(j)

    l.append((s, n))

l = sorted(sorted(sorted(l, key=lambda x: x[0]), key=lambda x: x[1]), key=lambda x: len(x[0]))
for i in l:
    print(i[0])
