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
        while len(upper) >= 2 and ccw(upper[-2][:2], upper[-1][:2], p[:2]) >= 0:
            upper.pop()
        upper.append(p)

    lower = []
    for p in reversed(arr):
        while len(lower) >= 2 and ccw(lower[-2][:2], lower[-1][:2], p[:2]) >= 0:
            lower.pop()
        lower.append(p)

    return upper[:-1] + lower[:-1]


n = int(input())
arr = [tuple(map(int, f"{input()} {i}".split())) for i in range(n)]
ans = [0] * n

for i in range(1, n//3 + 1):
    x = convex_hull(arr)
    if len(x) < 3:
        break

    for a in x:
        ans[a[2]] = i

    arr = list(set(arr) - set(x))

print(*ans)
