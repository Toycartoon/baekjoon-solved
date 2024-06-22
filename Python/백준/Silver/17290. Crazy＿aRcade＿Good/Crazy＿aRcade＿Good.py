g = [[False] * 10 for _ in range(10)]
r, c = map(int, input().split())
s = [[*input()] for _ in range(10)]

for y in range(10):
    for x in range(10):
        if s[y][x] == 'o':
            for dx in range(10):
                g[y][dx] = True

            for dy in range(10):
                g[dy][x] = True

dist = []
for y in range(10):
    for x in range(10):
        if not g[y][x]:
            dist.append(abs(y-r+1) + abs(x-c+1))

print(min(dist))
