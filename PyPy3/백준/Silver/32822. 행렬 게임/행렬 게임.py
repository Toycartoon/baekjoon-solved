import sys

input = sys.stdin.readline

n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

c = []
for x in range(n):
    g = []
    for y in range(n):
        g.append(abs(a[y][x] - b[y][x]))

    c.append(g)

ans = 0
d = list(map(int, input().split()))
for i in d:
    ans += max(c[i-1])

print(ans)
