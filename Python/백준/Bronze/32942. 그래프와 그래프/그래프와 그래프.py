a, b, c = map(int, input().split())

g = [[] for _ in range(11)]

for x in range(1, 11):
    if a == 0:
        g[x].append(c // b if c % b == 0 and 1 <= c // b <= 10 else 0)
    elif b == 0:
        i = c // a if c % a == 0 and 1 <= c // a <= 10 else 0
        g[i].append(x)
    else:
        i = (c - a * x) // b if (c - a * x) % b == 0 else 0
        if 1 <= i <= 10:
            g[x].append(i)


for i in range(1, 11):
    if len(g[i]) == 0:
        print(0)
    else:
        print(*sorted(g[i]))
