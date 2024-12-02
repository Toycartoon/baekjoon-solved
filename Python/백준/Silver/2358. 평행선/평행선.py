import sys

input = sys.stdin.readline

n = int(input())
l = []

x, y = {}, {}
for i in range(n):
    xi, yi = map(int, input().split())
    l.append((xi, yi))

for xi, yi in l:
    if xi not in x:
        x[xi] = 1
    else:
        x[xi] += 1

    if yi not in y:
        y[yi] = 1
    else:
        y[yi] += 1


ans = 0
for i in x.values():
    if i >= 2:
        ans += 1

for i in y.values():
    if i >= 2:
        ans += 1


print(ans)
