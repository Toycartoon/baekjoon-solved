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
        while len(upper) >= 2 and ccw(upper[-2], upper[-1], p) >= 0:
            upper.pop()
        upper.append(p)

    lower = []
    for p in reversed(arr):
        while len(lower) >= 2 and ccw(lower[-2], lower[-1], p) >= 0:
            lower.pop()
        lower.append(p)

    return upper[:-1] + lower[:-1]


n = int(input())
arr = [tuple(map(int, input().split())) for _ in range(n)]
ch = convex_hull(arr)

ch.append(ch[0])
s = 0
for i in range(len(ch)-1):
    s += ch[i][0] * ch[i+1][1]

for i in range(len(ch)-1):
    s -= ch[i][1] * ch[i+1][0]

print(abs(s) // 100)
