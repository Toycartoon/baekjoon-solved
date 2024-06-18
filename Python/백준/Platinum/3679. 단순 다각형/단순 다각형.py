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
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) > 0:
            upper.pop()
        upper.append(p)

    lower = []
    for p in reversed(arr):
        if p not in upper:
            lower.append(p)

    return upper + lower


for t in range(int(input())):
    c, *g = map(int, input().split())
    arr = []

    for i in range(0, c * 2, 2):
        arr.append((g[i], g[i+1], i // 2))

    ans = convex_hull(arr)
    for i in ans:
        print(i[2], end=" ")
    print()
