import sys

input = sys.stdin.readline

g = []
n, m = map(int, input().split())
for i in range(n):
    g.append(int(input()))


l = 0
r = max(g) + 1
while l + 1 < r:
    mid = (l + r) // 2

    x = 0
    for i in g:
        x += i // mid

    if x >= m:
        l = mid
    else:
        r = mid


print(l)
