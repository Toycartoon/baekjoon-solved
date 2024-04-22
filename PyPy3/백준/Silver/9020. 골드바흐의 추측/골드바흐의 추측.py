p = []
for i in range(1, 10000):
    f = True
    for j in range(2, i - 1):
        if i % j == 0:
            f = False
    if f and i != 1:
        p.append(i)

for _ in range(int(input())):
    n = int(input())
    a = 10000
    s = 0
    for l in p:
        if n - l in p and n - (2 * l) >= 0:
            a = min(a, n - (2 * l))
            s = l, n - l

    print(s[0], s[1])
