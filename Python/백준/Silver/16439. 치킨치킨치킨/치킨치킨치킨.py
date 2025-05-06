from itertools import combinations as comb

n, m = map(int, input().split())
g = [list(map(int, input().split())) for _ in range(n)]

mx = 0
for i in comb(range(m), 3):
    v = 0
    for a in range(n):
        v += max(g[a][i[0]], g[a][i[1]], g[a][i[2]])

    mx = max(mx, v)

print(mx)
