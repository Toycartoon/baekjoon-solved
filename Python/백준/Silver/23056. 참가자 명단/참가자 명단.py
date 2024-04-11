n, m = map(int, input().split())
c = [0 for _ in range(n+1)]
bl = []
wl = []

while True:
    num, name = input().split()
    if num == name == "0":
        break

    if c[int(num)] < m:
        c[int(num)] += 1

        if int(num) % 2 == 1:
            bl.append((int(num), name))
        else:
            wl.append((int(num), name))


bl = sorted(sorted(sorted(bl, key=lambda x: x[1]), key=lambda x: len(x[1])), key=lambda x: x[0])
wl = sorted(sorted(sorted(wl, key=lambda x: x[1]), key=lambda x: len(x[1])), key=lambda x: x[0])
for i in bl + wl:
    print(i[0], i[1])
