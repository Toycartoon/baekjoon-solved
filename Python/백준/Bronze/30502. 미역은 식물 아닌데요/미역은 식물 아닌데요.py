import sys

input = sys.stdin.readline

n, m = map(int, input().split())
g = [[-1, -1] for _ in range(n)]

for i in range(m):
    a, b, c = input().strip().split()

    if b == "P":
        g[int(a)-1][0] = int(c)
    elif b == 'M':
        g[int(a)-1][1] = int(c)


mi, mx = 0, 0
for pm in g:
    if pm[0] == 1 and pm[1] == 0:
        mx += 1
        mi += 1
    elif pm[1] == 0 and pm[0] == -1:
        mx += 1
    elif pm[0] == 1 and pm[1] == -1:
        mx += 1
    elif pm[0] == pm[1] == -1:
        mx += 1


print(mi, mx)
