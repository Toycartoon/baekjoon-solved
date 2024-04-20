import collections

m, n, h = map(int, input().split())

q = collections.deque()
g = []
ans = -1

for i in range(h):
    v = []
    for j in range(n):
        v.append(list(map(int, input().split())))

    g.append(v)


for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k] == 1:
                q.append((i, j, k, 0))


def pos(x, y, z, day):
    if 0 > x or x >= h:
        return
    if 0 > y or y >= n:
        return
    if 0 > z or z >= m:
        return
    if g[x][y][z] == 1 or g[x][y][z] == -1:
        return

    q.append((x, y, z, day+1))
    g[x][y][z] = 1
    return


while q:
    _h, _n, _m, day = q.popleft()

    if day > ans:
        ans = day

    pos(_h-1, _n, _m, day)
    pos(_h+1, _n, _m, day)
    pos(_h, _n-1, _m, day)
    pos(_h, _n+1, _m, day)
    pos(_h, _n, _m-1, day)
    pos(_h, _n, _m+1, day)


check = True
for i in range(h):
    for j in range(n):
        for k in range(m):
            if g[i][j][k] == 0:
                check = False
                break


if check:
    print(ans)
else:
    print(-1)
