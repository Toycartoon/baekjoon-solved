import sys

input = sys.stdin.readline


def ccw(a, b, c):
    u = (b[0] - a[0], b[1] - a[1])
    v = (c[0] - b[0], c[1] - b[1])

    return u[0] * v[1] - u[1] * v[0]


def convex_hull(arr):
    arr.sort()

    upper = []
    for p in arr:
        while len(upper) >= 2 and ccw(upper[-2][:2], upper[-1][:2], p[:2]) > 0:
            upper.pop()
        upper.append(p)

    lower = []
    for p in reversed(arr):
        while len(lower) >= 2 and ccw(lower[-2][:2], lower[-1][:2], p[:2]) > 0:
            lower.pop()
        lower.append(p)

    return upper[:-1] + lower[:-1]


while True:
    n = int(input())

    if n == 0:
        break

    arr = []
    for i in range(n):
        x, y = map(int, input().split())
        arr.append((x, y))

    layer = 0
    while True:
        c = convex_hull(arr)
        if len(c) < 3:
            break

        layer += 1
        arr = list(set(arr) - set(c))

    if layer % 2 == 0:
        print("Do not take this onion to the lab!")
    else:
        print("Take this onion to the lab!")
