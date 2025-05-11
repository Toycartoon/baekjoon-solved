n = int(input())
g = [[False for _ in range(501)] for __ in range(501)]

for i in range(n):
    x1, y1, x2, y2 = map(int, input().split())

    for y in range(y1, y2):
        for x in range(x1, x2):
            g[y][x] = True

ans = 0
for y in range(501):
    for x in range(501):
        if g[y][x]:
            ans += 1

print(ans)
