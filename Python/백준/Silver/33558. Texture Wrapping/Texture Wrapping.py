n, m = map(int, input().split())
u, v = map(int, input().split())
g = [[*input()] for _ in range(u)]
s = input()

ans = [["" for _ in range(m)] for __ in range(n)]
for y in range(min(n, u)):
    for x in range(min(m, v)):
        ans[y][x] = g[y][x]

if s == "clamp-to-edge":
    for y in range(min(n, u)):
        for x in range(v, m):
            ans[y][x] = ans[y][x-1]

    for y in range(u, n):
        for x in range(m):
            ans[y][x] = ans[y-1][x]
elif s == "repeat":
    for y in range(min(u, n)):
        for x in range(v, m):
            ans[y][x] = ans[y][x-v]

    for y in range(u, n):
        for x in range(m):
            ans[y][x] = ans[y-u][x]
elif s == "mirrored-repeat":
    for y in range(min(n, u)):
        for x in range(v, m):
            ans[y][x] = ans[y][x-(x % v)*2-1]

    for y in range(u, n):
        for x in range(m):
            ans[y][x] = ans[y-(y % u)*2-1][x]


for v in ans:
    print("".join(v))
