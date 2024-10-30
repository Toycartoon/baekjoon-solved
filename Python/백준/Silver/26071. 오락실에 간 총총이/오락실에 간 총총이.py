import sys


input = sys.stdin.readline

n = int(input())
g = [input() for _ in range(n)]

l = []
gom = 0
vertical = -2
horizontal = -2
for y in range(n):
    for x in range(n):
        if g[y][x] == 'G':
            l.append((x, y))
            gom += 1

            if horizontal == -2:
                horizontal = y
            elif horizontal != y:
                horizontal = -1

            if vertical == -2:
                vertical = x
            elif vertical != x:
                vertical = -1


if gom == 1:
    print(0)
    exit()

x = sorted(l, key=lambda x: x[0])
y = sorted(l, key=lambda x: x[1])

if horizontal != -1:
    print(min(x[-1][0], (n - x[0][0] - 1)))
elif vertical != -1:
    print(min(y[-1][1], (n - y[0][1] - 1)))
else:
    lu = x[-1][0] + y[-1][1]
    ru = (n - x[0][0] - 1) + y[-1][1]
    ld = x[-1][0] + (n - y[0][1] - 1)
    rd = (n - x[0][0] - 1) + (n - y[0][1] - 1)

    print(min(lu, ru, ld, rd))
