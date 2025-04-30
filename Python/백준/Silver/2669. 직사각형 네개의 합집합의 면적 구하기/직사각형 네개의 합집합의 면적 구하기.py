g = [[False for _ in range(100)] for __ in range(100)]

for i in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            g[y][x] = True

ans = 0
for y in g:
    ans += y.count(True)

print(ans)
