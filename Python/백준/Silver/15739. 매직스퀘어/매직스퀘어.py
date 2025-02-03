n = int(input())
g = [list(map(int, input().split())) for _ in range(n)]

f = True
s = sum(g[0])

l = set()
for y in range(n):
    for x in range(n):
        l.add(g[y][x])

if sum(l) != n ** 2 * (n ** 2 + 1) // 2 or len(l) != n ** 2:
    f = False

for i in range(n):
    if sum(g[i]) != s:
        f = False

for i in range(n):
    x = 0
    for j in range(n):
        x += g[j][i]

    if x != s:
        f = False


x = 0
for i in range(n):
    x += g[i][i]

if x != s:
    f = False


x = 0
for i in range(n):
    x += g[n-i-1][i]

if x != s:
    f = False


print(str(f).upper())
