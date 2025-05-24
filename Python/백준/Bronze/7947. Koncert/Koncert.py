from math import floor

for z in range(int(input())):
    r, g, b = 0, 0, 0

    for _ in range(10):
        i, j, k = map(int, input().split())
        r += i
        g += j
        b += k

    print(floor((r / 10) + 0.5), floor((g / 10) + 0.5), floor((b / 10) + 0.5))
