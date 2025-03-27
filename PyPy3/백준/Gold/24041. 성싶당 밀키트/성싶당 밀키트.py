import sys

input = sys.stdin.readline

n, g, k = map(int, input().split())
x = []

for i in range(n):
    s, l, o = map(int, input().split())
    x.append((s, l, o))

l, r = -1, 10 ** 12 + 1
while l + 1 < r:
    mid = (l + r) // 2

    v = 0
    x.sort(key=lambda i: -(i[0] * max(1, mid-i[1])))

    e = 0
    for i in range(len(x)):
        if x[i][2] == 1 and e < k:
            e += 1
            continue
        v += x[i][0] * max(1, mid-x[i][1])

    if v <= g:
        l = mid
    else:
        r = mid


print(l)
